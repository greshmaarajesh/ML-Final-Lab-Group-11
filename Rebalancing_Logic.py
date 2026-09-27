
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# ASSUMED SCENARIO PARAMETERS
# These values are NOT provided by the UCI dataset or project guide.
# ---------------------------------------------------------------------------

REVENUE_PER_RIDE = 3.50
HOLDING_COST_PER_BIKE = 0.75
REBALANCE_TRUCK_COST = 45.00
BIKES_PER_TRUCK_RUN = 150


def recommended_fleet(predicted_demand: pd.Series, safety_margin: float) -> pd.Series:
    """Convert model predictions into recommended fleet stock."""

    return np.ceil(
        predicted_demand * (1 + safety_margin)
    )


def classify_decision(
    stocked: pd.Series,
    actual_demand: pd.Series
) -> np.ndarray:
    """Classify each hour as UNDERSTOCK, OVERSTOCK, or OK."""

    diff = stocked - actual_demand

    return np.select(
        [
            diff < 0,
            diff > 0
        ],
        [
            "UNDERSTOCK",
            "OVERSTOCK"
        ],
        default="OK"
    )


def financial_impact(
    stocked: pd.Series,
    actual_demand: pd.Series
) -> pd.DataFrame:
    """Calculate lost rides, idle bikes, and their modeled costs."""

    lost_rides = np.clip(
        actual_demand - stocked,
        a_min=0,
        a_max=None
    )

    idle_bikes = np.clip(
        stocked - actual_demand,
        a_min=0,
        a_max=None
    )

    return pd.DataFrame({
        "lost_rides": lost_rides,
        "idle_bikes": idle_bikes,
        "lost_revenue": (
            lost_rides * REVENUE_PER_RIDE
        ),
        "holding_cost": (
            idle_bikes * HOLDING_COST_PER_BIKE
        )
    })


def daily_truck_cost(
    df_with_decision: pd.DataFrame
) -> pd.DataFrame:
    """
    Calculate daily truck-run cost based on
    additional bikes created by the safety margin.
    """

    added_bikes = (
        df_with_decision["recommended_fleet"]
        - df_with_decision["predicted_cnt"]
    ).clip(lower=0)

    daily = added_bikes.groupby(
        df_with_decision["dteday"]
    ).sum()

    trucks = np.ceil(
        daily / BIKES_PER_TRUCK_RUN
    )

    cost = (
        trucks * REBALANCE_TRUCK_COST
    ).rename("daily_truck_cost")

    return cost.reset_index()


def generate_decision_metrics(
    df: pd.DataFrame,
    safety_margin: float
) -> pd.DataFrame:
    """
    Full AE pipeline:

    model predictions
        -> safety margin
        -> recommended fleet
        -> operational decision
        -> financial impact

    Required columns:
    dteday
    actual_cnt
    predicted_cnt
    """

    out = df.copy()

    out["safety_margin"] = safety_margin

    out["recommended_fleet"] = recommended_fleet(
        out["predicted_cnt"],
        safety_margin
    )

    out["decision"] = classify_decision(
        out["recommended_fleet"],
        out["actual_cnt"]
    )

    impact = financial_impact(
        out["recommended_fleet"],
        out["actual_cnt"]
    )

    out = pd.concat(
        [
            out.reset_index(drop=True),
            impact.reset_index(drop=True)
        ],
        axis=1
    )

    out["net_operational_cost"] = (
        out["lost_revenue"]
        + out["holding_cost"]
    )

    trucks = daily_truck_cost(out)

    out = out.merge(
        trucks,
        on="dteday",
        how="left"
    )

    return out


def cost_matrix(
    decision_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Confusion-cost-style summary adapted for
    the regression/business decision problem.

    Summarizes UNDERSTOCK, OVERSTOCK and OK decisions.
    """

    summary = decision_df.groupby(
        "decision"
    ).agg(
        hours=("decision", "size"),
        total_lost_rides=("lost_rides", "sum"),
        total_idle_bikes=("idle_bikes", "sum"),
        total_lost_revenue=("lost_revenue", "sum"),
        total_holding_cost=("holding_cost", "sum")
    ).reset_index()

    summary["pct_of_hours"] = (
        summary["hours"]
        / len(decision_df)
        * 100
    ).round(1)

    return summary


def tune_safety_margin(
    df: pd.DataFrame,
    margins=None
) -> pd.DataFrame:
    """
    Test different safety margins and calculate
    the modeled total cost for each margin.

    The tuning table is displayed in
    Metrics_Analysis.ipynb and is not saved
    as a separate CSV.
    """

    if margins is None:

        margins = np.round(
            np.arange(
                0.0,
                0.41,
                0.05
            ),
            2
        )

    rows = []

    for m in margins:

        metrics = generate_decision_metrics(
            df,
            m
        )

        total_truck_cost = (
            metrics
            .drop_duplicates("dteday")
            ["daily_truck_cost"]
            .sum()
        )

        rows.append({

            "safety_margin": m,

            "understock_hours": int(
                (
                    metrics["decision"]
                    == "UNDERSTOCK"
                ).sum()
            ),

            "overstock_hours": int(
                (
                    metrics["decision"]
                    == "OVERSTOCK"
                ).sum()
            ),

            "ok_hours": int(
                (
                    metrics["decision"]
                    == "OK"
                ).sum()
            ),

            "total_lost_revenue": round(
                metrics["lost_revenue"].sum(),
                2
            ),

            "total_holding_cost": round(
                metrics["holding_cost"].sum(),
                2
            ),

            "total_truck_cost": round(
                total_truck_cost,
                2
            ),

            "total_net_cost": round(
                metrics["net_operational_cost"].sum()
                + total_truck_cost,
                2
            )
        })

    return (
        pd.DataFrame(rows)
        .sort_values("total_net_cost")
        .reset_index(drop=True)
    )

from typing import Literal, cast

InsightStatus = Literal["checked", "inspection", "pending"]

INSIGHT_STATUS_VALUES: set[InsightStatus] = {
    "checked",
    "inspection",
    "pending",
}


def check_insight_status(value: str) -> InsightStatus:
    if value in INSIGHT_STATUS_VALUES:
        return cast(InsightStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSIGHT_STATUS_VALUES!r}"
    )

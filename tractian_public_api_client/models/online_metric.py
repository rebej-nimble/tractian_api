from typing import Literal, cast

OnlineMetric = Literal["temperature", "totalUptime", "velRms"]

ONLINE_METRIC_VALUES: set[OnlineMetric] = {
    "temperature",
    "totalUptime",
    "velRms",
}


def check_online_metric(value: str) -> OnlineMetric:
    if value in ONLINE_METRIC_VALUES:
        return cast(OnlineMetric, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ONLINE_METRIC_VALUES!r}"
    )

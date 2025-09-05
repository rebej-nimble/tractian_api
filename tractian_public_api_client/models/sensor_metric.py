from typing import Literal, cast

SensorMetric = Literal["ampereHour", "binary", "humidity"]

SENSOR_METRIC_VALUES: set[SensorMetric] = {
    "ampereHour",
    "binary",
    "humidity",
}


def check_sensor_metric(value: str) -> SensorMetric:
    if value in SENSOR_METRIC_VALUES:
        return cast(SensorMetric, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SENSOR_METRIC_VALUES!r}"
    )

from typing import Literal, cast

FrequencyType = Literal["day", "hour", "minute", "month", "week", "year"]

FREQUENCY_TYPE_VALUES: set[FrequencyType] = {
    "day",
    "hour",
    "minute",
    "month",
    "week",
    "year",
}


def check_frequency_type(value: str) -> FrequencyType:
    if value in FREQUENCY_TYPE_VALUES:
        return cast(FrequencyType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FREQUENCY_TYPE_VALUES!r}"
    )

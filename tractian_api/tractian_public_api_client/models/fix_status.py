from typing import Literal, cast

FixStatus = Literal["fixed", "notFixed"]

FIX_STATUS_VALUES: set[FixStatus] = {
    "fixed",
    "notFixed",
}


def check_fix_status(value: str) -> FixStatus:
    if value in FIX_STATUS_VALUES:
        return cast(FixStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FIX_STATUS_VALUES!r}"
    )

from typing import Literal, cast

InspectionStatus = Literal["closed", "inProgress", "onHold", "open"]

INSPECTION_STATUS_VALUES: set[InspectionStatus] = {
    "closed",
    "inProgress",
    "onHold",
    "open",
}


def check_inspection_status(value: str) -> InspectionStatus:
    if value in INSPECTION_STATUS_VALUES:
        return cast(InspectionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSPECTION_STATUS_VALUES!r}"
    )

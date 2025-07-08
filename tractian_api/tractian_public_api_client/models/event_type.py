from typing import Literal, cast

EventType = Literal[
    "functionalFailure",
    "plannedStop",
    "potentialFailure",
    "powerOutage",
    "powerRestored",
    "powerSupplyProblem",
    "processAdjustment",
    "totalFailure",
    "unplannedOperation",
    "unplannedStop",
]

EVENT_TYPE_VALUES: set[EventType] = {
    "functionalFailure",
    "plannedStop",
    "potentialFailure",
    "powerOutage",
    "powerRestored",
    "powerSupplyProblem",
    "processAdjustment",
    "totalFailure",
    "unplannedOperation",
    "unplannedStop",
}


def check_event_type(value: str) -> EventType:
    if value in EVENT_TYPE_VALUES:
        return cast(EventType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EVENT_TYPE_VALUES!r}"
    )

from typing import Literal, cast

ItemReservationStatusEnum = Literal[
    "canceled", "pendingReturn", "reserved", "returned", "withdrawn"
]

ITEM_RESERVATION_STATUS_ENUM_VALUES: set[ItemReservationStatusEnum] = {
    "canceled",
    "pendingReturn",
    "reserved",
    "returned",
    "withdrawn",
}


def check_item_reservation_status_enum(value: str) -> ItemReservationStatusEnum:
    if value in ITEM_RESERVATION_STATUS_ENUM_VALUES:
        return cast(ItemReservationStatusEnum, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ITEM_RESERVATION_STATUS_ENUM_VALUES!r}"
    )

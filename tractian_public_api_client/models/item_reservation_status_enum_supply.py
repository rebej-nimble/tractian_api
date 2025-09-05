from typing import Literal, cast

ItemReservationStatusEnumSupply = Literal[
    "canceled", "pendingReturn", "reserved", "returned", "withdrawn"
]

ITEM_RESERVATION_STATUS_ENUM_SUPPLY_VALUES: set[ItemReservationStatusEnumSupply] = {
    "canceled",
    "pendingReturn",
    "reserved",
    "returned",
    "withdrawn",
}


def check_item_reservation_status_enum_supply(
    value: str,
) -> ItemReservationStatusEnumSupply:
    if value in ITEM_RESERVATION_STATUS_ENUM_SUPPLY_VALUES:
        return cast(ItemReservationStatusEnumSupply, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ITEM_RESERVATION_STATUS_ENUM_SUPPLY_VALUES!r}"
    )

from typing import Literal, cast

InventoryAdjustmentTypeEnum = Literal["entry", "withdrawn"]

INVENTORY_ADJUSTMENT_TYPE_ENUM_VALUES: set[InventoryAdjustmentTypeEnum] = {
    "entry",
    "withdrawn",
}


def check_inventory_adjustment_type_enum(value: str) -> InventoryAdjustmentTypeEnum:
    if value in INVENTORY_ADJUSTMENT_TYPE_ENUM_VALUES:
        return cast(InventoryAdjustmentTypeEnum, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVENTORY_ADJUSTMENT_TYPE_ENUM_VALUES!r}"
    )

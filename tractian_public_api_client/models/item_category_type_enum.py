from typing import Literal, cast

ItemCategoryTypeEnum = Literal["consumable", "nonConsumable", "service"]

ITEM_CATEGORY_TYPE_ENUM_VALUES: set[ItemCategoryTypeEnum] = {
    "consumable",
    "nonConsumable",
    "service",
}


def check_item_category_type_enum(value: str) -> ItemCategoryTypeEnum:
    if value in ITEM_CATEGORY_TYPE_ENUM_VALUES:
        return cast(ItemCategoryTypeEnum, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ITEM_CATEGORY_TYPE_ENUM_VALUES!r}"
    )

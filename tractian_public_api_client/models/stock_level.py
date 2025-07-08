from typing import Literal, cast

StockLevel = Literal[
    "criticalStock",
    "maximumStock",
    "minimumStock",
    "noScaling",
    "regularStock",
    "reorderPoint",
    "withoutStock",
]

STOCK_LEVEL_VALUES: set[StockLevel] = {
    "criticalStock",
    "maximumStock",
    "minimumStock",
    "noScaling",
    "regularStock",
    "reorderPoint",
    "withoutStock",
}


def check_stock_level(value: str) -> StockLevel:
    if value in STOCK_LEVEL_VALUES:
        return cast(StockLevel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOCK_LEVEL_VALUES!r}"
    )

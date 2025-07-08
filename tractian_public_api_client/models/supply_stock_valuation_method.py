from typing import Literal, cast

SupplyStockValuationMethod = Literal["fefo", "fifo", "lifo"]

SUPPLY_STOCK_VALUATION_METHOD_VALUES: set[SupplyStockValuationMethod] = {
    "fefo",
    "fifo",
    "lifo",
}


def check_supply_stock_valuation_method(value: str) -> SupplyStockValuationMethod:
    if value in SUPPLY_STOCK_VALUATION_METHOD_VALUES:
        return cast(SupplyStockValuationMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLY_STOCK_VALUATION_METHOD_VALUES!r}"
    )

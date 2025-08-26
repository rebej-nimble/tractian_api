from typing import Literal, cast

ApiSupplyPurchaseOrderStatus = Literal[
    "canceled", "created", "entryRegistered", "partialEntry"
]

API_SUPPLY_PURCHASE_ORDER_STATUS_VALUES: set[ApiSupplyPurchaseOrderStatus] = {
    "canceled",
    "created",
    "entryRegistered",
    "partialEntry",
}


def check_api_supply_purchase_order_status(value: str) -> ApiSupplyPurchaseOrderStatus:
    if value in API_SUPPLY_PURCHASE_ORDER_STATUS_VALUES:
        return cast(ApiSupplyPurchaseOrderStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_SUPPLY_PURCHASE_ORDER_STATUS_VALUES!r}"
    )

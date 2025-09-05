from typing import Literal, cast

ApiSupplyTransferRequestItemStatus = Literal["completed", "inProgress", "requested"]

API_SUPPLY_TRANSFER_REQUEST_ITEM_STATUS_VALUES: set[
    ApiSupplyTransferRequestItemStatus
] = {
    "completed",
    "inProgress",
    "requested",
}


def check_api_supply_transfer_request_item_status(
    value: str,
) -> ApiSupplyTransferRequestItemStatus:
    if value in API_SUPPLY_TRANSFER_REQUEST_ITEM_STATUS_VALUES:
        return cast(ApiSupplyTransferRequestItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_SUPPLY_TRANSFER_REQUEST_ITEM_STATUS_VALUES!r}"
    )

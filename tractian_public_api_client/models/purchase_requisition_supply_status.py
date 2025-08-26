from typing import Literal, cast

PurchaseRequisitionSupplyStatus = Literal[
    "accepted", "canceled", "completed", "pending", "rejected"
]

PURCHASE_REQUISITION_SUPPLY_STATUS_VALUES: set[PurchaseRequisitionSupplyStatus] = {
    "accepted",
    "canceled",
    "completed",
    "pending",
    "rejected",
}


def check_purchase_requisition_supply_status(
    value: str,
) -> PurchaseRequisitionSupplyStatus:
    if value in PURCHASE_REQUISITION_SUPPLY_STATUS_VALUES:
        return cast(PurchaseRequisitionSupplyStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUISITION_SUPPLY_STATUS_VALUES!r}"
    )

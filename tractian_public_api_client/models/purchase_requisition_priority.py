from typing import Literal, cast

PurchaseRequisitionPriority = Literal["high", "low", "medium", "urgent"]

PURCHASE_REQUISITION_PRIORITY_VALUES: set[PurchaseRequisitionPriority] = {
    "high",
    "low",
    "medium",
    "urgent",
}


def check_purchase_requisition_priority(value: str) -> PurchaseRequisitionPriority:
    if value in PURCHASE_REQUISITION_PRIORITY_VALUES:
        return cast(PurchaseRequisitionPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUISITION_PRIORITY_VALUES!r}"
    )

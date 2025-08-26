from typing import Literal, cast

PurchaseRequisitionSupplyPriority = Literal["high", "low", "medium", "urgent"]

PURCHASE_REQUISITION_SUPPLY_PRIORITY_VALUES: set[PurchaseRequisitionSupplyPriority] = {
    "high",
    "low",
    "medium",
    "urgent",
}


def check_purchase_requisition_supply_priority(
    value: str,
) -> PurchaseRequisitionSupplyPriority:
    if value in PURCHASE_REQUISITION_SUPPLY_PRIORITY_VALUES:
        return cast(PurchaseRequisitionSupplyPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUISITION_SUPPLY_PRIORITY_VALUES!r}"
    )

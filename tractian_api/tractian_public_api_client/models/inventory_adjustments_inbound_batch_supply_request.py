from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryAdjustmentsInboundBatchSupplyRequest")


@_attrs_define
class InventoryAdjustmentsInboundBatchSupplyRequest:
    quantity: float
    inbound_batch_id: str

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        inbound_batch_id = self.inbound_batch_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
                "inboundBatchId": inbound_batch_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        inbound_batch_id = d.pop("inboundBatchId")

        inventory_adjustments_inbound_batch_supply_request = cls(
            quantity=quantity,
            inbound_batch_id=inbound_batch_id,
        )

        return inventory_adjustments_inbound_batch_supply_request

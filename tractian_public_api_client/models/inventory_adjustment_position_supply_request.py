from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryAdjustmentPositionSupplyRequest")


@_attrs_define
class InventoryAdjustmentPositionSupplyRequest:
    storage_id: str
    quantity: float

    def to_dict(self) -> dict[str, Any]:
        storage_id = self.storage_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "storageId": storage_id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage_id = d.pop("storageId")

        quantity = d.pop("quantity")

        inventory_adjustment_position_supply_request = cls(
            storage_id=storage_id,
            quantity=quantity,
        )

        return inventory_adjustment_position_supply_request

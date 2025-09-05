from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryAdjustmentUpdatedBalanceSupplyResponse")


@_attrs_define
class InventoryAdjustmentUpdatedBalanceSupplyResponse:
    stock_quantity: float
    available_quantity: float
    reserved_quantity: float

    def to_dict(self) -> dict[str, Any]:
        stock_quantity = self.stock_quantity

        available_quantity = self.available_quantity

        reserved_quantity = self.reserved_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stockQuantity": stock_quantity,
                "availableQuantity": available_quantity,
                "reservedQuantity": reserved_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stock_quantity = d.pop("stockQuantity")

        available_quantity = d.pop("availableQuantity")

        reserved_quantity = d.pop("reservedQuantity")

        inventory_adjustment_updated_balance_supply_response = cls(
            stock_quantity=stock_quantity,
            available_quantity=available_quantity,
            reserved_quantity=reserved_quantity,
        )

        return inventory_adjustment_updated_balance_supply_response

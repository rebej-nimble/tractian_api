from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryMotorRequestBatchAPI")


@_attrs_define
class InventoryMotorRequestBatchAPI:
    id: str
    """ Unique identifier of the batch. """
    name: str
    """ Name of the batch. """
    reserved_quantity: float
    """ Quantity reserved and not available for use. """
    stock_quantity: float
    """ Total quantity of stock in the batch. """
    available_quantity: float
    """ Quantity available for use after reservations. """
    unit_cost: float
    """ Unit cost of the items in this batch. """

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        reserved_quantity = self.reserved_quantity

        stock_quantity = self.stock_quantity

        available_quantity = self.available_quantity

        unit_cost = self.unit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "reservedQuantity": reserved_quantity,
                "stockQuantity": stock_quantity,
                "availableQuantity": available_quantity,
                "unitCost": unit_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        reserved_quantity = d.pop("reservedQuantity")

        stock_quantity = d.pop("stockQuantity")

        available_quantity = d.pop("availableQuantity")

        unit_cost = d.pop("unitCost")

        inventory_motor_request_batch_api = cls(
            id=id,
            name=name,
            reserved_quantity=reserved_quantity,
            stock_quantity=stock_quantity,
            available_quantity=available_quantity,
            unit_cost=unit_cost,
        )

        return inventory_motor_request_batch_api

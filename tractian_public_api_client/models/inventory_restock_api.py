from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InventoryRestockAPI")


@_attrs_define
class InventoryRestockAPI:
    value: float
    """ If used with the 'Restock Inventory Total' route, this represents the total updated quantity of the item. If
    used with the 'Restock Inventory' route, this represents an incoming or outgoing quantity (negative for
    outgoing). """

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        inventory_restock_api = cls(
            value=value,
        )

        return inventory_restock_api

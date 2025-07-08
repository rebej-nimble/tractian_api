from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryRestockBatchesAPI")


@_attrs_define
class InventoryRestockBatchesAPI:
    is_add_new_batch: bool
    """ Indicates whether a new batch is being added. """
    name: str
    """ Batch name. """
    value: float
    """ If used with the 'Restock Inventory Batches Total' route, this represents the total updated quantity for the
    batch. If used with the 'Restock Inventory Batches' route, this represents an incoming or outgoing quantity
    (negative for outgoing). """
    unit_cost: float
    """ Unit cost of the item. """
    id: Union[None, Unset, str] = UNSET
    """ Batch ID. Required if 'isAddNewBatch' is False. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_add_new_batch = self.is_add_new_batch

        name = self.name

        value = self.value

        unit_cost = self.unit_cost

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAddNewBatch": is_add_new_batch,
                "name": name,
                "value": value,
                "unitCost": unit_cost,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_add_new_batch = d.pop("isAddNewBatch")

        name = d.pop("name")

        value = d.pop("value")

        unit_cost = d.pop("unitCost")

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        inventory_restock_batches_api = cls(
            is_add_new_batch=is_add_new_batch,
            name=name,
            value=value,
            unit_cost=unit_cost,
            id=id,
        )

        inventory_restock_batches_api.additional_properties = d
        return inventory_restock_batches_api

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

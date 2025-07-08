from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkOrderOperationInventorySelectedBatch")


@_attrs_define
class WorkOrderOperationInventorySelectedBatch:
    id: str
    quantity: Union[None, Unset, float] = UNSET
    available_quantity: Union[None, Unset, float] = UNSET
    unit_cost: Union[None, Unset, float] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        available_quantity: Union[None, Unset, float]
        if isinstance(self.available_quantity, Unset):
            available_quantity = UNSET
        else:
            available_quantity = self.available_quantity

        unit_cost: Union[None, Unset, float]
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_available_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        available_quantity = _parse_available_quantity(
            d.pop("availableQuantity", UNSET)
        )

        def _parse_unit_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        work_order_operation_inventory_selected_batch = cls(
            id=id,
            quantity=quantity,
            available_quantity=available_quantity,
            unit_cost=unit_cost,
            name=name,
        )

        work_order_operation_inventory_selected_batch.additional_properties = d
        return work_order_operation_inventory_selected_batch

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

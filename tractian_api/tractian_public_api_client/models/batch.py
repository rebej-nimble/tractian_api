from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    id: str
    """ Unique identifier for the batch. """
    name: str
    """ Name of the batch. """
    reserved_quantity: Union[None, Unset, float] = UNSET
    """ Quantity reserved in this batch. """
    stock_quantity: Union[None, Unset, float] = UNSET
    """ Total stock quantity in this batch. """
    available_quantity: Union[None, Unset, float] = UNSET
    """ Quantity available in this batch after reservations. """
    unit_cost: Union[None, Unset, float] = UNSET
    """ Unit cost of the items in this batch. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        reserved_quantity: Union[None, Unset, float]
        if isinstance(self.reserved_quantity, Unset):
            reserved_quantity = UNSET
        else:
            reserved_quantity = self.reserved_quantity

        stock_quantity: Union[None, Unset, float]
        if isinstance(self.stock_quantity, Unset):
            stock_quantity = UNSET
        else:
            stock_quantity = self.stock_quantity

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if reserved_quantity is not UNSET:
            field_dict["reservedQuantity"] = reserved_quantity
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_reserved_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        reserved_quantity = _parse_reserved_quantity(d.pop("reservedQuantity", UNSET))

        def _parse_stock_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        stock_quantity = _parse_stock_quantity(d.pop("stockQuantity", UNSET))

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

        batch = cls(
            id=id,
            name=name,
            reserved_quantity=reserved_quantity,
            stock_quantity=stock_quantity,
            available_quantity=available_quantity,
            unit_cost=unit_cost,
        )

        batch.additional_properties = d
        return batch

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInventoryItemMotor")


@_attrs_define
class AssetInventoryItemMotor:
    id: str
    name: Union[None, Unset, str] = UNSET
    available_quantity: Union[None, Unset, float, int] = UNSET
    stock_quantity: Union[None, Unset, float, int] = UNSET
    minimum_quantity: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        available_quantity: Union[None, Unset, float, int]
        if isinstance(self.available_quantity, Unset):
            available_quantity = UNSET
        else:
            available_quantity = self.available_quantity

        stock_quantity: Union[None, Unset, float, int]
        if isinstance(self.stock_quantity, Unset):
            stock_quantity = UNSET
        else:
            stock_quantity = self.stock_quantity

        minimum_quantity: Union[None, Unset, int]
        if isinstance(self.minimum_quantity, Unset):
            minimum_quantity = UNSET
        else:
            minimum_quantity = self.minimum_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if minimum_quantity is not UNSET:
            field_dict["minimumQuantity"] = minimum_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_available_quantity(data: object) -> Union[None, Unset, float, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, int], data)

        available_quantity = _parse_available_quantity(
            d.pop("availableQuantity", UNSET)
        )

        def _parse_stock_quantity(data: object) -> Union[None, Unset, float, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, int], data)

        stock_quantity = _parse_stock_quantity(d.pop("stockQuantity", UNSET))

        def _parse_minimum_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        minimum_quantity = _parse_minimum_quantity(d.pop("minimumQuantity", UNSET))

        asset_inventory_item_motor = cls(
            id=id,
            name=name,
            available_quantity=available_quantity,
            stock_quantity=stock_quantity,
            minimum_quantity=minimum_quantity,
        )

        asset_inventory_item_motor.additional_properties = d
        return asset_inventory_item_motor

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

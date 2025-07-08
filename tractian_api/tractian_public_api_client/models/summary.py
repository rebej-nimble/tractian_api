from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Summary")


@_attrs_define
class Summary:
    storage_locations: Union[None, Unset, list[str]] = UNSET
    available_quantity: Union[None, Unset, float] = 0.0
    stock_level: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_locations: Union[None, Unset, list[str]]
        if isinstance(self.storage_locations, Unset):
            storage_locations = UNSET
        elif isinstance(self.storage_locations, list):
            storage_locations = self.storage_locations

        else:
            storage_locations = self.storage_locations

        available_quantity: Union[None, Unset, float]
        if isinstance(self.available_quantity, Unset):
            available_quantity = UNSET
        else:
            available_quantity = self.available_quantity

        stock_level: Union[None, Unset, str]
        if isinstance(self.stock_level, Unset):
            stock_level = UNSET
        else:
            stock_level = self.stock_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_locations is not UNSET:
            field_dict["storageLocations"] = storage_locations
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if stock_level is not UNSET:
            field_dict["stockLevel"] = stock_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_storage_locations(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_locations_type_0 = cast(list[str], data)

                return storage_locations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        storage_locations = _parse_storage_locations(d.pop("storageLocations", UNSET))

        def _parse_available_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        available_quantity = _parse_available_quantity(
            d.pop("availableQuantity", UNSET)
        )

        def _parse_stock_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stock_level = _parse_stock_level(d.pop("stockLevel", UNSET))

        summary = cls(
            storage_locations=storage_locations,
            available_quantity=available_quantity,
            stock_level=stock_level,
        )

        summary.additional_properties = d
        return summary

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

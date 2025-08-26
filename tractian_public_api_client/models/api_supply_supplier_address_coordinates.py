from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplySupplierAddressCoordinates")


@_attrs_define
class ApiSupplySupplierAddressCoordinates:
    lng: Union[None, Unset, float] = UNSET
    """ Longitude of the supplier address """
    lat: Union[None, Unset, float] = UNSET
    """ Latitude of the supplier address """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lng: Union[None, Unset, float]
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        lat: Union[None, Unset, float]
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lng is not UNSET:
            field_dict["lng"] = lng
        if lat is not UNSET:
            field_dict["lat"] = lat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lng(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lng = _parse_lng(d.pop("lng", UNSET))

        def _parse_lat(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lat = _parse_lat(d.pop("lat", UNSET))

        api_supply_supplier_address_coordinates = cls(
            lng=lng,
            lat=lat,
        )

        api_supply_supplier_address_coordinates.additional_properties = d
        return api_supply_supplier_address_coordinates

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

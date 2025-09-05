from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.code_type import CodeType, check_code_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyStorageLocationCodeRequest")


@_attrs_define
class ApiSupplyStorageLocationCodeRequest:
    value: Union[None, Unset, str] = UNSET
    """ Value of the storage location code """
    type_: Union[CodeType, None, Unset] = UNSET
    """ Type of the storage location code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, str):
            type_ = self.type_
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_type_(data: object) -> Union[CodeType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = check_code_type(data)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CodeType, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        api_supply_storage_location_code_request = cls(
            value=value,
            type_=type_,
        )

        api_supply_storage_location_code_request.additional_properties = d
        return api_supply_storage_location_code_request

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

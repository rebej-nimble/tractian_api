from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.frequency_type import FrequencyType, check_frequency_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="FrequencyModelRequest")


@_attrs_define
class FrequencyModelRequest:
    type_: Union[FrequencyType, None, Unset] = UNSET
    """ Type of frequency schedule for metric measurement """
    value: Union[None, Unset, int, str] = UNSET
    """ Numeric value for the frequency interval """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, str):
            type_ = self.type_
        else:
            type_ = self.type_

        value: Union[None, Unset, int, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> Union[FrequencyType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = check_frequency_type(data)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FrequencyType, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        frequency_model_request = cls(
            type_=type_,
            value=value,
        )

        frequency_model_request.additional_properties = d
        return frequency_model_request

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

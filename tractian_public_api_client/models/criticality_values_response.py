from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CriticalityValuesResponse")


@_attrs_define
class CriticalityValuesResponse:
    mild: Union[None, Unset, float] = UNSET
    moderate: Union[None, Unset, float] = UNSET
    severe: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mild: Union[None, Unset, float]
        if isinstance(self.mild, Unset):
            mild = UNSET
        else:
            mild = self.mild

        moderate: Union[None, Unset, float]
        if isinstance(self.moderate, Unset):
            moderate = UNSET
        else:
            moderate = self.moderate

        severe: Union[None, Unset, float]
        if isinstance(self.severe, Unset):
            severe = UNSET
        else:
            severe = self.severe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mild is not UNSET:
            field_dict["mild"] = mild
        if moderate is not UNSET:
            field_dict["moderate"] = moderate
        if severe is not UNSET:
            field_dict["severe"] = severe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mild(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        mild = _parse_mild(d.pop("mild", UNSET))

        def _parse_moderate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        moderate = _parse_moderate(d.pop("moderate", UNSET))

        def _parse_severe(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        severe = _parse_severe(d.pop("severe", UNSET))

        criticality_values_response = cls(
            mild=mild,
            moderate=moderate,
            severe=severe,
        )

        criticality_values_response.additional_properties = d
        return criticality_values_response

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

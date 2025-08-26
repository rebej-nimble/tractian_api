from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criticality_values_response import CriticalityValuesResponse


T = TypeVar("T", bound="HeadValuesResponse")


@_attrs_define
class HeadValuesResponse:
    behavior: Union[None, Unset, bool] = UNSET
    criticality: Union[None, Unset, str] = UNSET
    criticality_values: Union["CriticalityValuesResponse", None, Unset] = UNSET
    max_: Union[None, Unset, float] = UNSET
    min_: Union[None, Unset, float] = UNSET
    user_threshold: Union[None, Unset, bool] = UNSET
    value: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.criticality_values_response import CriticalityValuesResponse

        behavior: Union[None, Unset, bool]
        if isinstance(self.behavior, Unset):
            behavior = UNSET
        else:
            behavior = self.behavior

        criticality: Union[None, Unset, str]
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        else:
            criticality = self.criticality

        criticality_values: Union[None, Unset, dict[str, Any]]
        if isinstance(self.criticality_values, Unset):
            criticality_values = UNSET
        elif isinstance(self.criticality_values, CriticalityValuesResponse):
            criticality_values = self.criticality_values.to_dict()
        else:
            criticality_values = self.criticality_values

        max_: Union[None, Unset, float]
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: Union[None, Unset, float]
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        user_threshold: Union[None, Unset, bool]
        if isinstance(self.user_threshold, Unset):
            user_threshold = UNSET
        else:
            user_threshold = self.user_threshold

        value: Union[None, Unset, float]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if behavior is not UNSET:
            field_dict["behavior"] = behavior
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if criticality_values is not UNSET:
            field_dict["criticalityValues"] = criticality_values
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if user_threshold is not UNSET:
            field_dict["userThreshold"] = user_threshold
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criticality_values_response import CriticalityValuesResponse

        d = dict(src_dict)

        def _parse_behavior(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        behavior = _parse_behavior(d.pop("behavior", UNSET))

        def _parse_criticality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_criticality_values(
            data: object,
        ) -> Union["CriticalityValuesResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                criticality_values_type_0 = CriticalityValuesResponse.from_dict(data)

                return criticality_values_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CriticalityValuesResponse", None, Unset], data)

        criticality_values = _parse_criticality_values(
            d.pop("criticalityValues", UNSET)
        )

        def _parse_max_(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_min_(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_user_threshold(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        user_threshold = _parse_user_threshold(d.pop("userThreshold", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        value = _parse_value(d.pop("value", UNSET))

        head_values_response = cls(
            behavior=behavior,
            criticality=criticality,
            criticality_values=criticality_values,
            max_=max_,
            min_=min_,
            user_threshold=user_threshold,
            value=value,
        )

        head_values_response.additional_properties = d
        return head_values_response

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

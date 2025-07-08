from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedRpmSampleData")


@_attrs_define
class SimplifiedRpmSampleData:
    id: Union[Unset, list[str]] = UNSET
    """ Sample ID (UUID). """
    rpm: Union[Unset, list[Union[None, float]]] = UNSET
    """ RPM data. """
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Sample date in ISO 8601 format. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id

        rpm: Union[Unset, list[Union[None, float]]] = UNSET
        if not isinstance(self.rpm, Unset):
            rpm = []
            for rpm_item_data in self.rpm:
                rpm_item: Union[None, float]
                rpm_item = rpm_item_data
                rpm.append(rpm_item)

        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if rpm is not UNSET:
            field_dict["rpm"] = rpm
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = cast(list[str], d.pop("id", UNSET))

        rpm = []
        _rpm = d.pop("rpm", UNSET)
        for rpm_item_data in _rpm or []:

            def _parse_rpm_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            rpm_item = _parse_rpm_item(rpm_item_data)

            rpm.append(rpm_item)

        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        simplified_rpm_sample_data = cls(
            id=id,
            rpm=rpm,
            sampled_at=sampled_at,
        )

        simplified_rpm_sample_data.additional_properties = d
        return simplified_rpm_sample_data

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyStorageLocationDisabled")


@_attrs_define
class ApiSupplyStorageLocationDisabled:
    value: Union[Unset, bool] = False
    """ Indicates whether the storage location has been disabled """
    reason: Union[None, Unset, str] = UNSET
    """ Reason for disabling the storage location """
    disabled_at: Union[None, Unset, str] = UNSET
    """ The date and time when the storage location was disabled """
    disabled_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who disabled the storage location """
    enabled_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who enabled the storage location """
    enabled_at: Union[None, Unset, str] = UNSET
    """ The date and time when the storage location was enabled """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        disabled_at: Union[None, Unset, str]
        if isinstance(self.disabled_at, Unset):
            disabled_at = UNSET
        else:
            disabled_at = self.disabled_at

        disabled_by_user_id: Union[None, Unset, str]
        if isinstance(self.disabled_by_user_id, Unset):
            disabled_by_user_id = UNSET
        else:
            disabled_by_user_id = self.disabled_by_user_id

        enabled_by_user_id: Union[None, Unset, str]
        if isinstance(self.enabled_by_user_id, Unset):
            enabled_by_user_id = UNSET
        else:
            enabled_by_user_id = self.enabled_by_user_id

        enabled_at: Union[None, Unset, str]
        if isinstance(self.enabled_at, Unset):
            enabled_at = UNSET
        else:
            enabled_at = self.enabled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if reason is not UNSET:
            field_dict["reason"] = reason
        if disabled_at is not UNSET:
            field_dict["disabledAt"] = disabled_at
        if disabled_by_user_id is not UNSET:
            field_dict["disabledByUserId"] = disabled_by_user_id
        if enabled_by_user_id is not UNSET:
            field_dict["enabledByUserId"] = enabled_by_user_id
        if enabled_at is not UNSET:
            field_dict["enabledAt"] = enabled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_disabled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disabled_at = _parse_disabled_at(d.pop("disabledAt", UNSET))

        def _parse_disabled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disabled_by_user_id = _parse_disabled_by_user_id(
            d.pop("disabledByUserId", UNSET)
        )

        def _parse_enabled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        enabled_by_user_id = _parse_enabled_by_user_id(d.pop("enabledByUserId", UNSET))

        def _parse_enabled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        enabled_at = _parse_enabled_at(d.pop("enabledAt", UNSET))

        api_supply_storage_location_disabled = cls(
            value=value,
            reason=reason,
            disabled_at=disabled_at,
            disabled_by_user_id=disabled_by_user_id,
            enabled_by_user_id=enabled_by_user_id,
            enabled_at=enabled_at,
        )

        api_supply_storage_location_disabled.additional_properties = d
        return api_supply_storage_location_disabled

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

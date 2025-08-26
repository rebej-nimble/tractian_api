from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplySupplierDeleted")


@_attrs_define
class ApiSupplySupplierDeleted:
    value: Union[Unset, bool] = False
    """ Indicates whether the supplier has been deleted """
    reason: Union[None, Unset, str] = UNSET
    """ Reason for deleting the supplier """
    deleted_at: Union[None, Unset, str] = UNSET
    """ The date and time when the supplier was deleted """
    deleted_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who deleted the supplier """
    restored_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who restored the supplier """
    restored_at: Union[None, Unset, str] = UNSET
    """ The date and time when the supplier was restored """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        deleted_by_user_id: Union[None, Unset, str]
        if isinstance(self.deleted_by_user_id, Unset):
            deleted_by_user_id = UNSET
        else:
            deleted_by_user_id = self.deleted_by_user_id

        restored_by_user_id: Union[None, Unset, str]
        if isinstance(self.restored_by_user_id, Unset):
            restored_by_user_id = UNSET
        else:
            restored_by_user_id = self.restored_by_user_id

        restored_at: Union[None, Unset, str]
        if isinstance(self.restored_at, Unset):
            restored_at = UNSET
        else:
            restored_at = self.restored_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if reason is not UNSET:
            field_dict["reason"] = reason
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by_user_id is not UNSET:
            field_dict["deletedByUserId"] = deleted_by_user_id
        if restored_by_user_id is not UNSET:
            field_dict["restoredByUserId"] = restored_by_user_id
        if restored_at is not UNSET:
            field_dict["restoredAt"] = restored_at

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

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))

        def _parse_deleted_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_by_user_id = _parse_deleted_by_user_id(d.pop("deletedByUserId", UNSET))

        def _parse_restored_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        restored_by_user_id = _parse_restored_by_user_id(
            d.pop("restoredByUserId", UNSET)
        )

        def _parse_restored_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        restored_at = _parse_restored_at(d.pop("restoredAt", UNSET))

        api_supply_supplier_deleted = cls(
            value=value,
            reason=reason,
            deleted_at=deleted_at,
            deleted_by_user_id=deleted_by_user_id,
            restored_by_user_id=restored_by_user_id,
            restored_at=restored_at,
        )

        api_supply_supplier_deleted.additional_properties = d
        return api_supply_supplier_deleted

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

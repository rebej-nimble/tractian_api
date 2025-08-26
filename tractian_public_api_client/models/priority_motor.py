from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.priority_motor_deleted import PriorityMotorDeleted
    from ..models.priority_motor_disabled import PriorityMotorDisabled


T = TypeVar("T", bound="PriorityMotor")


@_attrs_define
class PriorityMotor:
    id: str
    name: str
    company_id: str
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    disabled: Union[Unset, "PriorityMotorDisabled"] = UNSET
    deleted: Union[Unset, "PriorityMotorDeleted"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id = self.company_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        disabled: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.disabled, Unset):
            disabled = self.disabled.to_dict()

        deleted: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "companyId": company_id,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.priority_motor_deleted import PriorityMotorDeleted
        from ..models.priority_motor_disabled import PriorityMotorDisabled

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("companyId")

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        _disabled = d.pop("disabled", UNSET)
        disabled: Union[Unset, PriorityMotorDisabled]
        if isinstance(_disabled, Unset):
            disabled = UNSET
        else:
            disabled = PriorityMotorDisabled.from_dict(_disabled)

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, PriorityMotorDeleted]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = PriorityMotorDeleted.from_dict(_deleted)

        priority_motor = cls(
            id=id,
            name=name,
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            disabled=disabled,
            deleted=deleted,
        )

        priority_motor.additional_properties = d
        return priority_motor

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

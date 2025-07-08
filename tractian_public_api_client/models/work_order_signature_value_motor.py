from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkOrderSignatureValueMotor")


@_attrs_define
class WorkOrderSignatureValueMotor:
    date: Union[None, Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        work_order_signature_value_motor = cls(
            date=date,
            user_id=user_id,
        )

        work_order_signature_value_motor.additional_properties = d
        return work_order_signature_value_motor

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

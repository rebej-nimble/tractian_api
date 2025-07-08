from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feedback_request_user_motor import FeedbackRequestUserMotor


T = TypeVar("T", bound="FeedbackRequestsMotor")


@_attrs_define
class FeedbackRequestsMotor:
    reason: Union[None, Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, str] = UNSET
    user: Union["FeedbackRequestUserMotor", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.feedback_request_user_motor import FeedbackRequestUserMotor

        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        user: Union[None, Unset, dict[str, Any]]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, FeedbackRequestUserMotor):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if date is not UNSET:
            field_dict["date"] = date
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_request_user_motor import FeedbackRequestUserMotor

        d = dict(src_dict)

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_user(data: object) -> Union["FeedbackRequestUserMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = FeedbackRequestUserMotor.from_dict(data)

                return user_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackRequestUserMotor", None, Unset], data)

        user = _parse_user(d.pop("user", UNSET))

        feedback_requests_motor = cls(
            reason=reason,
            user_id=user_id,
            date=date,
            user=user,
        )

        feedback_requests_motor.additional_properties = d
        return feedback_requests_motor

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

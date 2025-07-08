from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentsMotor")


@_attrs_define
class CommentsMotor:
    company_id: str
    content: str
    attachments: Union[None, Unset, str] = UNSET
    audio_messages: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        content = self.content

        attachments: Union[None, Unset, str]
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        else:
            attachments = self.attachments

        audio_messages: Union[None, Unset, str]
        if isinstance(self.audio_messages, Unset):
            audio_messages = UNSET
        else:
            audio_messages = self.audio_messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "content": content,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if audio_messages is not UNSET:
            field_dict["audioMessages"] = audio_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        content = d.pop("content")

        def _parse_attachments(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_audio_messages(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_messages = _parse_audio_messages(d.pop("audioMessages", UNSET))

        comments_motor = cls(
            company_id=company_id,
            content=content,
            attachments=attachments,
            audio_messages=audio_messages,
        )

        comments_motor.additional_properties = d
        return comments_motor

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetAttachmentMotor")


@_attrs_define
class AssetAttachmentMotor:
    url: str
    filename: str
    content_type: str
    uploaded_by: str
    key: str
    size: Union[None, Unset, int] = UNSET
    internal: Union[None, Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        filename = self.filename

        content_type = self.content_type

        uploaded_by = self.uploaded_by

        key = self.key

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        internal: Union[None, Unset, bool]
        if isinstance(self.internal, Unset):
            internal = UNSET
        else:
            internal = self.internal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "filename": filename,
                "contentType": content_type,
                "uploadedBy": uploaded_by,
                "key": key,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if internal is not UNSET:
            field_dict["internal"] = internal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        filename = d.pop("filename")

        content_type = d.pop("contentType")

        uploaded_by = d.pop("uploadedBy")

        key = d.pop("key")

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_internal(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        internal = _parse_internal(d.pop("internal", UNSET))

        asset_attachment_motor = cls(
            url=url,
            filename=filename,
            content_type=content_type,
            uploaded_by=uploaded_by,
            key=key,
            size=size,
            internal=internal,
        )

        asset_attachment_motor.additional_properties = d
        return asset_attachment_motor

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

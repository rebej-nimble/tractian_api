from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkOrderMotorAttachment")


@_attrs_define
class WorkOrderMotorAttachment:
    id: str
    filename: str
    content_type: str
    url: str
    size: int
    uploaded_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename = self.filename

        content_type = self.content_type

        url = self.url

        size = self.size

        uploaded_by = self.uploaded_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "contentType": content_type,
                "url": url,
                "size": size,
                "uploadedBy": uploaded_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        filename = d.pop("filename")

        content_type = d.pop("contentType")

        url = d.pop("url")

        size = d.pop("size")

        uploaded_by = d.pop("uploadedBy")

        work_order_motor_attachment = cls(
            id=id,
            filename=filename,
            content_type=content_type,
            url=url,
            size=size,
            uploaded_by=uploaded_by,
        )

        work_order_motor_attachment.additional_properties = d
        return work_order_motor_attachment

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

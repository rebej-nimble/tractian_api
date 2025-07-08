from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetImageMotor")


@_attrs_define
class AssetImageMotor:
    id: str
    uploaded_by: str
    company_id: str
    filename: str
    content_type: str
    size: int
    url: str
    key: str
    created_at: str
    updated_at: str
    conversion: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uploaded_by = self.uploaded_by

        company_id = self.company_id

        filename = self.filename

        content_type = self.content_type

        size = self.size

        url = self.url

        key = self.key

        created_at = self.created_at

        updated_at = self.updated_at

        conversion: Union[None, Unset, str]
        if isinstance(self.conversion, Unset):
            conversion = UNSET
        else:
            conversion = self.conversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uploadedBy": uploaded_by,
                "companyId": company_id,
                "filename": filename,
                "contentType": content_type,
                "size": size,
                "url": url,
                "key": key,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if conversion is not UNSET:
            field_dict["conversion"] = conversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        uploaded_by = d.pop("uploadedBy")

        company_id = d.pop("companyId")

        filename = d.pop("filename")

        content_type = d.pop("contentType")

        size = d.pop("size")

        url = d.pop("url")

        key = d.pop("key")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_conversion(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conversion = _parse_conversion(d.pop("conversion", UNSET))

        asset_image_motor = cls(
            id=id,
            uploaded_by=uploaded_by,
            company_id=company_id,
            filename=filename,
            content_type=content_type,
            size=size,
            url=url,
            key=key,
            created_at=created_at,
            updated_at=updated_at,
            conversion=conversion,
        )

        asset_image_motor.additional_properties = d
        return asset_image_motor

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

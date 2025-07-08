from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateRequestMotorAttachment")


@_attrs_define
class TemplateRequestMotorAttachment:
    filename: str
    content_type: str
    url: str
    size: int
    company_id: str
    uploaded_by: str
    key: str
    id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    internal: Union[None, Unset, bool] = UNSET
    uploaded: Union[None, Unset, bool] = UNSET
    favorite: Union[None, Unset, bool] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    upload_url: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        content_type = self.content_type

        url = self.url

        size = self.size

        company_id = self.company_id

        uploaded_by = self.uploaded_by

        key = self.key

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        internal: Union[None, Unset, bool]
        if isinstance(self.internal, Unset):
            internal = UNSET
        else:
            internal = self.internal

        uploaded: Union[None, Unset, bool]
        if isinstance(self.uploaded, Unset):
            uploaded = UNSET
        else:
            uploaded = self.uploaded

        favorite: Union[None, Unset, bool]
        if isinstance(self.favorite, Unset):
            favorite = UNSET
        else:
            favorite = self.favorite

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        upload_url: Union[None, Unset, str]
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "contentType": content_type,
                "url": url,
                "size": size,
                "companyId": company_id,
                "uploadedBy": uploaded_by,
                "key": key,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if internal is not UNSET:
            field_dict["internal"] = internal
        if uploaded is not UNSET:
            field_dict["uploaded"] = uploaded
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if upload_url is not UNSET:
            field_dict["uploadURL"] = upload_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        content_type = d.pop("contentType")

        url = d.pop("url")

        size = d.pop("size")

        company_id = d.pop("companyId")

        uploaded_by = d.pop("uploadedBy")

        key = d.pop("key")

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_internal(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        internal = _parse_internal(d.pop("internal", UNSET))

        def _parse_uploaded(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        uploaded = _parse_uploaded(d.pop("uploaded", UNSET))

        def _parse_favorite(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        favorite = _parse_favorite(d.pop("favorite", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_upload_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        upload_url = _parse_upload_url(d.pop("uploadURL", UNSET))

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

        template_request_motor_attachment = cls(
            filename=filename,
            content_type=content_type,
            url=url,
            size=size,
            company_id=company_id,
            uploaded_by=uploaded_by,
            key=key,
            id=id,
            external_id=external_id,
            internal=internal,
            uploaded=uploaded,
            favorite=favorite,
            asset_id=asset_id,
            upload_url=upload_url,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
        )

        template_request_motor_attachment.additional_properties = d
        return template_request_motor_attachment

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

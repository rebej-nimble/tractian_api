from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_supplier_deleted import ApiSupplySupplierDeleted


T = TypeVar("T", bound="ApiSupplySupplierImage")


@_attrs_define
class ApiSupplySupplierImage:
    id: str
    """ Unique identifier of the image """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time when the image was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time when the image was last updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who created the image """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who last updated the image """
    deleted: Union["ApiSupplySupplierDeleted", None, Unset] = UNSET
    """ Deletion status information for the image """
    company_id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the company the image belongs to """
    external_id: Union[None, Unset, str] = UNSET
    """ External identifier for the image """
    upload_url: Union[None, Unset, str] = UNSET
    """ Upload URL for the image """
    conversion: Union[None, Unset, str] = UNSET
    """ Conversion information for the image """
    internal: Union[None, Unset, bool] = UNSET
    """ Whether the image is internal """
    uploaded: Union[None, Unset, bool] = UNSET
    """ Whether the image has been uploaded """
    favorite: Union[None, Unset, bool] = UNSET
    """ Whether the image is marked as favorite """
    key: Union[None, Unset, str] = UNSET
    """ Key identifier for the image """
    url: Union[None, Unset, str] = UNSET
    """ URL to access the image """
    size: Union[None, Unset, int] = UNSET
    """ Size of the image in bytes """
    content_type: Union[None, Unset, str] = UNSET
    """ Content type of the image """
    filename: Union[None, Unset, str] = UNSET
    """ Filename of the image """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_supply_supplier_deleted import ApiSupplySupplierDeleted

        id = self.id

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

        deleted: Union[None, Unset, dict[str, Any]]
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, ApiSupplySupplierDeleted):
            deleted = self.deleted.to_dict()
        else:
            deleted = self.deleted

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        upload_url: Union[None, Unset, str]
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url

        conversion: Union[None, Unset, str]
        if isinstance(self.conversion, Unset):
            conversion = UNSET
        else:
            conversion = self.conversion

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

        key: Union[None, Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        content_type: Union[None, Unset, str]
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        filename: Union[None, Unset, str]
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if upload_url is not UNSET:
            field_dict["uploadURL"] = upload_url
        if conversion is not UNSET:
            field_dict["conversion"] = conversion
        if internal is not UNSET:
            field_dict["internal"] = internal
        if uploaded is not UNSET:
            field_dict["uploaded"] = uploaded
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if key is not UNSET:
            field_dict["key"] = key
        if url is not UNSET:
            field_dict["url"] = url
        if size is not UNSET:
            field_dict["size"] = size
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_supplier_deleted import ApiSupplySupplierDeleted

        d = dict(src_dict)
        id = d.pop("id")

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

        def _parse_deleted(
            data: object,
        ) -> Union["ApiSupplySupplierDeleted", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_type_0 = ApiSupplySupplierDeleted.from_dict(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplySupplierDeleted", None, Unset], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_upload_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        upload_url = _parse_upload_url(d.pop("uploadURL", UNSET))

        def _parse_conversion(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conversion = _parse_conversion(d.pop("conversion", UNSET))

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

        def _parse_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_content_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))

        def _parse_filename(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        filename = _parse_filename(d.pop("filename", UNSET))

        api_supply_supplier_image = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            deleted=deleted,
            company_id=company_id,
            external_id=external_id,
            upload_url=upload_url,
            conversion=conversion,
            internal=internal,
            uploaded=uploaded,
            favorite=favorite,
            key=key,
            url=url,
            size=size,
            content_type=content_type,
            filename=filename,
        )

        api_supply_supplier_image.additional_properties = d
        return api_supply_supplier_image

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

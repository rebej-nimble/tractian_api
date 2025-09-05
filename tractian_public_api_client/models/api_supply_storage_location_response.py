from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_attachment import ApiSupplyAttachment
    from ..models.api_supply_image import ApiSupplyImage
    from ..models.api_supply_storage_location_code_response import (
        ApiSupplyStorageLocationCodeResponse,
    )
    from ..models.api_supply_storage_location_deleted import (
        ApiSupplyStorageLocationDeleted,
    )
    from ..models.api_supply_storage_location_disabled import (
        ApiSupplyStorageLocationDisabled,
    )


T = TypeVar("T", bound="ApiSupplyStorageLocationResponse")


@_attrs_define
class ApiSupplyStorageLocationResponse:
    id: str
    """ Unique identifier of the storage location """
    company_id: str
    """ The id of the company """
    name: str
    """ Name of the storage location """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time when the storage location was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time when the storage location was last updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who created the storage location """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who last updated the storage location """
    deleted: Union["ApiSupplyStorageLocationDeleted", None, Unset] = UNSET
    """ Deletion status information for the storage location """
    disabled: Union["ApiSupplyStorageLocationDisabled", None, Unset] = UNSET
    """ Disabled status information for the storage location """
    identifier_code: Union[None, Unset, str] = UNSET
    """ The identifier code of the storage location """
    description: Union[None, Unset, str] = UNSET
    """ Description of the storage location """
    parent_id: Union[None, Unset, str] = UNSET
    """ The id of the parent storage location """
    location_id: Union[None, Unset, str] = UNSET
    """ The id of the location """
    address: Union[None, Unset, str] = UNSET
    """ The address of the storage location """
    code: Union["ApiSupplyStorageLocationCodeResponse", None, Unset] = UNSET
    """ Code of the storage location """
    tags: Union[None, Unset, list[str]] = UNSET
    """ The tags of the storage location """
    image_id: Union[None, Unset, str] = UNSET
    """ The id of the image """
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    """ The ids of the users assigned to the storage location """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ The ids of the teams assigned to the storage location """
    attachment_ids: Union[None, Unset, list[str]] = UNSET
    """ The ids of the attachments """
    has_addressing: Union[None, Unset, bool] = UNSET
    """ Whether the storage location has addressing """
    has_stored_items: Union[None, Unset, bool] = UNSET
    """ Whether the storage location has stored items """
    image: Union["ApiSupplyImage", None, Unset] = UNSET
    attachments: Union[None, Unset, list["ApiSupplyAttachment"]] = UNSET
    """ The attachments of the storage location """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_supply_image import ApiSupplyImage
        from ..models.api_supply_storage_location_code_response import (
            ApiSupplyStorageLocationCodeResponse,
        )
        from ..models.api_supply_storage_location_deleted import (
            ApiSupplyStorageLocationDeleted,
        )
        from ..models.api_supply_storage_location_disabled import (
            ApiSupplyStorageLocationDisabled,
        )

        id = self.id

        company_id = self.company_id

        name = self.name

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
        elif isinstance(self.deleted, ApiSupplyStorageLocationDeleted):
            deleted = self.deleted.to_dict()
        else:
            deleted = self.deleted

        disabled: Union[None, Unset, dict[str, Any]]
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        elif isinstance(self.disabled, ApiSupplyStorageLocationDisabled):
            disabled = self.disabled.to_dict()
        else:
            disabled = self.disabled

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, ApiSupplyStorageLocationCodeResponse):
            code = self.code.to_dict()
        else:
            code = self.code

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        image_id: Union[None, Unset, str]
        if isinstance(self.image_id, Unset):
            image_id = UNSET
        else:
            image_id = self.image_id

        assigned_user_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = UNSET
        elif isinstance(self.assigned_user_ids, list):
            assigned_user_ids = self.assigned_user_ids

        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        attachment_ids: Union[None, Unset, list[str]]
        if isinstance(self.attachment_ids, Unset):
            attachment_ids = UNSET
        elif isinstance(self.attachment_ids, list):
            attachment_ids = self.attachment_ids

        else:
            attachment_ids = self.attachment_ids

        has_addressing: Union[None, Unset, bool]
        if isinstance(self.has_addressing, Unset):
            has_addressing = UNSET
        else:
            has_addressing = self.has_addressing

        has_stored_items: Union[None, Unset, bool]
        if isinstance(self.has_stored_items, Unset):
            has_stored_items = UNSET
        else:
            has_stored_items = self.has_stored_items

        image: Union[None, Unset, dict[str, Any]]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, ApiSupplyImage):
            image = self.image.to_dict()
        else:
            image = self.image

        attachments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "companyId": company_id,
                "name": name,
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
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if description is not UNSET:
            field_dict["description"] = description
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if address is not UNSET:
            field_dict["address"] = address
        if code is not UNSET:
            field_dict["code"] = code
        if tags is not UNSET:
            field_dict["tags"] = tags
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if attachment_ids is not UNSET:
            field_dict["attachmentIds"] = attachment_ids
        if has_addressing is not UNSET:
            field_dict["hasAddressing"] = has_addressing
        if has_stored_items is not UNSET:
            field_dict["hasStoredItems"] = has_stored_items
        if image is not UNSET:
            field_dict["image"] = image
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_attachment import ApiSupplyAttachment
        from ..models.api_supply_image import ApiSupplyImage
        from ..models.api_supply_storage_location_code_response import (
            ApiSupplyStorageLocationCodeResponse,
        )
        from ..models.api_supply_storage_location_deleted import (
            ApiSupplyStorageLocationDeleted,
        )
        from ..models.api_supply_storage_location_disabled import (
            ApiSupplyStorageLocationDisabled,
        )

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("companyId")

        name = d.pop("name")

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
        ) -> Union["ApiSupplyStorageLocationDeleted", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_type_0 = ApiSupplyStorageLocationDeleted.from_dict(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplyStorageLocationDeleted", None, Unset], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_disabled(
            data: object,
        ) -> Union["ApiSupplyStorageLocationDisabled", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                disabled_type_0 = ApiSupplyStorageLocationDisabled.from_dict(data)

                return disabled_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplyStorageLocationDisabled", None, Unset], data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_code(
            data: object,
        ) -> Union["ApiSupplyStorageLocationCodeResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                code_type_0 = ApiSupplyStorageLocationCodeResponse.from_dict(data)

                return code_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["ApiSupplyStorageLocationCodeResponse", None, Unset], data
            )

        code = _parse_code(d.pop("code", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_image_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_id = _parse_image_id(d.pop("imageId", UNSET))

        def _parse_assigned_user_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_user_ids_type_0 = cast(list[str], data)

                return assigned_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds", UNSET))

        def _parse_assigned_team_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds", UNSET))

        def _parse_attachment_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachment_ids_type_0 = cast(list[str], data)

                return attachment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        attachment_ids = _parse_attachment_ids(d.pop("attachmentIds", UNSET))

        def _parse_has_addressing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_addressing = _parse_has_addressing(d.pop("hasAddressing", UNSET))

        def _parse_has_stored_items(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_stored_items = _parse_has_stored_items(d.pop("hasStoredItems", UNSET))

        def _parse_image(data: object) -> Union["ApiSupplyImage", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = ApiSupplyImage.from_dict(data)

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplyImage", None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["ApiSupplyAttachment"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = ApiSupplyAttachment.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApiSupplyAttachment"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        api_supply_storage_location_response = cls(
            id=id,
            company_id=company_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            deleted=deleted,
            disabled=disabled,
            identifier_code=identifier_code,
            description=description,
            parent_id=parent_id,
            location_id=location_id,
            address=address,
            code=code,
            tags=tags,
            image_id=image_id,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            attachment_ids=attachment_ids,
            has_addressing=has_addressing,
            has_stored_items=has_stored_items,
            image=image,
            attachments=attachments,
        )

        api_supply_storage_location_response.additional_properties = d
        return api_supply_storage_location_response

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

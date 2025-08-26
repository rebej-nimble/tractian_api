from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_disabled_location import ApiDisabledLocation
    from ..models.api_locations_request_deleted import ApiLocationsRequestDeleted
    from ..models.entity_custom_field import EntityCustomField
    from ..models.file_motor import FileMotor


T = TypeVar("T", bound="ApiLocationsPutRequest")


@_attrs_define
class ApiLocationsPutRequest:
    id: str
    company_id: Union[None, Unset, str] = UNSET
    code: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    cost_center_id: Union[None, Unset, str] = UNSET
    disabled: Union[Unset, "ApiDisabledLocation"] = UNSET
    deleted: Union[Unset, "ApiLocationsRequestDeleted"] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    attachments: Union[None, Unset, list["FileMotor"]] = UNSET
    image: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    location_custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cost_center_id: Union[None, Unset, str]
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        disabled: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.disabled, Unset):
            disabled = self.disabled.to_dict()

        deleted: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.to_dict()

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

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

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

        location_custom_fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.location_custom_fields, Unset):
            location_custom_fields = UNSET
        elif isinstance(self.location_custom_fields, list):
            location_custom_fields = []
            for location_custom_fields_type_0_item_data in self.location_custom_fields:
                location_custom_fields_type_0_item = (
                    location_custom_fields_type_0_item_data.to_dict()
                )
                location_custom_fields.append(location_custom_fields_type_0_item)

        else:
            location_custom_fields = self.location_custom_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if code is not UNSET:
            field_dict["code"] = code
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if description is not UNSET:
            field_dict["description"] = description
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if name is not UNSET:
            field_dict["name"] = name
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if image is not UNSET:
            field_dict["image"] = image
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if location_custom_fields is not UNSET:
            field_dict["locationCustomFields"] = location_custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_disabled_location import ApiDisabledLocation
        from ..models.api_locations_request_deleted import ApiLocationsRequestDeleted
        from ..models.entity_custom_field import EntityCustomField
        from ..models.file_motor import FileMotor

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_cost_center_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        _disabled = d.pop("disabled", UNSET)
        disabled: Union[Unset, ApiDisabledLocation]
        if isinstance(_disabled, Unset):
            disabled = UNSET
        else:
            disabled = ApiDisabledLocation.from_dict(_disabled)

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, ApiLocationsRequestDeleted]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = ApiLocationsRequestDeleted.from_dict(_deleted)

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

        def _parse_attachments(data: object) -> Union[None, Unset, list["FileMotor"]]:
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
                    attachments_type_0_item = FileMotor.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["FileMotor"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

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

        def _parse_location_custom_fields(
            data: object,
        ) -> Union[None, Unset, list["EntityCustomField"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                location_custom_fields_type_0 = []
                _location_custom_fields_type_0 = data
                for (
                    location_custom_fields_type_0_item_data
                ) in _location_custom_fields_type_0:
                    location_custom_fields_type_0_item = EntityCustomField.from_dict(
                        location_custom_fields_type_0_item_data
                    )

                    location_custom_fields_type_0.append(
                        location_custom_fields_type_0_item
                    )

                return location_custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EntityCustomField"]], data)

        location_custom_fields = _parse_location_custom_fields(
            d.pop("locationCustomFields", UNSET)
        )

        api_locations_put_request = cls(
            id=id,
            company_id=company_id,
            code=code,
            external_id=external_id,
            description=description,
            parent_id=parent_id,
            name=name,
            cost_center_id=cost_center_id,
            disabled=disabled,
            deleted=deleted,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            attachments=attachments,
            image=image,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            location_custom_fields=location_custom_fields,
        )

        api_locations_put_request.additional_properties = d
        return api_locations_put_request

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

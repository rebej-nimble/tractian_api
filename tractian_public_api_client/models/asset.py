from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_attachment_motor import AssetAttachmentMotor
    from ..models.asset_criticality_motor import AssetCriticalityMotor
    from ..models.asset_inventory_item_motor import AssetInventoryItemMotor
    from ..models.asset_location_motor import AssetLocationMotor
    from ..models.asset_user_motor import AssetUserMotor
    from ..models.deleted import Deleted
    from ..models.disabled import Disabled
    from ..models.entity_custom_field import EntityCustomField
    from ..models.specifications import Specifications


T = TypeVar("T", bound="Asset")


@_attrs_define
class Asset:
    id: str
    name: str
    company_id: str
    external_id: Union[None, Unset, str] = UNSET
    attachments: Union[None, Unset, list["AssetAttachmentMotor"]] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    criticality: Union["AssetCriticalityMotor", None, Unset] = UNSET
    model_type: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    sensors: Union[None, Unset, list[str]] = UNSET
    description: Union[None, Unset, str] = UNSET
    criticality_id: Union[None, Unset, str] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    code: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    specifications: Union["Specifications", None, Unset] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    assigned_users: Union[None, Unset, list["AssetUserMotor"]] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    cost_center_id: Union[None, Unset, str] = UNSET
    created_by_user: Union["AssetUserMotor", None, Unset] = UNSET
    location: Union["AssetLocationMotor", None, Unset] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    disabled: Union[Unset, "Disabled"] = UNSET
    deleted: Union[Unset, "Deleted"] = UNSET
    inventory_items: Union[None, Unset, list["AssetInventoryItemMotor"]] = UNSET
    asset_custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    year: Union[None, Unset, int, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_criticality_motor import AssetCriticalityMotor
        from ..models.asset_location_motor import AssetLocationMotor
        from ..models.asset_user_motor import AssetUserMotor
        from ..models.specifications import Specifications

        id = self.id

        name = self.name

        company_id = self.company_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        manufacturer: Union[None, Unset, str]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = self.manufacturer

        criticality: Union[None, Unset, dict[str, Any]]
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, AssetCriticalityMotor):
            criticality = self.criticality.to_dict()
        else:
            criticality = self.criticality

        model_type: Union[None, Unset, str]
        if isinstance(self.model_type, Unset):
            model_type = UNSET
        else:
            model_type = self.model_type

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        sensors: Union[None, Unset, list[str]]
        if isinstance(self.sensors, Unset):
            sensors = UNSET
        elif isinstance(self.sensors, list):
            sensors = self.sensors

        else:
            sensors = self.sensors

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        criticality_id: Union[None, Unset, str]
        if isinstance(self.criticality_id, Unset):
            criticality_id = UNSET
        else:
            criticality_id = self.criticality_id

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        specifications: Union[None, Unset, dict[str, Any]]
        if isinstance(self.specifications, Unset):
            specifications = UNSET
        elif isinstance(self.specifications, Specifications):
            specifications = self.specifications.to_dict()
        else:
            specifications = self.specifications

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

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        assigned_users: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.assigned_users, Unset):
            assigned_users = UNSET
        elif isinstance(self.assigned_users, list):
            assigned_users = []
            for assigned_users_type_0_item_data in self.assigned_users:
                assigned_users_type_0_item = assigned_users_type_0_item_data.to_dict()
                assigned_users.append(assigned_users_type_0_item)

        else:
            assigned_users = self.assigned_users

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

        cost_center_id: Union[None, Unset, str]
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        created_by_user: Union[None, Unset, dict[str, Any]]
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, AssetUserMotor):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, AssetLocationMotor):
            location = self.location.to_dict()
        else:
            location = self.location

        equipment_id: Union[None, Unset, str]
        if isinstance(self.equipment_id, Unset):
            equipment_id = UNSET
        else:
            equipment_id = self.equipment_id

        disabled: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.disabled, Unset):
            disabled = self.disabled.to_dict()

        deleted: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.to_dict()

        inventory_items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.inventory_items, Unset):
            inventory_items = UNSET
        elif isinstance(self.inventory_items, list):
            inventory_items = []
            for inventory_items_type_0_item_data in self.inventory_items:
                inventory_items_type_0_item = inventory_items_type_0_item_data.to_dict()
                inventory_items.append(inventory_items_type_0_item)

        else:
            inventory_items = self.inventory_items

        asset_custom_fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.asset_custom_fields, Unset):
            asset_custom_fields = UNSET
        elif isinstance(self.asset_custom_fields, list):
            asset_custom_fields = []
            for asset_custom_fields_type_0_item_data in self.asset_custom_fields:
                asset_custom_fields_type_0_item = (
                    asset_custom_fields_type_0_item_data.to_dict()
                )
                asset_custom_fields.append(asset_custom_fields_type_0_item)

        else:
            asset_custom_fields = self.asset_custom_fields

        year: Union[None, Unset, int, str]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "companyId": company_id,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if model_type is not UNSET:
            field_dict["modelType"] = model_type
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sensors is not UNSET:
            field_dict["sensors"] = sensors
        if description is not UNSET:
            field_dict["description"] = description
        if criticality_id is not UNSET:
            field_dict["criticalityId"] = criticality_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if code is not UNSET:
            field_dict["code"] = code
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if specifications is not UNSET:
            field_dict["specifications"] = specifications
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if assigned_users is not UNSET:
            field_dict["assignedUsers"] = assigned_users
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if created_by_user is not UNSET:
            field_dict["createdByUser"] = created_by_user
        if location is not UNSET:
            field_dict["location"] = location
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if inventory_items is not UNSET:
            field_dict["inventoryItems"] = inventory_items
        if asset_custom_fields is not UNSET:
            field_dict["assetCustomFields"] = asset_custom_fields
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_attachment_motor import AssetAttachmentMotor
        from ..models.asset_criticality_motor import AssetCriticalityMotor
        from ..models.asset_inventory_item_motor import AssetInventoryItemMotor
        from ..models.asset_location_motor import AssetLocationMotor
        from ..models.asset_user_motor import AssetUserMotor
        from ..models.deleted import Deleted
        from ..models.disabled import Disabled
        from ..models.entity_custom_field import EntityCustomField
        from ..models.specifications import Specifications

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("companyId")

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["AssetAttachmentMotor"]]:
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
                    attachments_type_0_item = AssetAttachmentMotor.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AssetAttachmentMotor"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_criticality(
            data: object,
        ) -> Union["AssetCriticalityMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                criticality_type_0 = AssetCriticalityMotor.from_dict(data)

                return criticality_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AssetCriticalityMotor", None, Unset], data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_model_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_type = _parse_model_type(d.pop("modelType", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

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

        def _parse_sensors(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sensors_type_0 = cast(list[str], data)

                return sensors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        sensors = _parse_sensors(d.pop("sensors", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_criticality_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        criticality_id = _parse_criticality_id(d.pop("criticalityId", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_specifications(data: object) -> Union["Specifications", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                specifications_type_0 = Specifications.from_dict(data)

                return specifications_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Specifications", None, Unset], data)

        specifications = _parse_specifications(d.pop("specifications", UNSET))

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

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        def _parse_assigned_users(
            data: object,
        ) -> Union[None, Unset, list["AssetUserMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_users_type_0 = []
                _assigned_users_type_0 = data
                for assigned_users_type_0_item_data in _assigned_users_type_0:
                    assigned_users_type_0_item = AssetUserMotor.from_dict(
                        assigned_users_type_0_item_data
                    )

                    assigned_users_type_0.append(assigned_users_type_0_item)

                return assigned_users_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AssetUserMotor"]], data)

        assigned_users = _parse_assigned_users(d.pop("assignedUsers", UNSET))

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

        def _parse_cost_center_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        def _parse_created_by_user(
            data: object,
        ) -> Union["AssetUserMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = AssetUserMotor.from_dict(data)

                return created_by_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AssetUserMotor", None, Unset], data)

        created_by_user = _parse_created_by_user(d.pop("createdByUser", UNSET))

        def _parse_location(data: object) -> Union["AssetLocationMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = AssetLocationMotor.from_dict(data)

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AssetLocationMotor", None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        equipment_id = _parse_equipment_id(d.pop("equipmentId", UNSET))

        _disabled = d.pop("disabled", UNSET)
        disabled: Union[Unset, Disabled]
        if isinstance(_disabled, Unset):
            disabled = UNSET
        else:
            disabled = Disabled.from_dict(_disabled)

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, Deleted]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = Deleted.from_dict(_deleted)

        def _parse_inventory_items(
            data: object,
        ) -> Union[None, Unset, list["AssetInventoryItemMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inventory_items_type_0 = []
                _inventory_items_type_0 = data
                for inventory_items_type_0_item_data in _inventory_items_type_0:
                    inventory_items_type_0_item = AssetInventoryItemMotor.from_dict(
                        inventory_items_type_0_item_data
                    )

                    inventory_items_type_0.append(inventory_items_type_0_item)

                return inventory_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AssetInventoryItemMotor"]], data)

        inventory_items = _parse_inventory_items(d.pop("inventoryItems", UNSET))

        def _parse_asset_custom_fields(
            data: object,
        ) -> Union[None, Unset, list["EntityCustomField"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_custom_fields_type_0 = []
                _asset_custom_fields_type_0 = data
                for asset_custom_fields_type_0_item_data in _asset_custom_fields_type_0:
                    asset_custom_fields_type_0_item = EntityCustomField.from_dict(
                        asset_custom_fields_type_0_item_data
                    )

                    asset_custom_fields_type_0.append(asset_custom_fields_type_0_item)

                return asset_custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EntityCustomField"]], data)

        asset_custom_fields = _parse_asset_custom_fields(
            d.pop("assetCustomFields", UNSET)
        )

        def _parse_year(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        year = _parse_year(d.pop("year", UNSET))

        asset = cls(
            id=id,
            name=name,
            company_id=company_id,
            external_id=external_id,
            attachments=attachments,
            manufacturer=manufacturer,
            criticality=criticality,
            model_type=model_type,
            serial_number=serial_number,
            tags=tags,
            sensors=sensors,
            description=description,
            criticality_id=criticality_id,
            location_id=location_id,
            parent_id=parent_id,
            code=code,
            created_by_user_id=created_by_user_id,
            specifications=specifications,
            created_at=created_at,
            updated_at=updated_at,
            updated_by_user_id=updated_by_user_id,
            assigned_users=assigned_users,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            cost_center_id=cost_center_id,
            created_by_user=created_by_user,
            location=location,
            equipment_id=equipment_id,
            disabled=disabled,
            deleted=deleted,
            inventory_items=inventory_items,
            asset_custom_fields=asset_custom_fields,
            year=year,
        )

        asset.additional_properties = d
        return asset

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

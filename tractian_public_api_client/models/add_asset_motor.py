from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_asset_motor_attachment import AddAssetMotorAttachment
    from ..models.entity_custom_field import EntityCustomField
    from ..models.specification_motor import SpecificationMotor


T = TypeVar("T", bound="AddAssetMotor")


@_attrs_define
class AddAssetMotor:
    name: str
    company_id: str
    location_id: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    cost_center_id: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    code: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    model_description: Union[None, Unset, str] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    year: Union[None, Unset, int] = UNSET
    sensor_type: Union[None, Unset, str] = UNSET
    sensor_id: Union[None, Unset, str] = UNSET
    remove_sensor: Union[None, Unset, bool] = UNSET
    keep_collects: Union[None, Unset, bool] = UNSET
    sensors: Union[None, Unset, list[str]] = UNSET
    attachments: Union[None, Unset, list["AddAssetMotorAttachment"]] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    criticality_id: Union[None, Unset, str] = UNSET
    specifications: Union["SpecificationMotor", None, Unset] = UNSET
    asset_custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.specification_motor import SpecificationMotor

        name = self.name

        company_id = self.company_id

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

        cost_center_id: Union[None, Unset, str]
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        manufacturer: Union[None, Unset, str]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = self.manufacturer

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

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        model_description: Union[None, Unset, str]
        if isinstance(self.model_description, Unset):
            model_description = UNSET
        else:
            model_description = self.model_description

        equipment_id: Union[None, Unset, str]
        if isinstance(self.equipment_id, Unset):
            equipment_id = UNSET
        else:
            equipment_id = self.equipment_id

        year: Union[None, Unset, int]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        sensor_type: Union[None, Unset, str]
        if isinstance(self.sensor_type, Unset):
            sensor_type = UNSET
        else:
            sensor_type = self.sensor_type

        sensor_id: Union[None, Unset, str]
        if isinstance(self.sensor_id, Unset):
            sensor_id = UNSET
        else:
            sensor_id = self.sensor_id

        remove_sensor: Union[None, Unset, bool]
        if isinstance(self.remove_sensor, Unset):
            remove_sensor = UNSET
        else:
            remove_sensor = self.remove_sensor

        keep_collects: Union[None, Unset, bool]
        if isinstance(self.keep_collects, Unset):
            keep_collects = UNSET
        else:
            keep_collects = self.keep_collects

        sensors: Union[None, Unset, list[str]]
        if isinstance(self.sensors, Unset):
            sensors = UNSET
        elif isinstance(self.sensors, list):
            sensors = self.sensors

        else:
            sensors = self.sensors

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

        criticality_id: Union[None, Unset, str]
        if isinstance(self.criticality_id, Unset):
            criticality_id = UNSET
        else:
            criticality_id = self.criticality_id

        specifications: Union[None, Unset, dict[str, Any]]
        if isinstance(self.specifications, Unset):
            specifications = UNSET
        elif isinstance(self.specifications, SpecificationMotor):
            specifications = self.specifications.to_dict()
        else:
            specifications = self.specifications

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "companyId": company_id,
            }
        )
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if description is not UNSET:
            field_dict["description"] = description
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if tags is not UNSET:
            field_dict["tags"] = tags
        if code is not UNSET:
            field_dict["code"] = code
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if model_description is not UNSET:
            field_dict["modelDescription"] = model_description
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if year is not UNSET:
            field_dict["year"] = year
        if sensor_type is not UNSET:
            field_dict["sensorType"] = sensor_type
        if sensor_id is not UNSET:
            field_dict["sensorId"] = sensor_id
        if remove_sensor is not UNSET:
            field_dict["removeSensor"] = remove_sensor
        if keep_collects is not UNSET:
            field_dict["keepCollects"] = keep_collects
        if sensors is not UNSET:
            field_dict["sensors"] = sensors
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if criticality_id is not UNSET:
            field_dict["criticalityId"] = criticality_id
        if specifications is not UNSET:
            field_dict["specifications"] = specifications
        if asset_custom_fields is not UNSET:
            field_dict["assetCustomFields"] = asset_custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_asset_motor_attachment import AddAssetMotorAttachment
        from ..models.entity_custom_field import EntityCustomField
        from ..models.specification_motor import SpecificationMotor

        d = dict(src_dict)
        name = d.pop("name")

        company_id = d.pop("companyId")

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

        def _parse_cost_center_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

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

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_model_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_description = _parse_model_description(d.pop("modelDescription", UNSET))

        def _parse_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        equipment_id = _parse_equipment_id(d.pop("equipmentId", UNSET))

        def _parse_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        year = _parse_year(d.pop("year", UNSET))

        def _parse_sensor_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sensor_type = _parse_sensor_type(d.pop("sensorType", UNSET))

        def _parse_sensor_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sensor_id = _parse_sensor_id(d.pop("sensorId", UNSET))

        def _parse_remove_sensor(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        remove_sensor = _parse_remove_sensor(d.pop("removeSensor", UNSET))

        def _parse_keep_collects(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        keep_collects = _parse_keep_collects(d.pop("keepCollects", UNSET))

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

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["AddAssetMotorAttachment"]]:
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
                    attachments_type_0_item = AddAssetMotorAttachment.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AddAssetMotorAttachment"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

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

        def _parse_criticality_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        criticality_id = _parse_criticality_id(d.pop("criticalityId", UNSET))

        def _parse_specifications(
            data: object,
        ) -> Union["SpecificationMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                specifications_type_0 = SpecificationMotor.from_dict(data)

                return specifications_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SpecificationMotor", None, Unset], data)

        specifications = _parse_specifications(d.pop("specifications", UNSET))

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

        add_asset_motor = cls(
            name=name,
            company_id=company_id,
            location_id=location_id,
            parent_id=parent_id,
            cost_center_id=cost_center_id,
            description=description,
            manufacturer=manufacturer,
            serial_number=serial_number,
            tags=tags,
            code=code,
            identifier_code=identifier_code,
            model_description=model_description,
            equipment_id=equipment_id,
            year=year,
            sensor_type=sensor_type,
            sensor_id=sensor_id,
            remove_sensor=remove_sensor,
            keep_collects=keep_collects,
            sensors=sensors,
            attachments=attachments,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            criticality_id=criticality_id,
            specifications=specifications,
            asset_custom_fields=asset_custom_fields,
        )

        add_asset_motor.additional_properties = d
        return add_asset_motor

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.measurement_unit import MeasurementUnit, check_measurement_unit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_motor_request_batch_api import InventoryMotorRequestBatchAPI
    from ..models.inventory_motor_request_disabled_api import (
        InventoryMotorRequestDisabledAPI,
    )


T = TypeVar("T", bound="InventoryMotorRequestAPI")


@_attrs_define
class InventoryMotorRequestAPI:
    name: str
    """ Name of the inventory item. """
    measurement_unit: MeasurementUnit
    disabled: "InventoryMotorRequestDisabledAPI"
    identifier_code: Union[None, Unset, str] = UNSET
    """ Unique identifier code of the item, if applicable. This field should be used to store the customer's unique
    code for the item. """
    maximum_quantity: Union[None, Unset, float] = UNSET
    """ Maximum allowed quantity in stock. """
    minimum_quantity: Union[None, Unset, float] = UNSET
    """ Minimum required quantity in stock. """
    unit_cost: Union[None, Unset, float] = UNSET
    """ Unit cost of the item. """
    stock_quantity: Union[None, Unset, float] = UNSET
    """ Current available stock quantity. """
    batches: Union[None, Unset, list["InventoryMotorRequestBatchAPI"]] = UNSET
    """ List of batches associated with the item. """
    location_id: Union[None, Unset, str] = UNSET
    """ Identifier of the location where the item is stored. """
    description: Union[None, Unset, str] = UNSET
    """ Detailed description of the item. """
    material_type_id: Union[None, Unset, str] = UNSET
    """ Identifier of the material type of the item. """
    ncm_and_hs_code: Union[None, Unset, str] = UNSET
    """ NCM and HS code for customs classification. """
    lead_time: Union[None, Unset, float] = UNSET
    """ Estimated lead time for replenishment. """
    code: Union[None, Unset, str] = UNSET
    """ Additional code related to the item. """
    tags: Union[None, Unset, list[str]] = UNSET
    """ List of tags associated with the item. """
    assigned_users_ids: Union[None, Unset, list[str]] = UNSET
    """ List of user IDs assigned to the item. """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ List of team IDs assigned to the item. """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        measurement_unit: str = self.measurement_unit

        disabled = self.disabled.to_dict()

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        maximum_quantity: Union[None, Unset, float]
        if isinstance(self.maximum_quantity, Unset):
            maximum_quantity = UNSET
        else:
            maximum_quantity = self.maximum_quantity

        minimum_quantity: Union[None, Unset, float]
        if isinstance(self.minimum_quantity, Unset):
            minimum_quantity = UNSET
        else:
            minimum_quantity = self.minimum_quantity

        unit_cost: Union[None, Unset, float]
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        stock_quantity: Union[None, Unset, float]
        if isinstance(self.stock_quantity, Unset):
            stock_quantity = UNSET
        else:
            stock_quantity = self.stock_quantity

        batches: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.batches, Unset):
            batches = UNSET
        elif isinstance(self.batches, list):
            batches = []
            for batches_type_0_item_data in self.batches:
                batches_type_0_item = batches_type_0_item_data.to_dict()
                batches.append(batches_type_0_item)

        else:
            batches = self.batches

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        material_type_id: Union[None, Unset, str]
        if isinstance(self.material_type_id, Unset):
            material_type_id = UNSET
        else:
            material_type_id = self.material_type_id

        ncm_and_hs_code: Union[None, Unset, str]
        if isinstance(self.ncm_and_hs_code, Unset):
            ncm_and_hs_code = UNSET
        else:
            ncm_and_hs_code = self.ncm_and_hs_code

        lead_time: Union[None, Unset, float]
        if isinstance(self.lead_time, Unset):
            lead_time = UNSET
        else:
            lead_time = self.lead_time

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        assigned_users_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_users_ids, Unset):
            assigned_users_ids = UNSET
        elif isinstance(self.assigned_users_ids, list):
            assigned_users_ids = self.assigned_users_ids

        else:
            assigned_users_ids = self.assigned_users_ids

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "measurementUnit": measurement_unit,
                "disabled": disabled,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if maximum_quantity is not UNSET:
            field_dict["maximumQuantity"] = maximum_quantity
        if minimum_quantity is not UNSET:
            field_dict["minimumQuantity"] = minimum_quantity
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if stock_quantity is not UNSET:
            field_dict["stockQuantity"] = stock_quantity
        if batches is not UNSET:
            field_dict["batches"] = batches
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if description is not UNSET:
            field_dict["description"] = description
        if material_type_id is not UNSET:
            field_dict["materialTypeId"] = material_type_id
        if ncm_and_hs_code is not UNSET:
            field_dict["ncmAndHsCode"] = ncm_and_hs_code
        if lead_time is not UNSET:
            field_dict["leadTime"] = lead_time
        if code is not UNSET:
            field_dict["code"] = code
        if tags is not UNSET:
            field_dict["tags"] = tags
        if assigned_users_ids is not UNSET:
            field_dict["assignedUsersIds"] = assigned_users_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_motor_request_batch_api import (
            InventoryMotorRequestBatchAPI,
        )
        from ..models.inventory_motor_request_disabled_api import (
            InventoryMotorRequestDisabledAPI,
        )

        d = dict(src_dict)
        name = d.pop("name")

        measurement_unit = check_measurement_unit(d.pop("measurementUnit"))

        disabled = InventoryMotorRequestDisabledAPI.from_dict(d.pop("disabled"))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_maximum_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        maximum_quantity = _parse_maximum_quantity(d.pop("maximumQuantity", UNSET))

        def _parse_minimum_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        minimum_quantity = _parse_minimum_quantity(d.pop("minimumQuantity", UNSET))

        def _parse_unit_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        def _parse_stock_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        stock_quantity = _parse_stock_quantity(d.pop("stockQuantity", UNSET))

        def _parse_batches(
            data: object,
        ) -> Union[None, Unset, list["InventoryMotorRequestBatchAPI"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                batches_type_0 = []
                _batches_type_0 = data
                for batches_type_0_item_data in _batches_type_0:
                    batches_type_0_item = InventoryMotorRequestBatchAPI.from_dict(
                        batches_type_0_item_data
                    )

                    batches_type_0.append(batches_type_0_item)

                return batches_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["InventoryMotorRequestBatchAPI"]], data)

        batches = _parse_batches(d.pop("batches", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_material_type_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        material_type_id = _parse_material_type_id(d.pop("materialTypeId", UNSET))

        def _parse_ncm_and_hs_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ncm_and_hs_code = _parse_ncm_and_hs_code(d.pop("ncmAndHsCode", UNSET))

        def _parse_lead_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lead_time = _parse_lead_time(d.pop("leadTime", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

        def _parse_assigned_users_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_users_ids_type_0 = cast(list[str], data)

                return assigned_users_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_users_ids = _parse_assigned_users_ids(d.pop("assignedUsersIds", UNSET))

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

        inventory_motor_request_api = cls(
            name=name,
            measurement_unit=measurement_unit,
            disabled=disabled,
            identifier_code=identifier_code,
            maximum_quantity=maximum_quantity,
            minimum_quantity=minimum_quantity,
            unit_cost=unit_cost,
            stock_quantity=stock_quantity,
            batches=batches,
            location_id=location_id,
            description=description,
            material_type_id=material_type_id,
            ncm_and_hs_code=ncm_and_hs_code,
            lead_time=lead_time,
            code=code,
            tags=tags,
            assigned_users_ids=assigned_users_ids,
            assigned_team_ids=assigned_team_ids,
        )

        return inventory_motor_request_api

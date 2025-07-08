from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_custom_field import EntityCustomField
    from ..models.work_order_operations_procedure import WorkOrderOperationsProcedure


T = TypeVar("T", bound="WorkOrderOperations")


@_attrs_define
class WorkOrderOperations:
    id: str
    order: int
    work_order_operation_procedures: Union[
        None, Unset, list["WorkOrderOperationsProcedure"]
    ] = UNSET
    number: Union[None, Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    activity_type_id: Union[None, Unset, str] = UNSET
    planned_working_time: Union[None, Unset, int] = UNSET
    planned_worker_number: Union[None, Unset, int] = UNSET
    supply_item_ids: Union[None, Unset, list[str]] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    work_order_operation_custom_fields: Union[
        None, Unset, list["EntityCustomField"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order = self.order

        work_order_operation_procedures: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.work_order_operation_procedures, Unset):
            work_order_operation_procedures = UNSET
        elif isinstance(self.work_order_operation_procedures, list):
            work_order_operation_procedures = []
            for (
                work_order_operation_procedures_type_0_item_data
            ) in self.work_order_operation_procedures:
                work_order_operation_procedures_type_0_item = (
                    work_order_operation_procedures_type_0_item_data.to_dict()
                )
                work_order_operation_procedures.append(
                    work_order_operation_procedures_type_0_item
                )

        else:
            work_order_operation_procedures = self.work_order_operation_procedures

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        activity_type_id: Union[None, Unset, str]
        if isinstance(self.activity_type_id, Unset):
            activity_type_id = UNSET
        else:
            activity_type_id = self.activity_type_id

        planned_working_time: Union[None, Unset, int]
        if isinstance(self.planned_working_time, Unset):
            planned_working_time = UNSET
        else:
            planned_working_time = self.planned_working_time

        planned_worker_number: Union[None, Unset, int]
        if isinstance(self.planned_worker_number, Unset):
            planned_worker_number = UNSET
        else:
            planned_worker_number = self.planned_worker_number

        supply_item_ids: Union[None, Unset, list[str]]
        if isinstance(self.supply_item_ids, Unset):
            supply_item_ids = UNSET
        elif isinstance(self.supply_item_ids, list):
            supply_item_ids = self.supply_item_ids

        else:
            supply_item_ids = self.supply_item_ids

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        work_order_operation_custom_fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.work_order_operation_custom_fields, Unset):
            work_order_operation_custom_fields = UNSET
        elif isinstance(self.work_order_operation_custom_fields, list):
            work_order_operation_custom_fields = []
            for (
                work_order_operation_custom_fields_type_0_item_data
            ) in self.work_order_operation_custom_fields:
                work_order_operation_custom_fields_type_0_item = (
                    work_order_operation_custom_fields_type_0_item_data.to_dict()
                )
                work_order_operation_custom_fields.append(
                    work_order_operation_custom_fields_type_0_item
                )

        else:
            work_order_operation_custom_fields = self.work_order_operation_custom_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order": order,
            }
        )
        if work_order_operation_procedures is not UNSET:
            field_dict["workOrderOperationProcedures"] = work_order_operation_procedures
        if number is not UNSET:
            field_dict["number"] = number
        if title is not UNSET:
            field_dict["title"] = title
        if activity_type_id is not UNSET:
            field_dict["activityTypeId"] = activity_type_id
        if planned_working_time is not UNSET:
            field_dict["plannedWorkingTime"] = planned_working_time
        if planned_worker_number is not UNSET:
            field_dict["plannedWorkerNumber"] = planned_worker_number
        if supply_item_ids is not UNSET:
            field_dict["supplyItemIds"] = supply_item_ids
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if work_order_operation_custom_fields is not UNSET:
            field_dict["workOrderOperationCustomFields"] = (
                work_order_operation_custom_fields
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_custom_field import EntityCustomField
        from ..models.work_order_operations_procedure import (
            WorkOrderOperationsProcedure,
        )

        d = dict(src_dict)
        id = d.pop("id")

        order = d.pop("order")

        def _parse_work_order_operation_procedures(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderOperationsProcedure"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_procedures_type_0 = []
                _work_order_operation_procedures_type_0 = data
                for (
                    work_order_operation_procedures_type_0_item_data
                ) in _work_order_operation_procedures_type_0:
                    work_order_operation_procedures_type_0_item = (
                        WorkOrderOperationsProcedure.from_dict(
                            work_order_operation_procedures_type_0_item_data
                        )
                    )

                    work_order_operation_procedures_type_0.append(
                        work_order_operation_procedures_type_0_item
                    )

                return work_order_operation_procedures_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrderOperationsProcedure"]], data)

        work_order_operation_procedures = _parse_work_order_operation_procedures(
            d.pop("workOrderOperationProcedures", UNSET)
        )

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_activity_type_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activity_type_id = _parse_activity_type_id(d.pop("activityTypeId", UNSET))

        def _parse_planned_working_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        planned_working_time = _parse_planned_working_time(
            d.pop("plannedWorkingTime", UNSET)
        )

        def _parse_planned_worker_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        planned_worker_number = _parse_planned_worker_number(
            d.pop("plannedWorkerNumber", UNSET)
        )

        def _parse_supply_item_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supply_item_ids_type_0 = cast(list[str], data)

                return supply_item_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        supply_item_ids = _parse_supply_item_ids(d.pop("supplyItemIds", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_work_order_operation_custom_fields(
            data: object,
        ) -> Union[None, Unset, list["EntityCustomField"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_custom_fields_type_0 = []
                _work_order_operation_custom_fields_type_0 = data
                for (
                    work_order_operation_custom_fields_type_0_item_data
                ) in _work_order_operation_custom_fields_type_0:
                    work_order_operation_custom_fields_type_0_item = (
                        EntityCustomField.from_dict(
                            work_order_operation_custom_fields_type_0_item_data
                        )
                    )

                    work_order_operation_custom_fields_type_0.append(
                        work_order_operation_custom_fields_type_0_item
                    )

                return work_order_operation_custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EntityCustomField"]], data)

        work_order_operation_custom_fields = _parse_work_order_operation_custom_fields(
            d.pop("workOrderOperationCustomFields", UNSET)
        )

        work_order_operations = cls(
            id=id,
            order=order,
            work_order_operation_procedures=work_order_operation_procedures,
            number=number,
            title=title,
            activity_type_id=activity_type_id,
            planned_working_time=planned_working_time,
            planned_worker_number=planned_worker_number,
            supply_item_ids=supply_item_ids,
            asset_id=asset_id,
            location_id=location_id,
            work_order_operation_custom_fields=work_order_operation_custom_fields,
        )

        work_order_operations.additional_properties = d
        return work_order_operations

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

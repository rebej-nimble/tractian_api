from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_custom_field import EntityCustomField
    from ..models.work_order_operation_asset_motor import WorkOrderOperationAssetMotor
    from ..models.workorder_operation_procedure import WorkorderOperationProcedure


T = TypeVar("T", bound="WorkOrderOperationMotor")


@_attrs_define
class WorkOrderOperationMotor:
    id: str
    """ Unique identifier for the work order operation motor. """
    activity_type_id: Union[None, Unset, str] = UNSET
    """ Identifier for the type of activity associated with the operation. """
    asset_id: Union[None, Unset, str] = UNSET
    """ Identifier for the asset related to this operation. """
    title: Union[None, Unset, str] = UNSET
    """ Title or short description of the work order operation. """
    work_order_id: Union[None, Unset, str] = UNSET
    """ Identifier for the related work order. """
    company_id: Union[None, Unset, str] = UNSET
    """ Identifier for the company responsible for the work order. """
    created_at: Union[None, Unset, str] = UNSET
    """ Timestamp of when the work order operation was created. """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ Identifier of the user who created the work order operation. """
    order: Union[None, Unset, int] = UNSET
    """ Order number indicating the sequence of this operation within the work order. """
    status: Union[None, Unset, str] = UNSET
    """ Current status of the work order operation. """
    updated_at: Union[None, Unset, str] = UNSET
    """ Timestamp of when the work order operation was last updated. """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ Identifier of the user who last updated the work order operation. """
    number: Union[None, Unset, int] = UNSET
    """ Unique number assigned to the work order operation. """
    work_order_operation_timer_ids: Union[None, Unset, list[str]] = UNSET
    """ List of timer identifiers associated with this operation. """
    location_id: Union[None, Unset, str] = UNSET
    """ Identifier for the location where the operation takes place. """
    planned_team_id: Union[None, Unset, str] = UNSET
    """ Identifier for the team planned to execute this operation. """
    planned_working_time: Union[None, Unset, int] = UNSET
    """ Estimated working time required for the operation (in minutes). """
    planned_worker_number: Union[None, Unset, int] = UNSET
    """ Number of workers planned for this operation. """
    executant_ids: Union[None, Unset, list[str]] = UNSET
    """ List of identifiers for the users executing the operation. """
    work_order_operation_procedure_ids: Union[None, Unset, list[str]] = UNSET
    """ List of procedure identifiers related to this operation. """
    work_order_operation_procedures: Union[
        None, Unset, list["WorkorderOperationProcedure"]
    ] = UNSET
    """ List of work order procedures related to workorder operation. """
    asset: Union["WorkOrderOperationAssetMotor", None, Unset] = UNSET
    """ Asset data related to the operation. """
    work_order_item_statuses: Union[None, Unset, list[str]] = UNSET
    """ List of work order item statuses related to the operation. """
    supply_item_ids: Union[None, Unset, list[str]] = UNSET
    """ List of supply item identifiers related to the operation. """
    work_order_operation_custom_fields: Union[
        None, Unset, list["EntityCustomField"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.work_order_operation_asset_motor import (
            WorkOrderOperationAssetMotor,
        )

        id = self.id

        activity_type_id: Union[None, Unset, str]
        if isinstance(self.activity_type_id, Unset):
            activity_type_id = UNSET
        else:
            activity_type_id = self.activity_type_id

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        order: Union[None, Unset, int]
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        work_order_operation_timer_ids: Union[None, Unset, list[str]]
        if isinstance(self.work_order_operation_timer_ids, Unset):
            work_order_operation_timer_ids = UNSET
        elif isinstance(self.work_order_operation_timer_ids, list):
            work_order_operation_timer_ids = self.work_order_operation_timer_ids

        else:
            work_order_operation_timer_ids = self.work_order_operation_timer_ids

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        planned_team_id: Union[None, Unset, str]
        if isinstance(self.planned_team_id, Unset):
            planned_team_id = UNSET
        else:
            planned_team_id = self.planned_team_id

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

        executant_ids: Union[None, Unset, list[str]]
        if isinstance(self.executant_ids, Unset):
            executant_ids = UNSET
        elif isinstance(self.executant_ids, list):
            executant_ids = self.executant_ids

        else:
            executant_ids = self.executant_ids

        work_order_operation_procedure_ids: Union[None, Unset, list[str]]
        if isinstance(self.work_order_operation_procedure_ids, Unset):
            work_order_operation_procedure_ids = UNSET
        elif isinstance(self.work_order_operation_procedure_ids, list):
            work_order_operation_procedure_ids = self.work_order_operation_procedure_ids

        else:
            work_order_operation_procedure_ids = self.work_order_operation_procedure_ids

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

        asset: Union[None, Unset, dict[str, Any]]
        if isinstance(self.asset, Unset):
            asset = UNSET
        elif isinstance(self.asset, WorkOrderOperationAssetMotor):
            asset = self.asset.to_dict()
        else:
            asset = self.asset

        work_order_item_statuses: Union[None, Unset, list[str]]
        if isinstance(self.work_order_item_statuses, Unset):
            work_order_item_statuses = UNSET
        elif isinstance(self.work_order_item_statuses, list):
            work_order_item_statuses = self.work_order_item_statuses

        else:
            work_order_item_statuses = self.work_order_item_statuses

        supply_item_ids: Union[None, Unset, list[str]]
        if isinstance(self.supply_item_ids, Unset):
            supply_item_ids = UNSET
        elif isinstance(self.supply_item_ids, list):
            supply_item_ids = self.supply_item_ids

        else:
            supply_item_ids = self.supply_item_ids

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
            }
        )
        if activity_type_id is not UNSET:
            field_dict["activityTypeId"] = activity_type_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if title is not UNSET:
            field_dict["title"] = title
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if order is not UNSET:
            field_dict["order"] = order
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if number is not UNSET:
            field_dict["number"] = number
        if work_order_operation_timer_ids is not UNSET:
            field_dict["workOrderOperationTimerIds"] = work_order_operation_timer_ids
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if planned_team_id is not UNSET:
            field_dict["plannedTeamId"] = planned_team_id
        if planned_working_time is not UNSET:
            field_dict["plannedWorkingTime"] = planned_working_time
        if planned_worker_number is not UNSET:
            field_dict["plannedWorkerNumber"] = planned_worker_number
        if executant_ids is not UNSET:
            field_dict["executantIds"] = executant_ids
        if work_order_operation_procedure_ids is not UNSET:
            field_dict["workOrderOperationProcedureIds"] = (
                work_order_operation_procedure_ids
            )
        if work_order_operation_procedures is not UNSET:
            field_dict["workOrderOperationProcedures"] = work_order_operation_procedures
        if asset is not UNSET:
            field_dict["asset"] = asset
        if work_order_item_statuses is not UNSET:
            field_dict["workOrderItemStatuses"] = work_order_item_statuses
        if supply_item_ids is not UNSET:
            field_dict["supplyItemIds"] = supply_item_ids
        if work_order_operation_custom_fields is not UNSET:
            field_dict["workOrderOperationCustomFields"] = (
                work_order_operation_custom_fields
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_custom_field import EntityCustomField
        from ..models.work_order_operation_asset_motor import (
            WorkOrderOperationAssetMotor,
        )
        from ..models.workorder_operation_procedure import WorkorderOperationProcedure

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_activity_type_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activity_type_id = _parse_activity_type_id(d.pop("activityTypeId", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        order = _parse_order(d.pop("order", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_work_order_operation_timer_ids(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_timer_ids_type_0 = cast(list[str], data)

                return work_order_operation_timer_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        work_order_operation_timer_ids = _parse_work_order_operation_timer_ids(
            d.pop("workOrderOperationTimerIds", UNSET)
        )

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_planned_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        planned_team_id = _parse_planned_team_id(d.pop("plannedTeamId", UNSET))

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

        def _parse_executant_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                executant_ids_type_0 = cast(list[str], data)

                return executant_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        executant_ids = _parse_executant_ids(d.pop("executantIds", UNSET))

        def _parse_work_order_operation_procedure_ids(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_procedure_ids_type_0 = cast(list[str], data)

                return work_order_operation_procedure_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        work_order_operation_procedure_ids = _parse_work_order_operation_procedure_ids(
            d.pop("workOrderOperationProcedureIds", UNSET)
        )

        def _parse_work_order_operation_procedures(
            data: object,
        ) -> Union[None, Unset, list["WorkorderOperationProcedure"]]:
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
                        WorkorderOperationProcedure.from_dict(
                            work_order_operation_procedures_type_0_item_data
                        )
                    )

                    work_order_operation_procedures_type_0.append(
                        work_order_operation_procedures_type_0_item
                    )

                return work_order_operation_procedures_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkorderOperationProcedure"]], data)

        work_order_operation_procedures = _parse_work_order_operation_procedures(
            d.pop("workOrderOperationProcedures", UNSET)
        )

        def _parse_asset(
            data: object,
        ) -> Union["WorkOrderOperationAssetMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_type_0 = WorkOrderOperationAssetMotor.from_dict(data)

                return asset_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkOrderOperationAssetMotor", None, Unset], data)

        asset = _parse_asset(d.pop("asset", UNSET))

        def _parse_work_order_item_statuses(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_item_statuses_type_0 = cast(list[str], data)

                return work_order_item_statuses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        work_order_item_statuses = _parse_work_order_item_statuses(
            d.pop("workOrderItemStatuses", UNSET)
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

        work_order_operation_motor = cls(
            id=id,
            activity_type_id=activity_type_id,
            asset_id=asset_id,
            title=title,
            work_order_id=work_order_id,
            company_id=company_id,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            order=order,
            status=status,
            updated_at=updated_at,
            updated_by_user_id=updated_by_user_id,
            number=number,
            work_order_operation_timer_ids=work_order_operation_timer_ids,
            location_id=location_id,
            planned_team_id=planned_team_id,
            planned_working_time=planned_working_time,
            planned_worker_number=planned_worker_number,
            executant_ids=executant_ids,
            work_order_operation_procedure_ids=work_order_operation_procedure_ids,
            work_order_operation_procedures=work_order_operation_procedures,
            asset=asset,
            work_order_item_statuses=work_order_item_statuses,
            supply_item_ids=supply_item_ids,
            work_order_operation_custom_fields=work_order_operation_custom_fields,
        )

        work_order_operation_motor.additional_properties = d
        return work_order_operation_motor

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

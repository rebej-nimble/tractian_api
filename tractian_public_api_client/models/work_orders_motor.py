from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_review_cycle_motor import CurrentReviewCycleMotor
    from ..models.entity_custom_field import EntityCustomField
    from ..models.identified_asset_failures import IdentifiedAssetFailures
    from ..models.total_cost import TotalCost
    from ..models.work_order_asset_motor import WorkOrderAssetMotor
    from ..models.work_order_completed_by_user import WorkOrderCompletedByUser
    from ..models.work_order_deleted_info import WorkOrderDeletedInfo
    from ..models.work_order_location_motor import WorkOrderLocationMotor
    from ..models.work_order_motor_attachment import WorkOrderMotorAttachment
    from ..models.work_order_operation_inventory import WorkOrderOperationInventory
    from ..models.work_order_operations import WorkOrderOperations
    from ..models.work_order_procedures import WorkOrderProcedures
    from ..models.work_order_timers import WorkOrderTimers
    from ..models.work_orders_elapsed_intervals_motor import (
        WorkOrdersElapsedIntervalsMotor,
    )
    from ..models.work_orders_others_costs_motor import WorkOrdersOthersCostsMotor


T = TypeVar("T", bound="WorkOrdersMotor")


@_attrs_define
class WorkOrdersMotor:
    id: str
    status: str
    number: int
    company_id: str
    updated_at: str
    created_at: str
    created_by_user_id: str
    title: Union[None, Unset, str] = UNSET
    custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    identified_asset_failures: Union[None, Unset, list["IdentifiedAssetFailures"]] = (
        UNSET
    )
    started_at: Union[None, Unset, str] = UNSET
    planning_status: Union[None, Unset, str] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    work_order_operations: Union[None, Unset, list["WorkOrderOperations"]] = UNSET
    """ Work Order Operations """
    work_order_operation_inventories: Union[
        None, Unset, list["WorkOrderOperationInventory"]
    ] = UNSET
    """ Work Order inventory items reserved """
    current_review_cycle: Union["CurrentReviewCycleMotor", None, Unset] = UNSET
    priority_id: Union[None, Unset, str] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    schedule_id: Union[None, Unset, str] = UNSET
    due_date: Union[None, Unset, str] = UNSET
    planned_start_date: Union[None, Unset, str] = UNSET
    request_id: Union[None, Unset, str] = UNSET
    elapsed_intervals: Union[Unset, list["WorkOrdersElapsedIntervalsMotor"]] = UNSET
    system_elapsed_intervals: Union[Unset, list["WorkOrdersElapsedIntervalsMotor"]] = (
        UNSET
    )
    work_order_timers: Union[Unset, list["WorkOrderTimers"]] = UNSET
    description: Union[None, Unset, str] = UNSET
    category_ids: Union[None, Unset, list[str]] = UNSET
    total_cost: Union["TotalCost", None, Unset] = UNSET
    work_order_operation_ids: Union[None, Unset, list[str]] = UNSET
    canceled_reason: Union[None, Unset, str] = UNSET
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    canceled_at: Union[None, Unset, str] = UNSET
    work_order_procedures: Union[None, Unset, list["WorkOrderProcedures"]] = UNSET
    other_costs: Union[None, Unset, list["WorkOrdersOthersCostsMotor"]] = UNSET
    location: Union["WorkOrderLocationMotor", None, Unset] = UNSET
    asset: Union["WorkOrderAssetMotor", None, Unset] = UNSET
    attachments: Union[None, Unset, list["WorkOrderMotorAttachment"]] = UNSET
    deleted: Union["WorkOrderDeletedInfo", None, Unset] = UNSET
    completed_by_user: Union["WorkOrderCompletedByUser", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.current_review_cycle_motor import CurrentReviewCycleMotor
        from ..models.total_cost import TotalCost
        from ..models.work_order_asset_motor import WorkOrderAssetMotor
        from ..models.work_order_completed_by_user import WorkOrderCompletedByUser
        from ..models.work_order_deleted_info import WorkOrderDeletedInfo
        from ..models.work_order_location_motor import WorkOrderLocationMotor

        id = self.id

        status = self.status

        number = self.number

        company_id = self.company_id

        updated_at = self.updated_at

        created_at = self.created_at

        created_by_user_id = self.created_by_user_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        custom_fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, list):
            custom_fields = []
            for custom_fields_type_0_item_data in self.custom_fields:
                custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                custom_fields.append(custom_fields_type_0_item)

        else:
            custom_fields = self.custom_fields

        identified_asset_failures: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.identified_asset_failures, Unset):
            identified_asset_failures = UNSET
        elif isinstance(self.identified_asset_failures, list):
            identified_asset_failures = []
            for (
                identified_asset_failures_type_0_item_data
            ) in self.identified_asset_failures:
                identified_asset_failures_type_0_item = (
                    identified_asset_failures_type_0_item_data.to_dict()
                )
                identified_asset_failures.append(identified_asset_failures_type_0_item)

        else:
            identified_asset_failures = self.identified_asset_failures

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        planning_status: Union[None, Unset, str]
        if isinstance(self.planning_status, Unset):
            planning_status = UNSET
        else:
            planning_status = self.planning_status

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        work_order_operations: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.work_order_operations, Unset):
            work_order_operations = UNSET
        elif isinstance(self.work_order_operations, list):
            work_order_operations = []
            for work_order_operations_type_0_item_data in self.work_order_operations:
                work_order_operations_type_0_item = (
                    work_order_operations_type_0_item_data.to_dict()
                )
                work_order_operations.append(work_order_operations_type_0_item)

        else:
            work_order_operations = self.work_order_operations

        work_order_operation_inventories: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.work_order_operation_inventories, Unset):
            work_order_operation_inventories = UNSET
        elif isinstance(self.work_order_operation_inventories, list):
            work_order_operation_inventories = []
            for (
                work_order_operation_inventories_type_0_item_data
            ) in self.work_order_operation_inventories:
                work_order_operation_inventories_type_0_item = (
                    work_order_operation_inventories_type_0_item_data.to_dict()
                )
                work_order_operation_inventories.append(
                    work_order_operation_inventories_type_0_item
                )

        else:
            work_order_operation_inventories = self.work_order_operation_inventories

        current_review_cycle: Union[None, Unset, dict[str, Any]]
        if isinstance(self.current_review_cycle, Unset):
            current_review_cycle = UNSET
        elif isinstance(self.current_review_cycle, CurrentReviewCycleMotor):
            current_review_cycle = self.current_review_cycle.to_dict()
        else:
            current_review_cycle = self.current_review_cycle

        priority_id: Union[None, Unset, str]
        if isinstance(self.priority_id, Unset):
            priority_id = UNSET
        else:
            priority_id = self.priority_id

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        schedule_id: Union[None, Unset, str]
        if isinstance(self.schedule_id, Unset):
            schedule_id = UNSET
        else:
            schedule_id = self.schedule_id

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        planned_start_date: Union[None, Unset, str]
        if isinstance(self.planned_start_date, Unset):
            planned_start_date = UNSET
        else:
            planned_start_date = self.planned_start_date

        request_id: Union[None, Unset, str]
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        elapsed_intervals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.elapsed_intervals, Unset):
            elapsed_intervals = []
            for elapsed_intervals_item_data in self.elapsed_intervals:
                elapsed_intervals_item = elapsed_intervals_item_data.to_dict()
                elapsed_intervals.append(elapsed_intervals_item)

        system_elapsed_intervals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.system_elapsed_intervals, Unset):
            system_elapsed_intervals = []
            for system_elapsed_intervals_item_data in self.system_elapsed_intervals:
                system_elapsed_intervals_item = (
                    system_elapsed_intervals_item_data.to_dict()
                )
                system_elapsed_intervals.append(system_elapsed_intervals_item)

        work_order_timers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.work_order_timers, Unset):
            work_order_timers = []
            for work_order_timers_item_data in self.work_order_timers:
                work_order_timers_item = work_order_timers_item_data.to_dict()
                work_order_timers.append(work_order_timers_item)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        category_ids: Union[None, Unset, list[str]]
        if isinstance(self.category_ids, Unset):
            category_ids = UNSET
        elif isinstance(self.category_ids, list):
            category_ids = self.category_ids

        else:
            category_ids = self.category_ids

        total_cost: Union[None, Unset, dict[str, Any]]
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        elif isinstance(self.total_cost, TotalCost):
            total_cost = self.total_cost.to_dict()
        else:
            total_cost = self.total_cost

        work_order_operation_ids: Union[None, Unset, list[str]]
        if isinstance(self.work_order_operation_ids, Unset):
            work_order_operation_ids = UNSET
        elif isinstance(self.work_order_operation_ids, list):
            work_order_operation_ids = self.work_order_operation_ids

        else:
            work_order_operation_ids = self.work_order_operation_ids

        canceled_reason: Union[None, Unset, str]
        if isinstance(self.canceled_reason, Unset):
            canceled_reason = UNSET
        else:
            canceled_reason = self.canceled_reason

        canceled_by_user_id: Union[None, Unset, str]
        if isinstance(self.canceled_by_user_id, Unset):
            canceled_by_user_id = UNSET
        else:
            canceled_by_user_id = self.canceled_by_user_id

        canceled_at: Union[None, Unset, str]
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = self.canceled_at

        work_order_procedures: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.work_order_procedures, Unset):
            work_order_procedures = UNSET
        elif isinstance(self.work_order_procedures, list):
            work_order_procedures = []
            for work_order_procedures_type_0_item_data in self.work_order_procedures:
                work_order_procedures_type_0_item = (
                    work_order_procedures_type_0_item_data.to_dict()
                )
                work_order_procedures.append(work_order_procedures_type_0_item)

        else:
            work_order_procedures = self.work_order_procedures

        other_costs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.other_costs, Unset):
            other_costs = UNSET
        elif isinstance(self.other_costs, list):
            other_costs = []
            for other_costs_type_0_item_data in self.other_costs:
                other_costs_type_0_item = other_costs_type_0_item_data.to_dict()
                other_costs.append(other_costs_type_0_item)

        else:
            other_costs = self.other_costs

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, WorkOrderLocationMotor):
            location = self.location.to_dict()
        else:
            location = self.location

        asset: Union[None, Unset, dict[str, Any]]
        if isinstance(self.asset, Unset):
            asset = UNSET
        elif isinstance(self.asset, WorkOrderAssetMotor):
            asset = self.asset.to_dict()
        else:
            asset = self.asset

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

        deleted: Union[None, Unset, dict[str, Any]]
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, WorkOrderDeletedInfo):
            deleted = self.deleted.to_dict()
        else:
            deleted = self.deleted

        completed_by_user: Union[None, Unset, dict[str, Any]]
        if isinstance(self.completed_by_user, Unset):
            completed_by_user = UNSET
        elif isinstance(self.completed_by_user, WorkOrderCompletedByUser):
            completed_by_user = self.completed_by_user.to_dict()
        else:
            completed_by_user = self.completed_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "number": number,
                "companyId": company_id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "createdByUserId": created_by_user_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if identified_asset_failures is not UNSET:
            field_dict["identifiedAssetFailures"] = identified_asset_failures
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if planning_status is not UNSET:
            field_dict["planningStatus"] = planning_status
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if work_order_operations is not UNSET:
            field_dict["workOrderOperations"] = work_order_operations
        if work_order_operation_inventories is not UNSET:
            field_dict["workOrderOperationInventories"] = (
                work_order_operation_inventories
            )
        if current_review_cycle is not UNSET:
            field_dict["currentReviewCycle"] = current_review_cycle
        if priority_id is not UNSET:
            field_dict["priorityId"] = priority_id
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if schedule_id is not UNSET:
            field_dict["scheduleId"] = schedule_id
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if planned_start_date is not UNSET:
            field_dict["plannedStartDate"] = planned_start_date
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if elapsed_intervals is not UNSET:
            field_dict["elapsedIntervals"] = elapsed_intervals
        if system_elapsed_intervals is not UNSET:
            field_dict["systemElapsedIntervals"] = system_elapsed_intervals
        if work_order_timers is not UNSET:
            field_dict["workOrderTimers"] = work_order_timers
        if description is not UNSET:
            field_dict["description"] = description
        if category_ids is not UNSET:
            field_dict["categoryIds"] = category_ids
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if work_order_operation_ids is not UNSET:
            field_dict["workOrderOperationIds"] = work_order_operation_ids
        if canceled_reason is not UNSET:
            field_dict["canceledReason"] = canceled_reason
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if work_order_procedures is not UNSET:
            field_dict["workOrderProcedures"] = work_order_procedures
        if other_costs is not UNSET:
            field_dict["otherCosts"] = other_costs
        if location is not UNSET:
            field_dict["location"] = location
        if asset is not UNSET:
            field_dict["asset"] = asset
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if completed_by_user is not UNSET:
            field_dict["completedByUser"] = completed_by_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_review_cycle_motor import CurrentReviewCycleMotor
        from ..models.entity_custom_field import EntityCustomField
        from ..models.identified_asset_failures import IdentifiedAssetFailures
        from ..models.total_cost import TotalCost
        from ..models.work_order_asset_motor import WorkOrderAssetMotor
        from ..models.work_order_completed_by_user import WorkOrderCompletedByUser
        from ..models.work_order_deleted_info import WorkOrderDeletedInfo
        from ..models.work_order_location_motor import WorkOrderLocationMotor
        from ..models.work_order_motor_attachment import WorkOrderMotorAttachment
        from ..models.work_order_operation_inventory import WorkOrderOperationInventory
        from ..models.work_order_operations import WorkOrderOperations
        from ..models.work_order_procedures import WorkOrderProcedures
        from ..models.work_order_timers import WorkOrderTimers
        from ..models.work_orders_elapsed_intervals_motor import (
            WorkOrdersElapsedIntervalsMotor,
        )
        from ..models.work_orders_others_costs_motor import WorkOrdersOthersCostsMotor

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        number = d.pop("number")

        company_id = d.pop("companyId")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        created_by_user_id = d.pop("createdByUserId")

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_custom_fields(
            data: object,
        ) -> Union[None, Unset, list["EntityCustomField"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_fields_type_0 = []
                _custom_fields_type_0 = data
                for custom_fields_type_0_item_data in _custom_fields_type_0:
                    custom_fields_type_0_item = EntityCustomField.from_dict(
                        custom_fields_type_0_item_data
                    )

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EntityCustomField"]], data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))

        def _parse_identified_asset_failures(
            data: object,
        ) -> Union[None, Unset, list["IdentifiedAssetFailures"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identified_asset_failures_type_0 = []
                _identified_asset_failures_type_0 = data
                for (
                    identified_asset_failures_type_0_item_data
                ) in _identified_asset_failures_type_0:
                    identified_asset_failures_type_0_item = (
                        IdentifiedAssetFailures.from_dict(
                            identified_asset_failures_type_0_item_data
                        )
                    )

                    identified_asset_failures_type_0.append(
                        identified_asset_failures_type_0_item
                    )

                return identified_asset_failures_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IdentifiedAssetFailures"]], data)

        identified_asset_failures = _parse_identified_asset_failures(
            d.pop("identifiedAssetFailures", UNSET)
        )

        def _parse_started_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        def _parse_planning_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        planning_status = _parse_planning_status(d.pop("planningStatus", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_work_order_operations(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderOperations"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operations_type_0 = []
                _work_order_operations_type_0 = data
                for (
                    work_order_operations_type_0_item_data
                ) in _work_order_operations_type_0:
                    work_order_operations_type_0_item = WorkOrderOperations.from_dict(
                        work_order_operations_type_0_item_data
                    )

                    work_order_operations_type_0.append(
                        work_order_operations_type_0_item
                    )

                return work_order_operations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrderOperations"]], data)

        work_order_operations = _parse_work_order_operations(
            d.pop("workOrderOperations", UNSET)
        )

        def _parse_work_order_operation_inventories(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderOperationInventory"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_inventories_type_0 = []
                _work_order_operation_inventories_type_0 = data
                for (
                    work_order_operation_inventories_type_0_item_data
                ) in _work_order_operation_inventories_type_0:
                    work_order_operation_inventories_type_0_item = (
                        WorkOrderOperationInventory.from_dict(
                            work_order_operation_inventories_type_0_item_data
                        )
                    )

                    work_order_operation_inventories_type_0.append(
                        work_order_operation_inventories_type_0_item
                    )

                return work_order_operation_inventories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrderOperationInventory"]], data)

        work_order_operation_inventories = _parse_work_order_operation_inventories(
            d.pop("workOrderOperationInventories", UNSET)
        )

        def _parse_current_review_cycle(
            data: object,
        ) -> Union["CurrentReviewCycleMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_review_cycle_type_0 = CurrentReviewCycleMotor.from_dict(data)

                return current_review_cycle_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CurrentReviewCycleMotor", None, Unset], data)

        current_review_cycle = _parse_current_review_cycle(
            d.pop("currentReviewCycle", UNSET)
        )

        def _parse_priority_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        priority_id = _parse_priority_id(d.pop("priorityId", UNSET))

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

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_schedule_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schedule_id = _parse_schedule_id(d.pop("scheduleId", UNSET))

        def _parse_due_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))

        def _parse_planned_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        planned_start_date = _parse_planned_start_date(d.pop("plannedStartDate", UNSET))

        def _parse_request_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))

        elapsed_intervals = []
        _elapsed_intervals = d.pop("elapsedIntervals", UNSET)
        for elapsed_intervals_item_data in _elapsed_intervals or []:
            elapsed_intervals_item = WorkOrdersElapsedIntervalsMotor.from_dict(
                elapsed_intervals_item_data
            )

            elapsed_intervals.append(elapsed_intervals_item)

        system_elapsed_intervals = []
        _system_elapsed_intervals = d.pop("systemElapsedIntervals", UNSET)
        for system_elapsed_intervals_item_data in _system_elapsed_intervals or []:
            system_elapsed_intervals_item = WorkOrdersElapsedIntervalsMotor.from_dict(
                system_elapsed_intervals_item_data
            )

            system_elapsed_intervals.append(system_elapsed_intervals_item)

        work_order_timers = []
        _work_order_timers = d.pop("workOrderTimers", UNSET)
        for work_order_timers_item_data in _work_order_timers or []:
            work_order_timers_item = WorkOrderTimers.from_dict(
                work_order_timers_item_data
            )

            work_order_timers.append(work_order_timers_item)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_category_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                category_ids_type_0 = cast(list[str], data)

                return category_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        category_ids = _parse_category_ids(d.pop("categoryIds", UNSET))

        def _parse_total_cost(data: object) -> Union["TotalCost", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                total_cost_type_0 = TotalCost.from_dict(data)

                return total_cost_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TotalCost", None, Unset], data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        def _parse_work_order_operation_ids(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_operation_ids_type_0 = cast(list[str], data)

                return work_order_operation_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        work_order_operation_ids = _parse_work_order_operation_ids(
            d.pop("workOrderOperationIds", UNSET)
        )

        def _parse_canceled_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_reason = _parse_canceled_reason(d.pop("canceledReason", UNSET))

        def _parse_canceled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_by_user_id = _parse_canceled_by_user_id(
            d.pop("canceledByUserId", UNSET)
        )

        def _parse_canceled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))

        def _parse_work_order_procedures(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderProcedures"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_order_procedures_type_0 = []
                _work_order_procedures_type_0 = data
                for (
                    work_order_procedures_type_0_item_data
                ) in _work_order_procedures_type_0:
                    work_order_procedures_type_0_item = WorkOrderProcedures.from_dict(
                        work_order_procedures_type_0_item_data
                    )

                    work_order_procedures_type_0.append(
                        work_order_procedures_type_0_item
                    )

                return work_order_procedures_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrderProcedures"]], data)

        work_order_procedures = _parse_work_order_procedures(
            d.pop("workOrderProcedures", UNSET)
        )

        def _parse_other_costs(
            data: object,
        ) -> Union[None, Unset, list["WorkOrdersOthersCostsMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                other_costs_type_0 = []
                _other_costs_type_0 = data
                for other_costs_type_0_item_data in _other_costs_type_0:
                    other_costs_type_0_item = WorkOrdersOthersCostsMotor.from_dict(
                        other_costs_type_0_item_data
                    )

                    other_costs_type_0.append(other_costs_type_0_item)

                return other_costs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrdersOthersCostsMotor"]], data)

        other_costs = _parse_other_costs(d.pop("otherCosts", UNSET))

        def _parse_location(
            data: object,
        ) -> Union["WorkOrderLocationMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = WorkOrderLocationMotor.from_dict(data)

                return location_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkOrderLocationMotor", None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_asset(data: object) -> Union["WorkOrderAssetMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_type_0 = WorkOrderAssetMotor.from_dict(data)

                return asset_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkOrderAssetMotor", None, Unset], data)

        asset = _parse_asset(d.pop("asset", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderMotorAttachment"]]:
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
                    attachments_type_0_item = WorkOrderMotorAttachment.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WorkOrderMotorAttachment"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_deleted(data: object) -> Union["WorkOrderDeletedInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_type_0 = WorkOrderDeletedInfo.from_dict(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkOrderDeletedInfo", None, Unset], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_completed_by_user(
            data: object,
        ) -> Union["WorkOrderCompletedByUser", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                completed_by_user_type_0 = WorkOrderCompletedByUser.from_dict(data)

                return completed_by_user_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WorkOrderCompletedByUser", None, Unset], data)

        completed_by_user = _parse_completed_by_user(d.pop("completedByUser", UNSET))

        work_orders_motor = cls(
            id=id,
            status=status,
            number=number,
            company_id=company_id,
            updated_at=updated_at,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            title=title,
            custom_fields=custom_fields,
            identified_asset_failures=identified_asset_failures,
            started_at=started_at,
            planning_status=planning_status,
            asset_id=asset_id,
            work_order_operations=work_order_operations,
            work_order_operation_inventories=work_order_operation_inventories,
            current_review_cycle=current_review_cycle,
            priority_id=priority_id,
            assigned_team_ids=assigned_team_ids,
            location_id=location_id,
            schedule_id=schedule_id,
            due_date=due_date,
            planned_start_date=planned_start_date,
            request_id=request_id,
            elapsed_intervals=elapsed_intervals,
            system_elapsed_intervals=system_elapsed_intervals,
            work_order_timers=work_order_timers,
            description=description,
            category_ids=category_ids,
            total_cost=total_cost,
            work_order_operation_ids=work_order_operation_ids,
            canceled_reason=canceled_reason,
            canceled_by_user_id=canceled_by_user_id,
            canceled_at=canceled_at,
            work_order_procedures=work_order_procedures,
            other_costs=other_costs,
            location=location,
            asset=asset,
            attachments=attachments,
            deleted=deleted,
            completed_by_user=completed_by_user,
        )

        work_orders_motor.additional_properties = d
        return work_orders_motor

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

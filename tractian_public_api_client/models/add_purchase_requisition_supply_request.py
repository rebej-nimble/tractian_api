from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_requisition_supply_priority import (
    PurchaseRequisitionSupplyPriority,
    check_purchase_requisition_supply_priority,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_inventory_item_supply import AttachmentInventoryItemSupply
    from ..models.entity_custom_field import EntityCustomField


T = TypeVar("T", bound="AddPurchaseRequisitionSupplyRequest")


@_attrs_define
class AddPurchaseRequisitionSupplyRequest:
    company_id: str
    created_at: Union[None, str]
    updated_at: Union[None, str]
    created_by_user_id: Union[None, str]
    updated_by_user_id: Union[None, str]
    work_order_id: Union[None, str]
    identifier_code: Union[None, str]
    external_id: Union[None, str]
    priority: Union[None, PurchaseRequisitionSupplyPriority]
    notes: Union[None, str]
    assigned_user_ids: Union[None, list[str]]
    assigned_team_ids: Union[None, list[str]]
    system_created: Union[None, bool]
    reject_reason_notes: Union[None, str]
    reject_reason_id: Union[None, str]
    reviewed_at: Union[None, str]
    attachments: Union[None, list["AttachmentInventoryItemSupply"]]
    custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        created_at: Union[None, str]
        created_at = self.created_at

        updated_at: Union[None, str]
        updated_at = self.updated_at

        created_by_user_id: Union[None, str]
        created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, str]
        updated_by_user_id = self.updated_by_user_id

        work_order_id: Union[None, str]
        work_order_id = self.work_order_id

        identifier_code: Union[None, str]
        identifier_code = self.identifier_code

        external_id: Union[None, str]
        external_id = self.external_id

        priority: Union[None, str]
        if isinstance(self.priority, str):
            priority = self.priority
        else:
            priority = self.priority

        notes: Union[None, str]
        notes = self.notes

        assigned_user_ids: Union[None, list[str]]
        if isinstance(self.assigned_user_ids, list):
            assigned_user_ids = self.assigned_user_ids

        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, list[str]]
        if isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        system_created: Union[None, bool]
        system_created = self.system_created

        reject_reason_notes: Union[None, str]
        reject_reason_notes = self.reject_reason_notes

        reject_reason_id: Union[None, str]
        reject_reason_id = self.reject_reason_id

        reviewed_at: Union[None, str]
        reviewed_at = self.reviewed_at

        attachments: Union[None, list[dict[str, Any]]]
        if isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
                "workOrderId": work_order_id,
                "identifierCode": identifier_code,
                "externalId": external_id,
                "priority": priority,
                "notes": notes,
                "assignedUserIds": assigned_user_ids,
                "assignedTeamIds": assigned_team_ids,
                "systemCreated": system_created,
                "rejectReasonNotes": reject_reason_notes,
                "rejectReasonId": reject_reason_id,
                "reviewedAt": reviewed_at,
                "attachments": attachments,
            }
        )
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_inventory_item_supply import (
            AttachmentInventoryItemSupply,
        )
        from ..models.entity_custom_field import EntityCustomField

        d = dict(src_dict)
        company_id = d.pop("companyId")

        def _parse_created_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_at = _parse_created_at(d.pop("createdAt"))

        def _parse_updated_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId"))

        def _parse_updated_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId"))

        def _parse_work_order_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId"))

        def _parse_identifier_code(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode"))

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("externalId"))

        def _parse_priority(
            data: object,
        ) -> Union[None, PurchaseRequisitionSupplyPriority]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = check_purchase_requisition_supply_priority(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PurchaseRequisitionSupplyPriority], data)

        priority = _parse_priority(d.pop("priority"))

        def _parse_notes(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        notes = _parse_notes(d.pop("notes"))

        def _parse_assigned_user_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_user_ids_type_0 = cast(list[str], data)

                return assigned_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds"))

        def _parse_assigned_team_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds"))

        def _parse_system_created(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        system_created = _parse_system_created(d.pop("systemCreated"))

        def _parse_reject_reason_notes(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reject_reason_notes = _parse_reject_reason_notes(d.pop("rejectReasonNotes"))

        def _parse_reject_reason_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reject_reason_id = _parse_reject_reason_id(d.pop("rejectReasonId"))

        def _parse_reviewed_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewedAt"))

        def _parse_attachments(
            data: object,
        ) -> Union[None, list["AttachmentInventoryItemSupply"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = AttachmentInventoryItemSupply.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["AttachmentInventoryItemSupply"]], data)

        attachments = _parse_attachments(d.pop("attachments"))

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

        add_purchase_requisition_supply_request = cls(
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            work_order_id=work_order_id,
            identifier_code=identifier_code,
            external_id=external_id,
            priority=priority,
            notes=notes,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            system_created=system_created,
            reject_reason_notes=reject_reason_notes,
            reject_reason_id=reject_reason_id,
            reviewed_at=reviewed_at,
            attachments=attachments,
            custom_fields=custom_fields,
        )

        add_purchase_requisition_supply_request.additional_properties = d
        return add_purchase_requisition_supply_request

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

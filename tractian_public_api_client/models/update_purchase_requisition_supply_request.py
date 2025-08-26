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


T = TypeVar("T", bound="UpdatePurchaseRequisitionSupplyRequest")


@_attrs_define
class UpdatePurchaseRequisitionSupplyRequest:
    id: str
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    work_order_id: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    priority: Union[None, PurchaseRequisitionSupplyPriority, Unset] = UNSET
    notes: Union[None, Unset, str] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    system_created: Union[None, Unset, bool] = UNSET
    reject_reason_notes: Union[None, Unset, str] = UNSET
    reject_reason_id: Union[None, Unset, str] = UNSET
    reviewed_at: Union[None, Unset, str] = UNSET
    attachments: Union[None, Unset, list["AttachmentInventoryItemSupply"]] = UNSET
    custom_fields: Union[None, Unset, list["EntityCustomField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, str):
            priority = self.priority
        else:
            priority = self.priority

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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

        system_created: Union[None, Unset, bool]
        if isinstance(self.system_created, Unset):
            system_created = UNSET
        else:
            system_created = self.system_created

        reject_reason_notes: Union[None, Unset, str]
        if isinstance(self.reject_reason_notes, Unset):
            reject_reason_notes = UNSET
        else:
            reject_reason_notes = self.reject_reason_notes

        reject_reason_id: Union[None, Unset, str]
        if isinstance(self.reject_reason_id, Unset):
            reject_reason_id = UNSET
        else:
            reject_reason_id = self.reject_reason_id

        reviewed_at: Union[None, Unset, str]
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = self.reviewed_at

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
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if notes is not UNSET:
            field_dict["notes"] = notes
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if system_created is not UNSET:
            field_dict["systemCreated"] = system_created
        if reject_reason_notes is not UNSET:
            field_dict["rejectReasonNotes"] = reject_reason_notes
        if reject_reason_id is not UNSET:
            field_dict["rejectReasonId"] = reject_reason_id
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
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

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_priority(
            data: object,
        ) -> Union[None, PurchaseRequisitionSupplyPriority, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = check_purchase_requisition_supply_priority(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PurchaseRequisitionSupplyPriority, Unset], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

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

        def _parse_system_created(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        system_created = _parse_system_created(d.pop("systemCreated", UNSET))

        def _parse_reject_reason_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reject_reason_notes = _parse_reject_reason_notes(
            d.pop("rejectReasonNotes", UNSET)
        )

        def _parse_reject_reason_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reject_reason_id = _parse_reject_reason_id(d.pop("rejectReasonId", UNSET))

        def _parse_reviewed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewedAt", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["AttachmentInventoryItemSupply"]]:
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
                    attachments_type_0_item = AttachmentInventoryItemSupply.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AttachmentInventoryItemSupply"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

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

        update_purchase_requisition_supply_request = cls(
            id=id,
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

        update_purchase_requisition_supply_request.additional_properties = d
        return update_purchase_requisition_supply_request

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

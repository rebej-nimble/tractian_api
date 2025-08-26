from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiSupplyRejectPurchaseRequestAction")


@_attrs_define
class ApiSupplyRejectPurchaseRequestAction:
    purchase_requisition_ids: list[str]
    company_id: str
    reject_reason_id: str
    reject_reason_notes: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_requisition_ids = self.purchase_requisition_ids

        company_id = self.company_id

        reject_reason_id = self.reject_reason_id

        reject_reason_notes = self.reject_reason_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purchaseRequisitionIds": purchase_requisition_ids,
                "companyId": company_id,
                "rejectReasonId": reject_reason_id,
                "rejectReasonNotes": reject_reason_notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purchase_requisition_ids = cast(list[str], d.pop("purchaseRequisitionIds"))

        company_id = d.pop("companyId")

        reject_reason_id = d.pop("rejectReasonId")

        reject_reason_notes = d.pop("rejectReasonNotes")

        api_supply_reject_purchase_request_action = cls(
            purchase_requisition_ids=purchase_requisition_ids,
            company_id=company_id,
            reject_reason_id=reject_reason_id,
            reject_reason_notes=reject_reason_notes,
        )

        api_supply_reject_purchase_request_action.additional_properties = d
        return api_supply_reject_purchase_request_action

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

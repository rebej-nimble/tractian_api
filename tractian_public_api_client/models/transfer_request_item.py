from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_supply_transfer_request_item_status import (
    ApiSupplyTransferRequestItemStatus,
    check_api_supply_transfer_request_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferRequestItem")


@_attrs_define
class TransferRequestItem:
    id: str
    number: int
    created_at: str
    updated_at: str
    created_by_user_id: str
    updated_by_user_id: str
    company_id: str
    item_id: str
    from_item_storage_id: str
    to_item_storage_id: str
    transfer_request_id: str
    transfer_request_number: int
    status: ApiSupplyTransferRequestItemStatus
    quantity: float
    external_id: Union[None, Unset, str] = UNSET
    cost_center_id: Union[None, Unset, str] = UNSET
    work_order_item_id: Union[None, Unset, str] = UNSET
    work_order_operation_id: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        created_at = self.created_at

        updated_at = self.updated_at

        created_by_user_id = self.created_by_user_id

        updated_by_user_id = self.updated_by_user_id

        company_id = self.company_id

        item_id = self.item_id

        from_item_storage_id = self.from_item_storage_id

        to_item_storage_id = self.to_item_storage_id

        transfer_request_id = self.transfer_request_id

        transfer_request_number = self.transfer_request_number

        status: str = self.status

        quantity = self.quantity

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        cost_center_id: Union[None, Unset, str]
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        work_order_item_id: Union[None, Unset, str]
        if isinstance(self.work_order_item_id, Unset):
            work_order_item_id = UNSET
        else:
            work_order_item_id = self.work_order_item_id

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
                "companyId": company_id,
                "itemId": item_id,
                "fromItemStorageId": from_item_storage_id,
                "toItemStorageId": to_item_storage_id,
                "transferRequestId": transfer_request_id,
                "transferRequestNumber": transfer_request_number,
                "status": status,
                "quantity": quantity,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if work_order_item_id is not UNSET:
            field_dict["workOrderItemId"] = work_order_item_id
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        created_by_user_id = d.pop("createdByUserId")

        updated_by_user_id = d.pop("updatedByUserId")

        company_id = d.pop("companyId")

        item_id = d.pop("itemId")

        from_item_storage_id = d.pop("fromItemStorageId")

        to_item_storage_id = d.pop("toItemStorageId")

        transfer_request_id = d.pop("transferRequestId")

        transfer_request_number = d.pop("transferRequestNumber")

        status = check_api_supply_transfer_request_item_status(d.pop("status"))

        quantity = d.pop("quantity")

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_cost_center_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        def _parse_work_order_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_item_id = _parse_work_order_item_id(d.pop("workOrderItemId", UNSET))

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        transfer_request_item = cls(
            id=id,
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            company_id=company_id,
            item_id=item_id,
            from_item_storage_id=from_item_storage_id,
            to_item_storage_id=to_item_storage_id,
            transfer_request_id=transfer_request_id,
            transfer_request_number=transfer_request_number,
            status=status,
            quantity=quantity,
            external_id=external_id,
            cost_center_id=cost_center_id,
            work_order_item_id=work_order_item_id,
            work_order_operation_id=work_order_operation_id,
            notes=notes,
        )

        transfer_request_item.additional_properties = d
        return transfer_request_item

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

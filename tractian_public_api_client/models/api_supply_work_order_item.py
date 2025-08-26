from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyWorkOrderItem")


@_attrs_define
class ApiSupplyWorkOrderItem:
    id: Union[None, Unset, str] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    company_id: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    item_id: Union[None, Unset, str] = UNSET
    item_storage_id: Union[None, Unset, str] = UNSET
    work_order_id: Union[None, Unset, str] = UNSET
    work_order_operation_id: Union[None, Unset, str] = UNSET
    purchase_requisition_item_id: Union[None, Unset, str] = UNSET
    cost_center_id: Union[None, Unset, str] = UNSET
    item_reservation_id: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
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

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        item_storage_id: Union[None, Unset, str]
        if isinstance(self.item_storage_id, Unset):
            item_storage_id = UNSET
        else:
            item_storage_id = self.item_storage_id

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        purchase_requisition_item_id: Union[None, Unset, str]
        if isinstance(self.purchase_requisition_item_id, Unset):
            purchase_requisition_item_id = UNSET
        else:
            purchase_requisition_item_id = self.purchase_requisition_item_id

        cost_center_id: Union[None, Unset, str]
        if isinstance(self.cost_center_id, Unset):
            cost_center_id = UNSET
        else:
            cost_center_id = self.cost_center_id

        item_reservation_id: Union[None, Unset, str]
        if isinstance(self.item_reservation_id, Unset):
            item_reservation_id = UNSET
        else:
            item_reservation_id = self.item_reservation_id

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if item_storage_id is not UNSET:
            field_dict["itemStorageId"] = item_storage_id
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if purchase_requisition_item_id is not UNSET:
            field_dict["purchaseRequisitionItemId"] = purchase_requisition_item_id
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if item_reservation_id is not UNSET:
            field_dict["itemReservationId"] = item_reservation_id
        if status is not UNSET:
            field_dict["status"] = status
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("itemId", UNSET))

        def _parse_item_storage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_storage_id = _parse_item_storage_id(d.pop("itemStorageId", UNSET))

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_purchase_requisition_item_id(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_requisition_item_id = _parse_purchase_requisition_item_id(
            d.pop("purchaseRequisitionItemId", UNSET)
        )

        def _parse_cost_center_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_id = _parse_cost_center_id(d.pop("costCenterId", UNSET))

        def _parse_item_reservation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_reservation_id = _parse_item_reservation_id(
            d.pop("itemReservationId", UNSET)
        )

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        api_supply_work_order_item = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            company_id=company_id,
            identifier_code=identifier_code,
            item_id=item_id,
            item_storage_id=item_storage_id,
            work_order_id=work_order_id,
            work_order_operation_id=work_order_operation_id,
            purchase_requisition_item_id=purchase_requisition_item_id,
            cost_center_id=cost_center_id,
            item_reservation_id=item_reservation_id,
            status=status,
            quantity=quantity,
        )

        api_supply_work_order_item.additional_properties = d
        return api_supply_work_order_item

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

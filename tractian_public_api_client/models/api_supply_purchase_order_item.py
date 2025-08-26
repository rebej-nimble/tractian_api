from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyPurchaseOrderItem")


@_attrs_define
class ApiSupplyPurchaseOrderItem:
    id: str
    status: str
    item_id: str
    cost_center_id: str
    purchase_order_id: str
    negotiated_unit_price: float
    company_id: str
    created_at: str
    updated_at: str
    purchase_order_number: int
    number: int
    pending_quantity: float
    purchased_quantity: float
    created_by_user_id: str
    updated_by_user_id: str
    name: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    item_storage_id: Union[None, Unset, str] = UNSET
    purchase_requisition_number: Union[None, Unset, int] = UNSET
    purchase_requisition_item_number: Union[None, Unset, int] = UNSET
    need_date: Union[None, Unset, str] = UNSET
    estimated_unit_price: Union[None, Unset, float] = UNSET
    entry_unit_price: Union[None, Unset, float] = UNSET
    work_order_operation_id: Union[None, Unset, str] = UNSET
    created_by_user_oid: Union[None, Unset, str] = UNSET
    updated_by_user_oid: Union[None, Unset, str] = UNSET
    canceled_at: Union[None, Unset, str] = UNSET
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    work_order_item_id: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    purchase_requisition_id: Union[None, Unset, str] = UNSET
    purchase_requisition_identifier_code: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        item_id = self.item_id

        cost_center_id = self.cost_center_id

        purchase_order_id = self.purchase_order_id

        negotiated_unit_price = self.negotiated_unit_price

        company_id = self.company_id

        created_at = self.created_at

        updated_at = self.updated_at

        purchase_order_number = self.purchase_order_number

        number = self.number

        pending_quantity = self.pending_quantity

        purchased_quantity = self.purchased_quantity

        created_by_user_id = self.created_by_user_id

        updated_by_user_id = self.updated_by_user_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        item_storage_id: Union[None, Unset, str]
        if isinstance(self.item_storage_id, Unset):
            item_storage_id = UNSET
        else:
            item_storage_id = self.item_storage_id

        purchase_requisition_number: Union[None, Unset, int]
        if isinstance(self.purchase_requisition_number, Unset):
            purchase_requisition_number = UNSET
        else:
            purchase_requisition_number = self.purchase_requisition_number

        purchase_requisition_item_number: Union[None, Unset, int]
        if isinstance(self.purchase_requisition_item_number, Unset):
            purchase_requisition_item_number = UNSET
        else:
            purchase_requisition_item_number = self.purchase_requisition_item_number

        need_date: Union[None, Unset, str]
        if isinstance(self.need_date, Unset):
            need_date = UNSET
        else:
            need_date = self.need_date

        estimated_unit_price: Union[None, Unset, float]
        if isinstance(self.estimated_unit_price, Unset):
            estimated_unit_price = UNSET
        else:
            estimated_unit_price = self.estimated_unit_price

        entry_unit_price: Union[None, Unset, float]
        if isinstance(self.entry_unit_price, Unset):
            entry_unit_price = UNSET
        else:
            entry_unit_price = self.entry_unit_price

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        created_by_user_oid: Union[None, Unset, str]
        if isinstance(self.created_by_user_oid, Unset):
            created_by_user_oid = UNSET
        else:
            created_by_user_oid = self.created_by_user_oid

        updated_by_user_oid: Union[None, Unset, str]
        if isinstance(self.updated_by_user_oid, Unset):
            updated_by_user_oid = UNSET
        else:
            updated_by_user_oid = self.updated_by_user_oid

        canceled_at: Union[None, Unset, str]
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = self.canceled_at

        canceled_by_user_id: Union[None, Unset, str]
        if isinstance(self.canceled_by_user_id, Unset):
            canceled_by_user_id = UNSET
        else:
            canceled_by_user_id = self.canceled_by_user_id

        work_order_item_id: Union[None, Unset, str]
        if isinstance(self.work_order_item_id, Unset):
            work_order_item_id = UNSET
        else:
            work_order_item_id = self.work_order_item_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        purchase_requisition_id: Union[None, Unset, str]
        if isinstance(self.purchase_requisition_id, Unset):
            purchase_requisition_id = UNSET
        else:
            purchase_requisition_id = self.purchase_requisition_id

        purchase_requisition_identifier_code: Union[None, Unset, str]
        if isinstance(self.purchase_requisition_identifier_code, Unset):
            purchase_requisition_identifier_code = UNSET
        else:
            purchase_requisition_identifier_code = (
                self.purchase_requisition_identifier_code
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "itemId": item_id,
                "costCenterId": cost_center_id,
                "purchaseOrderId": purchase_order_id,
                "negotiatedUnitPrice": negotiated_unit_price,
                "companyId": company_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "purchaseOrderNumber": purchase_order_number,
                "number": number,
                "pendingQuantity": pending_quantity,
                "purchasedQuantity": purchased_quantity,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if item_storage_id is not UNSET:
            field_dict["itemStorageId"] = item_storage_id
        if purchase_requisition_number is not UNSET:
            field_dict["purchaseRequisitionNumber"] = purchase_requisition_number
        if purchase_requisition_item_number is not UNSET:
            field_dict["purchaseRequisitionItemNumber"] = (
                purchase_requisition_item_number
            )
        if need_date is not UNSET:
            field_dict["needDate"] = need_date
        if estimated_unit_price is not UNSET:
            field_dict["estimatedUnitPrice"] = estimated_unit_price
        if entry_unit_price is not UNSET:
            field_dict["entryUnitPrice"] = entry_unit_price
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if created_by_user_oid is not UNSET:
            field_dict["createdByUserOid"] = created_by_user_oid
        if updated_by_user_oid is not UNSET:
            field_dict["updatedByUserOid"] = updated_by_user_oid
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if work_order_item_id is not UNSET:
            field_dict["workOrderItemId"] = work_order_item_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if purchase_requisition_id is not UNSET:
            field_dict["purchaseRequisitionId"] = purchase_requisition_id
        if purchase_requisition_identifier_code is not UNSET:
            field_dict["purchaseRequisitionIdentifierCode"] = (
                purchase_requisition_identifier_code
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        item_id = d.pop("itemId")

        cost_center_id = d.pop("costCenterId")

        purchase_order_id = d.pop("purchaseOrderId")

        negotiated_unit_price = d.pop("negotiatedUnitPrice")

        company_id = d.pop("companyId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        purchase_order_number = d.pop("purchaseOrderNumber")

        number = d.pop("number")

        pending_quantity = d.pop("pendingQuantity")

        purchased_quantity = d.pop("purchasedQuantity")

        created_by_user_id = d.pop("createdByUserId")

        updated_by_user_id = d.pop("updatedByUserId")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_item_storage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_storage_id = _parse_item_storage_id(d.pop("itemStorageId", UNSET))

        def _parse_purchase_requisition_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        purchase_requisition_number = _parse_purchase_requisition_number(
            d.pop("purchaseRequisitionNumber", UNSET)
        )

        def _parse_purchase_requisition_item_number(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        purchase_requisition_item_number = _parse_purchase_requisition_item_number(
            d.pop("purchaseRequisitionItemNumber", UNSET)
        )

        def _parse_need_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        need_date = _parse_need_date(d.pop("needDate", UNSET))

        def _parse_estimated_unit_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        estimated_unit_price = _parse_estimated_unit_price(
            d.pop("estimatedUnitPrice", UNSET)
        )

        def _parse_entry_unit_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        entry_unit_price = _parse_entry_unit_price(d.pop("entryUnitPrice", UNSET))

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_created_by_user_oid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_oid = _parse_created_by_user_oid(
            d.pop("createdByUserOid", UNSET)
        )

        def _parse_updated_by_user_oid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_oid = _parse_updated_by_user_oid(
            d.pop("updatedByUserOid", UNSET)
        )

        def _parse_canceled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))

        def _parse_canceled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_by_user_id = _parse_canceled_by_user_id(
            d.pop("canceledByUserId", UNSET)
        )

        def _parse_work_order_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_item_id = _parse_work_order_item_id(d.pop("workOrderItemId", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_purchase_requisition_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_requisition_id = _parse_purchase_requisition_id(
            d.pop("purchaseRequisitionId", UNSET)
        )

        def _parse_purchase_requisition_identifier_code(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_requisition_identifier_code = (
            _parse_purchase_requisition_identifier_code(
                d.pop("purchaseRequisitionIdentifierCode", UNSET)
            )
        )

        api_supply_purchase_order_item = cls(
            id=id,
            status=status,
            item_id=item_id,
            cost_center_id=cost_center_id,
            purchase_order_id=purchase_order_id,
            negotiated_unit_price=negotiated_unit_price,
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            purchase_order_number=purchase_order_number,
            number=number,
            pending_quantity=pending_quantity,
            purchased_quantity=purchased_quantity,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            name=name,
            quantity=quantity,
            item_storage_id=item_storage_id,
            purchase_requisition_number=purchase_requisition_number,
            purchase_requisition_item_number=purchase_requisition_item_number,
            need_date=need_date,
            estimated_unit_price=estimated_unit_price,
            entry_unit_price=entry_unit_price,
            work_order_operation_id=work_order_operation_id,
            created_by_user_oid=created_by_user_oid,
            updated_by_user_oid=updated_by_user_oid,
            canceled_at=canceled_at,
            canceled_by_user_id=canceled_by_user_id,
            work_order_item_id=work_order_item_id,
            identifier_code=identifier_code,
            purchase_requisition_id=purchase_requisition_id,
            purchase_requisition_identifier_code=purchase_requisition_identifier_code,
        )

        api_supply_purchase_order_item.additional_properties = d
        return api_supply_purchase_order_item

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

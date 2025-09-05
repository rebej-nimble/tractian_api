from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyPurchaseRequisitionItemRequest")


@_attrs_define
class ApiSupplyPurchaseRequisitionItemRequest:
    company_id: str
    """ The company id """
    cost_center_id: str
    """ The cost center id """
    requested_quantity: float
    """ The requested quantity """
    item_id: Union[None, Unset, str] = UNSET
    """ The item id """
    number: Union[None, Unset, int] = UNSET
    """ The number """
    created_at: Union[None, Unset, str] = UNSET
    """ The date when the item was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date when the item was updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id who created the item """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id who updated the item """
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id who canceled the item """
    canceled_at: Union[None, Unset, str] = UNSET
    """ The date when the item was canceled """
    identifier_code: Union[None, Unset, str] = UNSET
    """ The identifier code of the item """
    purchase_requisition_id: Union[None, Unset, str] = UNSET
    """ The purchase requisition id """
    purchase_requisition_number: Union[None, Unset, int] = UNSET
    """ The purchase requisition number """
    name: Union[None, Unset, str] = UNSET
    """ The name of the item """
    item_storage_id: Union[None, Unset, str] = UNSET
    """ The item storage id """
    suggested_supplier_ids: Union[None, Unset, list[str]] = UNSET
    """ The suggested supplier ids """
    purchase_order_id: Union[None, Unset, str] = UNSET
    """ The purchase order id """
    work_order_operation_id: Union[None, Unset, str] = UNSET
    """ The work order operation id """
    work_order_item_id: Union[None, Unset, str] = UNSET
    """ The work order item id """
    need_date: Union[None, Unset, str] = UNSET
    """ The need date """
    estimated_unit_price: Union[None, Unset, float] = UNSET
    """ The estimated unit price """
    negotiated_unit_price: Union[None, Unset, float] = UNSET
    """ The negotiated unit price """
    entry_unit_price: Union[None, Unset, float] = UNSET
    """ The entry unit price """
    pending_quantity: Union[None, Unset, float] = UNSET
    """ The pending quantity """
    status: Union[None, Unset, str] = UNSET
    """ The status of the item """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        cost_center_id = self.cost_center_id

        requested_quantity = self.requested_quantity

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

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

        purchase_requisition_number: Union[None, Unset, int]
        if isinstance(self.purchase_requisition_number, Unset):
            purchase_requisition_number = UNSET
        else:
            purchase_requisition_number = self.purchase_requisition_number

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        item_storage_id: Union[None, Unset, str]
        if isinstance(self.item_storage_id, Unset):
            item_storage_id = UNSET
        else:
            item_storage_id = self.item_storage_id

        suggested_supplier_ids: Union[None, Unset, list[str]]
        if isinstance(self.suggested_supplier_ids, Unset):
            suggested_supplier_ids = UNSET
        elif isinstance(self.suggested_supplier_ids, list):
            suggested_supplier_ids = self.suggested_supplier_ids

        else:
            suggested_supplier_ids = self.suggested_supplier_ids

        purchase_order_id: Union[None, Unset, str]
        if isinstance(self.purchase_order_id, Unset):
            purchase_order_id = UNSET
        else:
            purchase_order_id = self.purchase_order_id

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        work_order_item_id: Union[None, Unset, str]
        if isinstance(self.work_order_item_id, Unset):
            work_order_item_id = UNSET
        else:
            work_order_item_id = self.work_order_item_id

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

        negotiated_unit_price: Union[None, Unset, float]
        if isinstance(self.negotiated_unit_price, Unset):
            negotiated_unit_price = UNSET
        else:
            negotiated_unit_price = self.negotiated_unit_price

        entry_unit_price: Union[None, Unset, float]
        if isinstance(self.entry_unit_price, Unset):
            entry_unit_price = UNSET
        else:
            entry_unit_price = self.entry_unit_price

        pending_quantity: Union[None, Unset, float]
        if isinstance(self.pending_quantity, Unset):
            pending_quantity = UNSET
        else:
            pending_quantity = self.pending_quantity

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "costCenterId": cost_center_id,
                "requestedQuantity": requested_quantity,
            }
        )
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if number is not UNSET:
            field_dict["number"] = number
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if purchase_requisition_id is not UNSET:
            field_dict["purchaseRequisitionId"] = purchase_requisition_id
        if purchase_requisition_number is not UNSET:
            field_dict["purchaseRequisitionNumber"] = purchase_requisition_number
        if name is not UNSET:
            field_dict["name"] = name
        if item_storage_id is not UNSET:
            field_dict["itemStorageId"] = item_storage_id
        if suggested_supplier_ids is not UNSET:
            field_dict["suggestedSupplierIds"] = suggested_supplier_ids
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if work_order_item_id is not UNSET:
            field_dict["workOrderItemId"] = work_order_item_id
        if need_date is not UNSET:
            field_dict["needDate"] = need_date
        if estimated_unit_price is not UNSET:
            field_dict["estimatedUnitPrice"] = estimated_unit_price
        if negotiated_unit_price is not UNSET:
            field_dict["negotiatedUnitPrice"] = negotiated_unit_price
        if entry_unit_price is not UNSET:
            field_dict["entryUnitPrice"] = entry_unit_price
        if pending_quantity is not UNSET:
            field_dict["pendingQuantity"] = pending_quantity
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        cost_center_id = d.pop("costCenterId")

        requested_quantity = d.pop("requestedQuantity")

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("itemId", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

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

        def _parse_purchase_requisition_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        purchase_requisition_number = _parse_purchase_requisition_number(
            d.pop("purchaseRequisitionNumber", UNSET)
        )

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_item_storage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_storage_id = _parse_item_storage_id(d.pop("itemStorageId", UNSET))

        def _parse_suggested_supplier_ids(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggested_supplier_ids_type_0 = cast(list[str], data)

                return suggested_supplier_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        suggested_supplier_ids = _parse_suggested_supplier_ids(
            d.pop("suggestedSupplierIds", UNSET)
        )

        def _parse_purchase_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_order_id = _parse_purchase_order_id(d.pop("purchaseOrderId", UNSET))

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_work_order_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_item_id = _parse_work_order_item_id(d.pop("workOrderItemId", UNSET))

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

        def _parse_negotiated_unit_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        negotiated_unit_price = _parse_negotiated_unit_price(
            d.pop("negotiatedUnitPrice", UNSET)
        )

        def _parse_entry_unit_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        entry_unit_price = _parse_entry_unit_price(d.pop("entryUnitPrice", UNSET))

        def _parse_pending_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pending_quantity = _parse_pending_quantity(d.pop("pendingQuantity", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        api_supply_purchase_requisition_item_request = cls(
            company_id=company_id,
            cost_center_id=cost_center_id,
            requested_quantity=requested_quantity,
            item_id=item_id,
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            canceled_by_user_id=canceled_by_user_id,
            canceled_at=canceled_at,
            identifier_code=identifier_code,
            purchase_requisition_id=purchase_requisition_id,
            purchase_requisition_number=purchase_requisition_number,
            name=name,
            item_storage_id=item_storage_id,
            suggested_supplier_ids=suggested_supplier_ids,
            purchase_order_id=purchase_order_id,
            work_order_operation_id=work_order_operation_id,
            work_order_item_id=work_order_item_id,
            need_date=need_date,
            estimated_unit_price=estimated_unit_price,
            negotiated_unit_price=negotiated_unit_price,
            entry_unit_price=entry_unit_price,
            pending_quantity=pending_quantity,
            status=status,
        )

        api_supply_purchase_requisition_item_request.additional_properties = d
        return api_supply_purchase_requisition_item_request

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

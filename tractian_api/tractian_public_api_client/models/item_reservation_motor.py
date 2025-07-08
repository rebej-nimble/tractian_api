from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_reservation_motor_delete import ItemReservationMotorDelete
    from ..models.item_reservation_motor_selected_batch import (
        ItemReservationMotorSelectedBatch,
    )


T = TypeVar("T", bound="ItemReservationMotor")


@_attrs_define
class ItemReservationMotor:
    id: str
    """ Unique identifier for the reservation. """
    type_: str
    """ Type of reservation (e.g., manual, automatic). """
    status: str
    """ Current status of the reservation (e.g., pending, completed). """
    inventory_item_id: str
    """ Unique identifier of the inventory item being reserved. """
    company_id: str
    """ Unique identifier of the company making the reservation. """
    quantity: float
    """ Total quantity of the item reserved. """
    purchase_order_id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the related purchase order, if applicable. """
    sub_status: Union[None, Unset, str] = UNSET
    """ Status of the purchase order (e.g., pendingPurchase, purchased). """
    work_order_operation_inventory_id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the work order operation inventory, if applicable. """
    work_order_operation_id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the work order operation, if applicable. """
    identifier_code: Union[None, Unset, str] = UNSET
    """ Unique identifier code of the item, if applicable. This field should be used to store the customer's unique
    code for the reservation. """
    work_order_id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the work order, if applicable. """
    number: Union[None, Unset, int] = UNSET
    """ Reservation number for tracking purposes. """
    selected_batches: Union[None, Unset, list["ItemReservationMotorSelectedBatch"]] = (
        UNSET
    )
    """ List of selected batches from which the item is reserved. """
    withdrawn_at: Union[None, Unset, str] = UNSET
    """ Timestamp of when the item was withdrawn, if applicable. """
    withdrawn_by_user_id: Union[None, Unset, str] = UNSET
    """ User ID of the person who withdrew the item, if applicable. """
    created_at: Union[None, Unset, str] = UNSET
    """ Timestamp indicating when the reservation was created. """
    deleted: Union["ItemReservationMotorDelete", None, Unset] = UNSET
    """ Indicates whether the reservation has been deleted. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_reservation_motor_delete import ItemReservationMotorDelete

        id = self.id

        type_ = self.type_

        status = self.status

        inventory_item_id = self.inventory_item_id

        company_id = self.company_id

        quantity = self.quantity

        purchase_order_id: Union[None, Unset, str]
        if isinstance(self.purchase_order_id, Unset):
            purchase_order_id = UNSET
        else:
            purchase_order_id = self.purchase_order_id

        sub_status: Union[None, Unset, str]
        if isinstance(self.sub_status, Unset):
            sub_status = UNSET
        else:
            sub_status = self.sub_status

        work_order_operation_inventory_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_inventory_id, Unset):
            work_order_operation_inventory_id = UNSET
        else:
            work_order_operation_inventory_id = self.work_order_operation_inventory_id

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        selected_batches: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.selected_batches, Unset):
            selected_batches = UNSET
        elif isinstance(self.selected_batches, list):
            selected_batches = []
            for selected_batches_type_0_item_data in self.selected_batches:
                selected_batches_type_0_item = (
                    selected_batches_type_0_item_data.to_dict()
                )
                selected_batches.append(selected_batches_type_0_item)

        else:
            selected_batches = self.selected_batches

        withdrawn_at: Union[None, Unset, str]
        if isinstance(self.withdrawn_at, Unset):
            withdrawn_at = UNSET
        else:
            withdrawn_at = self.withdrawn_at

        withdrawn_by_user_id: Union[None, Unset, str]
        if isinstance(self.withdrawn_by_user_id, Unset):
            withdrawn_by_user_id = UNSET
        else:
            withdrawn_by_user_id = self.withdrawn_by_user_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        deleted: Union[None, Unset, dict[str, Any]]
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, ItemReservationMotorDelete):
            deleted = self.deleted.to_dict()
        else:
            deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "inventoryItemId": inventory_item_id,
                "companyId": company_id,
                "quantity": quantity,
            }
        )
        if purchase_order_id is not UNSET:
            field_dict["purchaseOrderId"] = purchase_order_id
        if sub_status is not UNSET:
            field_dict["subStatus"] = sub_status
        if work_order_operation_inventory_id is not UNSET:
            field_dict["workOrderOperationInventoryId"] = (
                work_order_operation_inventory_id
            )
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if number is not UNSET:
            field_dict["number"] = number
        if selected_batches is not UNSET:
            field_dict["selectedBatches"] = selected_batches
        if withdrawn_at is not UNSET:
            field_dict["withdrawnAt"] = withdrawn_at
        if withdrawn_by_user_id is not UNSET:
            field_dict["withdrawnByUserId"] = withdrawn_by_user_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_reservation_motor_delete import ItemReservationMotorDelete
        from ..models.item_reservation_motor_selected_batch import (
            ItemReservationMotorSelectedBatch,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        status = d.pop("status")

        inventory_item_id = d.pop("inventoryItemId")

        company_id = d.pop("companyId")

        quantity = d.pop("quantity")

        def _parse_purchase_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purchase_order_id = _parse_purchase_order_id(d.pop("purchaseOrderId", UNSET))

        def _parse_sub_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_status = _parse_sub_status(d.pop("subStatus", UNSET))

        def _parse_work_order_operation_inventory_id(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_inventory_id = _parse_work_order_operation_inventory_id(
            d.pop("workOrderOperationInventoryId", UNSET)
        )

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_selected_batches(
            data: object,
        ) -> Union[None, Unset, list["ItemReservationMotorSelectedBatch"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_batches_type_0 = []
                _selected_batches_type_0 = data
                for selected_batches_type_0_item_data in _selected_batches_type_0:
                    selected_batches_type_0_item = (
                        ItemReservationMotorSelectedBatch.from_dict(
                            selected_batches_type_0_item_data
                        )
                    )

                    selected_batches_type_0.append(selected_batches_type_0_item)

                return selected_batches_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ItemReservationMotorSelectedBatch"]], data
            )

        selected_batches = _parse_selected_batches(d.pop("selectedBatches", UNSET))

        def _parse_withdrawn_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        withdrawn_at = _parse_withdrawn_at(d.pop("withdrawnAt", UNSET))

        def _parse_withdrawn_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        withdrawn_by_user_id = _parse_withdrawn_by_user_id(
            d.pop("withdrawnByUserId", UNSET)
        )

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_deleted(
            data: object,
        ) -> Union["ItemReservationMotorDelete", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_type_0 = ItemReservationMotorDelete.from_dict(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ItemReservationMotorDelete", None, Unset], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        item_reservation_motor = cls(
            id=id,
            type_=type_,
            status=status,
            inventory_item_id=inventory_item_id,
            company_id=company_id,
            quantity=quantity,
            purchase_order_id=purchase_order_id,
            sub_status=sub_status,
            work_order_operation_inventory_id=work_order_operation_inventory_id,
            work_order_operation_id=work_order_operation_id,
            identifier_code=identifier_code,
            work_order_id=work_order_id,
            number=number,
            selected_batches=selected_batches,
            withdrawn_at=withdrawn_at,
            withdrawn_by_user_id=withdrawn_by_user_id,
            created_at=created_at,
            deleted=deleted,
        )

        item_reservation_motor.additional_properties = d
        return item_reservation_motor

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

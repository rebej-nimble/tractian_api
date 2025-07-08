from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_reservation_request_selected_batches_api import (
        ItemReservationRequestSelectedBatchesAPI,
    )


T = TypeVar("T", bound="ItemReservationRequestAPI")


@_attrs_define
class ItemReservationRequestAPI:
    work_order_operation_id: str
    """ Unique identifier of the work order operation related to the reservation. """
    work_order_id: str
    """ Unique identifier of the work order. """
    inventory_id: str
    """ Unique identifier of the inventory item being reserved. """
    quantity: float
    """ Total quantity of the item to be reserved. """
    selected_batches: list["ItemReservationRequestSelectedBatchesAPI"]
    """ List of selected batches from which the item will be reserved. """
    should_reserve: bool
    """ Indicates whether the item should be reserved. """
    company_id: str
    """ Unique identifier of the company requesting the reservation. """
    should_request_purchase: bool
    """ Indicates whether a purchase request should be triggered if the stock is insufficient. """
    identifier_code: Union[None, Unset, str] = UNSET
    """ Unique identifier code of the item, if applicable. This field should be used to store the customer's unique
    code for the reservation. """

    def to_dict(self) -> dict[str, Any]:
        work_order_operation_id = self.work_order_operation_id

        work_order_id = self.work_order_id

        inventory_id = self.inventory_id

        quantity = self.quantity

        selected_batches = []
        for selected_batches_item_data in self.selected_batches:
            selected_batches_item = selected_batches_item_data.to_dict()
            selected_batches.append(selected_batches_item)

        should_reserve = self.should_reserve

        company_id = self.company_id

        should_request_purchase = self.should_request_purchase

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workOrderOperationId": work_order_operation_id,
                "workOrderId": work_order_id,
                "inventoryId": inventory_id,
                "quantity": quantity,
                "selectedBatches": selected_batches,
                "shouldReserve": should_reserve,
                "companyId": company_id,
                "shouldRequestPurchase": should_request_purchase,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_reservation_request_selected_batches_api import (
            ItemReservationRequestSelectedBatchesAPI,
        )

        d = dict(src_dict)
        work_order_operation_id = d.pop("workOrderOperationId")

        work_order_id = d.pop("workOrderId")

        inventory_id = d.pop("inventoryId")

        quantity = d.pop("quantity")

        selected_batches = []
        _selected_batches = d.pop("selectedBatches")
        for selected_batches_item_data in _selected_batches:
            selected_batches_item = ItemReservationRequestSelectedBatchesAPI.from_dict(
                selected_batches_item_data
            )

            selected_batches.append(selected_batches_item)

        should_reserve = d.pop("shouldReserve")

        company_id = d.pop("companyId")

        should_request_purchase = d.pop("shouldRequestPurchase")

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        item_reservation_request_api = cls(
            work_order_operation_id=work_order_operation_id,
            work_order_id=work_order_id,
            inventory_id=inventory_id,
            quantity=quantity,
            selected_batches=selected_batches,
            should_reserve=should_reserve,
            company_id=company_id,
            should_request_purchase=should_request_purchase,
            identifier_code=identifier_code,
        )

        return item_reservation_request_api

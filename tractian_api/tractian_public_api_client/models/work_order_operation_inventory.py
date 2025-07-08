from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_order_operation_inventory_inventory import (
        WorkOrderOperationInventoryInventory,
    )
    from ..models.work_order_operation_inventory_selected_batch import (
        WorkOrderOperationInventorySelectedBatch,
    )


T = TypeVar("T", bound="WorkOrderOperationInventory")


@_attrs_define
class WorkOrderOperationInventory:
    quantity: float
    work_order_operation_id: str
    reservation_id: str
    inventory: "WorkOrderOperationInventoryInventory"
    selected_batches: Union[
        None, Unset, list["WorkOrderOperationInventorySelectedBatch"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        work_order_operation_id = self.work_order_operation_id

        reservation_id = self.reservation_id

        inventory = self.inventory.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "workOrderOperationId": work_order_operation_id,
                "reservationId": reservation_id,
                "inventory": inventory,
            }
        )
        if selected_batches is not UNSET:
            field_dict["selectedBatches"] = selected_batches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_order_operation_inventory_inventory import (
            WorkOrderOperationInventoryInventory,
        )
        from ..models.work_order_operation_inventory_selected_batch import (
            WorkOrderOperationInventorySelectedBatch,
        )

        d = dict(src_dict)
        quantity = d.pop("quantity")

        work_order_operation_id = d.pop("workOrderOperationId")

        reservation_id = d.pop("reservationId")

        inventory = WorkOrderOperationInventoryInventory.from_dict(d.pop("inventory"))

        def _parse_selected_batches(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderOperationInventorySelectedBatch"]]:
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
                        WorkOrderOperationInventorySelectedBatch.from_dict(
                            selected_batches_type_0_item_data
                        )
                    )

                    selected_batches_type_0.append(selected_batches_type_0_item)

                return selected_batches_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["WorkOrderOperationInventorySelectedBatch"]],
                data,
            )

        selected_batches = _parse_selected_batches(d.pop("selectedBatches", UNSET))

        work_order_operation_inventory = cls(
            quantity=quantity,
            work_order_operation_id=work_order_operation_id,
            reservation_id=reservation_id,
            inventory=inventory,
            selected_batches=selected_batches,
        )

        work_order_operation_inventory.additional_properties = d
        return work_order_operation_inventory

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

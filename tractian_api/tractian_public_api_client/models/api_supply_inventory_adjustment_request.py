from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.inventory_adjustment_type_enum import (
    InventoryAdjustmentTypeEnum,
    check_inventory_adjustment_type_enum,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_adjustment_position_supply_request import (
        InventoryAdjustmentPositionSupplyRequest,
    )
    from ..models.inventory_adjustments_inbound_batch_supply_request import (
        InventoryAdjustmentsInboundBatchSupplyRequest,
    )
    from ..models.new_inbound_batch_supply_request import NewInboundBatchSupplyRequest


T = TypeVar("T", bound="ApiSupplyInventoryAdjustmentRequest")


@_attrs_define
class ApiSupplyInventoryAdjustmentRequest:
    created_at: str
    updated_at: str
    created_by_user_id: str
    updated_by_user_id: str
    item_id: str
    item_storage_id: str
    quantity: float
    company_id: str
    cost_center_id: str
    type_: InventoryAdjustmentTypeEnum
    inventory_adjustment_positions: list["InventoryAdjustmentPositionSupplyRequest"]
    inbound_batches: list["InventoryAdjustmentsInboundBatchSupplyRequest"]
    new_inbound_batch: Union["NewInboundBatchSupplyRequest", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_inbound_batch_supply_request import (
            NewInboundBatchSupplyRequest,
        )

        created_at = self.created_at

        updated_at = self.updated_at

        created_by_user_id = self.created_by_user_id

        updated_by_user_id = self.updated_by_user_id

        item_id = self.item_id

        item_storage_id = self.item_storage_id

        quantity = self.quantity

        company_id = self.company_id

        cost_center_id = self.cost_center_id

        type_: str = self.type_

        inventory_adjustment_positions = []
        for (
            inventory_adjustment_positions_item_data
        ) in self.inventory_adjustment_positions:
            inventory_adjustment_positions_item = (
                inventory_adjustment_positions_item_data.to_dict()
            )
            inventory_adjustment_positions.append(inventory_adjustment_positions_item)

        inbound_batches = []
        for inbound_batches_item_data in self.inbound_batches:
            inbound_batches_item = inbound_batches_item_data.to_dict()
            inbound_batches.append(inbound_batches_item)

        new_inbound_batch: Union[None, Unset, dict[str, Any]]
        if isinstance(self.new_inbound_batch, Unset):
            new_inbound_batch = UNSET
        elif isinstance(self.new_inbound_batch, NewInboundBatchSupplyRequest):
            new_inbound_batch = self.new_inbound_batch.to_dict()
        else:
            new_inbound_batch = self.new_inbound_batch

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
                "itemId": item_id,
                "itemStorageId": item_storage_id,
                "quantity": quantity,
                "companyId": company_id,
                "costCenterId": cost_center_id,
                "type": type_,
                "inventoryAdjustmentPositions": inventory_adjustment_positions,
                "inboundBatches": inbound_batches,
            }
        )
        if new_inbound_batch is not UNSET:
            field_dict["newInboundBatch"] = new_inbound_batch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_adjustment_position_supply_request import (
            InventoryAdjustmentPositionSupplyRequest,
        )
        from ..models.inventory_adjustments_inbound_batch_supply_request import (
            InventoryAdjustmentsInboundBatchSupplyRequest,
        )
        from ..models.new_inbound_batch_supply_request import (
            NewInboundBatchSupplyRequest,
        )

        d = dict(src_dict)
        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        created_by_user_id = d.pop("createdByUserId")

        updated_by_user_id = d.pop("updatedByUserId")

        item_id = d.pop("itemId")

        item_storage_id = d.pop("itemStorageId")

        quantity = d.pop("quantity")

        company_id = d.pop("companyId")

        cost_center_id = d.pop("costCenterId")

        type_ = check_inventory_adjustment_type_enum(d.pop("type"))

        inventory_adjustment_positions = []
        _inventory_adjustment_positions = d.pop("inventoryAdjustmentPositions")
        for inventory_adjustment_positions_item_data in _inventory_adjustment_positions:
            inventory_adjustment_positions_item = (
                InventoryAdjustmentPositionSupplyRequest.from_dict(
                    inventory_adjustment_positions_item_data
                )
            )

            inventory_adjustment_positions.append(inventory_adjustment_positions_item)

        inbound_batches = []
        _inbound_batches = d.pop("inboundBatches")
        for inbound_batches_item_data in _inbound_batches:
            inbound_batches_item = (
                InventoryAdjustmentsInboundBatchSupplyRequest.from_dict(
                    inbound_batches_item_data
                )
            )

            inbound_batches.append(inbound_batches_item)

        def _parse_new_inbound_batch(
            data: object,
        ) -> Union["NewInboundBatchSupplyRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_inbound_batch_type_0 = NewInboundBatchSupplyRequest.from_dict(data)

                return new_inbound_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewInboundBatchSupplyRequest", None, Unset], data)

        new_inbound_batch = _parse_new_inbound_batch(d.pop("newInboundBatch", UNSET))

        api_supply_inventory_adjustment_request = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            item_id=item_id,
            item_storage_id=item_storage_id,
            quantity=quantity,
            company_id=company_id,
            cost_center_id=cost_center_id,
            type_=type_,
            inventory_adjustment_positions=inventory_adjustment_positions,
            inbound_batches=inbound_batches,
            new_inbound_batch=new_inbound_batch,
        )

        return api_supply_inventory_adjustment_request

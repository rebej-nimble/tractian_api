from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.inventory_adjustment_updated_balance_supply_response import (
        InventoryAdjustmentUpdatedBalanceSupplyResponse,
    )


T = TypeVar("T", bound="ApiSupplyInventoryAdjustmentResponse")


@_attrs_define
class ApiSupplyInventoryAdjustmentResponse:
    movement_id: str
    updated_balance: "InventoryAdjustmentUpdatedBalanceSupplyResponse"

    def to_dict(self) -> dict[str, Any]:
        movement_id = self.movement_id

        updated_balance = self.updated_balance.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "movementId": movement_id,
                "updatedBalance": updated_balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_adjustment_updated_balance_supply_response import (
            InventoryAdjustmentUpdatedBalanceSupplyResponse,
        )

        d = dict(src_dict)
        movement_id = d.pop("movementId")

        updated_balance = InventoryAdjustmentUpdatedBalanceSupplyResponse.from_dict(
            d.pop("updatedBalance")
        )

        api_supply_inventory_adjustment_response = cls(
            movement_id=movement_id,
            updated_balance=updated_balance,
        )

        return api_supply_inventory_adjustment_response

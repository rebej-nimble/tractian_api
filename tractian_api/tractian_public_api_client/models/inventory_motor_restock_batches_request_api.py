from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.inventory_restock_batches_api import InventoryRestockBatchesAPI


T = TypeVar("T", bound="InventoryMotorRestockBatchesRequestAPI")


@_attrs_define
class InventoryMotorRestockBatchesRequestAPI:
    restock: "InventoryRestockBatchesAPI"

    def to_dict(self) -> dict[str, Any]:
        restock = self.restock.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "restock": restock,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_restock_batches_api import InventoryRestockBatchesAPI

        d = dict(src_dict)
        restock = InventoryRestockBatchesAPI.from_dict(d.pop("restock"))

        inventory_motor_restock_batches_request_api = cls(
            restock=restock,
        )

        return inventory_motor_restock_batches_request_api

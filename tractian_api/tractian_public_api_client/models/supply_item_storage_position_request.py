from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupplyItemStoragePositionRequest")


@_attrs_define
class SupplyItemStoragePositionRequest:
    storage_id: str
    quantity: float
    total_price: float
    storage_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_id = self.storage_id

        quantity = self.quantity

        total_price = self.total_price

        storage_name = self.storage_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storageId": storage_id,
                "quantity": quantity,
                "totalPrice": total_price,
                "storageName": storage_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        storage_id = d.pop("storageId")

        quantity = d.pop("quantity")

        total_price = d.pop("totalPrice")

        storage_name = d.pop("storageName")

        supply_item_storage_position_request = cls(
            storage_id=storage_id,
            quantity=quantity,
            total_price=total_price,
            storage_name=storage_name,
        )

        supply_item_storage_position_request.additional_properties = d
        return supply_item_storage_position_request

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

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WithdrawnPosition")


@_attrs_define
class WithdrawnPosition:
    item_reservation_id: str
    storage_id: str
    storage_name: str
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_reservation_id = self.item_reservation_id

        storage_id = self.storage_id

        storage_name = self.storage_name

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemReservationId": item_reservation_id,
                "storageId": storage_id,
                "storageName": storage_name,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_reservation_id = d.pop("itemReservationId")

        storage_id = d.pop("storageId")

        storage_name = d.pop("storageName")

        quantity = d.pop("quantity")

        withdrawn_position = cls(
            item_reservation_id=item_reservation_id,
            storage_id=storage_id,
            storage_name=storage_name,
            quantity=quantity,
        )

        withdrawn_position.additional_properties = d
        return withdrawn_position

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

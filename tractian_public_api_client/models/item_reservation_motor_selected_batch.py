from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ItemReservationMotorSelectedBatch")


@_attrs_define
class ItemReservationMotorSelectedBatch:
    id: str
    """ Unique identifier of the selected batch. """
    quantity: float
    """ Quantity reserved from the selected batch. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quantity = d.pop("quantity")

        item_reservation_motor_selected_batch = cls(
            id=id,
            quantity=quantity,
        )

        item_reservation_motor_selected_batch.additional_properties = d
        return item_reservation_motor_selected_batch

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

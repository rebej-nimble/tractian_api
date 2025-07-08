from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ItemReservationRequestSelectedBatchesAPI")


@_attrs_define
class ItemReservationRequestSelectedBatchesAPI:
    id: str
    """ Unique identifier of the selected batch. """
    quantity: float
    """ Quantity to be reserved from the selected batch. """

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

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

        item_reservation_request_selected_batches_api = cls(
            id=id,
            quantity=quantity,
        )

        return item_reservation_request_selected_batches_api

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WithdrawnBatch")


@_attrs_define
class WithdrawnBatch:
    item_reservation_id: str
    inbound_batch_id: str
    inbound_batch_unit_price: float
    inbound_batch_name: str
    quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_reservation_id = self.item_reservation_id

        inbound_batch_id = self.inbound_batch_id

        inbound_batch_unit_price = self.inbound_batch_unit_price

        inbound_batch_name = self.inbound_batch_name

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemReservationId": item_reservation_id,
                "inboundBatchId": inbound_batch_id,
                "inboundBatchUnitPrice": inbound_batch_unit_price,
                "inboundBatchName": inbound_batch_name,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_reservation_id = d.pop("itemReservationId")

        inbound_batch_id = d.pop("inboundBatchId")

        inbound_batch_unit_price = d.pop("inboundBatchUnitPrice")

        inbound_batch_name = d.pop("inboundBatchName")

        quantity = d.pop("quantity")

        withdrawn_batch = cls(
            item_reservation_id=item_reservation_id,
            inbound_batch_id=inbound_batch_id,
            inbound_batch_unit_price=inbound_batch_unit_price,
            inbound_batch_name=inbound_batch_name,
            quantity=quantity,
        )

        withdrawn_batch.additional_properties = d
        return withdrawn_batch

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

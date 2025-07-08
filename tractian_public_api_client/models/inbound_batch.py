from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InboundBatch")


@_attrs_define
class InboundBatch:
    item_storage_id: str
    inbound_batch_id: str
    quantity: float
    inbound_batch_name: str
    inbound_batch_unit_price: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_storage_id = self.item_storage_id

        inbound_batch_id = self.inbound_batch_id

        quantity = self.quantity

        inbound_batch_name = self.inbound_batch_name

        inbound_batch_unit_price = self.inbound_batch_unit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemStorageId": item_storage_id,
                "inboundBatchId": inbound_batch_id,
                "quantity": quantity,
                "inboundBatchName": inbound_batch_name,
                "inboundBatchUnitPrice": inbound_batch_unit_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_storage_id = d.pop("itemStorageId")

        inbound_batch_id = d.pop("inboundBatchId")

        quantity = d.pop("quantity")

        inbound_batch_name = d.pop("inboundBatchName")

        inbound_batch_unit_price = d.pop("inboundBatchUnitPrice")

        inbound_batch = cls(
            item_storage_id=item_storage_id,
            inbound_batch_id=inbound_batch_id,
            quantity=quantity,
            inbound_batch_name=inbound_batch_name,
            inbound_batch_unit_price=inbound_batch_unit_price,
        )

        inbound_batch.additional_properties = d
        return inbound_batch

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

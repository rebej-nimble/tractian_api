from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApiSupplyItemStorageInboundBatch")


@_attrs_define
class ApiSupplyItemStorageInboundBatch:
    item_id: str
    """ Item id. """
    quantity: float
    """ Quantity. """
    company_id: str
    """ Company id. """
    name: str
    """ Name. """
    entry_date: str
    """ Entry date. """
    unit_price: float
    """ Unit price. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        quantity = self.quantity

        company_id = self.company_id

        name = self.name

        entry_date = self.entry_date

        unit_price = self.unit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemId": item_id,
                "quantity": quantity,
                "companyId": company_id,
                "name": name,
                "entryDate": entry_date,
                "unitPrice": unit_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("itemId")

        quantity = d.pop("quantity")

        company_id = d.pop("companyId")

        name = d.pop("name")

        entry_date = d.pop("entryDate")

        unit_price = d.pop("unitPrice")

        api_supply_item_storage_inbound_batch = cls(
            item_id=item_id,
            quantity=quantity,
            company_id=company_id,
            name=name,
            entry_date=entry_date,
            unit_price=unit_price,
        )

        api_supply_item_storage_inbound_batch.additional_properties = d
        return api_supply_item_storage_inbound_batch

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

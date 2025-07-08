from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SupplyItemStorageInboundBatchRequest")


@_attrs_define
class SupplyItemStorageInboundBatchRequest:
    quantity: float
    company_id: str
    name: str
    entry_date: str
    unit_price: float

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        company_id = self.company_id

        name = self.name

        entry_date = self.entry_date

        unit_price = self.unit_price

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
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
        quantity = d.pop("quantity")

        company_id = d.pop("companyId")

        name = d.pop("name")

        entry_date = d.pop("entryDate")

        unit_price = d.pop("unitPrice")

        supply_item_storage_inbound_batch_request = cls(
            quantity=quantity,
            company_id=company_id,
            name=name,
            entry_date=entry_date,
            unit_price=unit_price,
        )

        return supply_item_storage_inbound_batch_request

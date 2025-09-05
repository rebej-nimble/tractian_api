from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewInboundBatchSupplyRequest")


@_attrs_define
class NewInboundBatchSupplyRequest:
    unit_price: float
    entry_date: str
    name: str
    identifier_code: str

    def to_dict(self) -> dict[str, Any]:
        unit_price = self.unit_price

        entry_date = self.entry_date

        name = self.name

        identifier_code = self.identifier_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "unitPrice": unit_price,
                "entryDate": entry_date,
                "name": name,
                "identifierCode": identifier_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_price = d.pop("unitPrice")

        entry_date = d.pop("entryDate")

        name = d.pop("name")

        identifier_code = d.pop("identifierCode")

        new_inbound_batch_supply_request = cls(
            unit_price=unit_price,
            entry_date=entry_date,
            name=name,
            identifier_code=identifier_code,
        )

        return new_inbound_batch_supply_request

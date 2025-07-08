from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    stock_quantity: float
    available_quantity: float
    reserved_quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stock_quantity = self.stock_quantity

        available_quantity = self.available_quantity

        reserved_quantity = self.reserved_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stockQuantity": stock_quantity,
                "availableQuantity": available_quantity,
                "reservedQuantity": reserved_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stock_quantity = d.pop("stockQuantity")

        available_quantity = d.pop("availableQuantity")

        reserved_quantity = d.pop("reservedQuantity")

        balance = cls(
            stock_quantity=stock_quantity,
            available_quantity=available_quantity,
            reserved_quantity=reserved_quantity,
        )

        balance.additional_properties = d
        return balance

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoragePosition")


@_attrs_define
class StoragePosition:
    quantity: float
    storage_id: str
    storage_name: str
    item_storage_id: str
    total_price: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        storage_id = self.storage_id

        storage_name = self.storage_name

        item_storage_id = self.item_storage_id

        total_price: Union[None, Unset, float]
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "storageId": storage_id,
                "storageName": storage_name,
                "itemStorageId": item_storage_id,
            }
        )
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        storage_id = d.pop("storageId")

        storage_name = d.pop("storageName")

        item_storage_id = d.pop("itemStorageId")

        def _parse_total_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))

        storage_position = cls(
            quantity=quantity,
            storage_id=storage_id,
            storage_name=storage_name,
            item_storage_id=item_storage_id,
            total_price=total_price,
        )

        storage_position.additional_properties = d
        return storage_position

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

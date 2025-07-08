from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_items_cost import InventoryItemsCost
    from ..models.other_cost import OtherCost
    from ..models.time_spent_cost import TimeSpentCost


T = TypeVar("T", bound="TotalCost")


@_attrs_define
class TotalCost:
    total: Union[None, Unset, float] = UNSET
    time_spent_cost: Union["TimeSpentCost", None, Unset] = UNSET
    other_cost: Union["OtherCost", None, Unset] = UNSET
    inventory_items_cost: Union["InventoryItemsCost", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_items_cost import InventoryItemsCost
        from ..models.other_cost import OtherCost
        from ..models.time_spent_cost import TimeSpentCost

        total: Union[None, Unset, float]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        time_spent_cost: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time_spent_cost, Unset):
            time_spent_cost = UNSET
        elif isinstance(self.time_spent_cost, TimeSpentCost):
            time_spent_cost = self.time_spent_cost.to_dict()
        else:
            time_spent_cost = self.time_spent_cost

        other_cost: Union[None, Unset, dict[str, Any]]
        if isinstance(self.other_cost, Unset):
            other_cost = UNSET
        elif isinstance(self.other_cost, OtherCost):
            other_cost = self.other_cost.to_dict()
        else:
            other_cost = self.other_cost

        inventory_items_cost: Union[None, Unset, dict[str, Any]]
        if isinstance(self.inventory_items_cost, Unset):
            inventory_items_cost = UNSET
        elif isinstance(self.inventory_items_cost, InventoryItemsCost):
            inventory_items_cost = self.inventory_items_cost.to_dict()
        else:
            inventory_items_cost = self.inventory_items_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if time_spent_cost is not UNSET:
            field_dict["timeSpentCost"] = time_spent_cost
        if other_cost is not UNSET:
            field_dict["otherCost"] = other_cost
        if inventory_items_cost is not UNSET:
            field_dict["inventoryItemsCost"] = inventory_items_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_items_cost import InventoryItemsCost
        from ..models.other_cost import OtherCost
        from ..models.time_spent_cost import TimeSpentCost

        d = dict(src_dict)

        def _parse_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_time_spent_cost(data: object) -> Union["TimeSpentCost", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_spent_cost_type_0 = TimeSpentCost.from_dict(data)

                return time_spent_cost_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TimeSpentCost", None, Unset], data)

        time_spent_cost = _parse_time_spent_cost(d.pop("timeSpentCost", UNSET))

        def _parse_other_cost(data: object) -> Union["OtherCost", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_cost_type_0 = OtherCost.from_dict(data)

                return other_cost_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OtherCost", None, Unset], data)

        other_cost = _parse_other_cost(d.pop("otherCost", UNSET))

        def _parse_inventory_items_cost(
            data: object,
        ) -> Union["InventoryItemsCost", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inventory_items_cost_type_0 = InventoryItemsCost.from_dict(data)

                return inventory_items_cost_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InventoryItemsCost", None, Unset], data)

        inventory_items_cost = _parse_inventory_items_cost(
            d.pop("inventoryItemsCost", UNSET)
        )

        total_cost = cls(
            total=total,
            time_spent_cost=time_spent_cost,
            other_cost=other_cost,
            inventory_items_cost=inventory_items_cost,
        )

        total_cost.additional_properties = d
        return total_cost

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

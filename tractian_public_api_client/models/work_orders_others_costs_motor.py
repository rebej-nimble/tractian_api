from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkOrdersOthersCostsMotor")


@_attrs_define
class WorkOrdersOthersCostsMotor:
    cost_id: str
    """ Unique identifier for the additional cost. """
    cost: float
    """ Additional cost amount related to the work order. """
    category: str
    """ Category of the additional cost, based on the type of expense related to the work order. """
    description: Union[None, Unset, str] = UNSET
    """ Detailed description of the additional cost. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost_id = self.cost_id

        cost = self.cost

        category = self.category

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costId": cost_id,
                "cost": cost,
                "category": category,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_id = d.pop("costId")

        cost = d.pop("cost")

        category = d.pop("category")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        work_orders_others_costs_motor = cls(
            cost_id=cost_id,
            cost=cost,
            category=category,
            description=description,
        )

        work_orders_others_costs_motor.additional_properties = d
        return work_orders_others_costs_motor

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

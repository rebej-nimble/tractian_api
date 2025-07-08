from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.category_other_costs import CategoryOtherCosts, check_category_other_costs
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkOrdersOthersCostsMotorRequestAPI")


@_attrs_define
class WorkOrdersOthersCostsMotorRequestAPI:
    cost: float
    """ Additional cost amount related to the work order. """
    category: CategoryOtherCosts
    description: Union[None, Unset, str] = UNSET
    """ Detailed description of the additional cost. """

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost

        category: str = self.category

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
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
        cost = d.pop("cost")

        category = check_category_other_costs(d.pop("category"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        work_orders_others_costs_motor_request_api = cls(
            cost=cost,
            category=category,
            description=description,
        )

        return work_orders_others_costs_motor_request_api

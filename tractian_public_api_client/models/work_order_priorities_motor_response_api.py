from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkOrderPrioritiesMotorResponseAPI")


@_attrs_define
class WorkOrderPrioritiesMotorResponseAPI:
    id: str
    """ Unique identifier for the work order priority """
    name: str
    """ Human-readable name/label for the priority level """
    color: str
    """ Hexadecimal color code for visual representation in UI """
    company_id: str
    """ Identifier of the company this priority belongs to """
    order: int
    """ Numerical value determining priority ranking (lower numbers indicate higher priority) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        company_id = self.company_id

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
                "companyId": company_id,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        color = d.pop("color")

        company_id = d.pop("companyId")

        order = d.pop("order")

        work_order_priorities_motor_response_api = cls(
            id=id,
            name=name,
            color=color,
            company_id=company_id,
            order=order,
        )

        work_order_priorities_motor_response_api.additional_properties = d
        return work_order_priorities_motor_response_api

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

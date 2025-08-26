from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsFieldValuesMotor")


@_attrs_define
class MetricsFieldValuesMotor:
    id: str
    type_: str
    name: str
    metric_id: str
    value: str
    metric_value_id: str
    notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        name = self.name

        metric_id = self.metric_id

        value = self.value

        metric_value_id = self.metric_value_id

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "name": name,
                "metricId": metric_id,
                "value": value,
                "metricValueId": metric_value_id,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        name = d.pop("name")

        metric_id = d.pop("metricId")

        value = d.pop("value")

        metric_value_id = d.pop("metricValueId")

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        metrics_field_values_motor = cls(
            id=id,
            type_=type_,
            name=name,
            metric_id=metric_id,
            value=value,
            metric_value_id=metric_value_id,
            notes=notes,
        )

        metrics_field_values_motor.additional_properties = d
        return metrics_field_values_motor

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

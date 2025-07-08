from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_field_values import MetricsFieldValues


T = TypeVar("T", bound="Metrics")


@_attrs_define
class Metrics:
    id: str
    name: str
    metric_ids: list[str]
    type_: Union[Unset, str] = "metrics"
    notes: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, list["MetricsFieldValues"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        metric_ids = self.metric_ids

        type_ = self.type_

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        value: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "metricIds": metric_ids,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if notes is not UNSET:
            field_dict["notes"] = notes
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_field_values import MetricsFieldValues

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        metric_ids = cast(list[str], d.pop("metricIds"))

        type_ = d.pop("type", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_value(
            data: object,
        ) -> Union[None, Unset, list["MetricsFieldValues"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:
                    value_type_0_item = MetricsFieldValues.from_dict(
                        value_type_0_item_data
                    )

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MetricsFieldValues"]], data)

        value = _parse_value(d.pop("value", UNSET))

        metrics = cls(
            id=id,
            name=name,
            metric_ids=metric_ids,
            type_=type_,
            notes=notes,
            value=value,
        )

        metrics.additional_properties = d
        return metrics

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

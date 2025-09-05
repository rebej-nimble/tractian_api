from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMetricValue")


@_attrs_define
class ApiMetricValue:
    metric_id: str
    """ Unique identifier of the metric this value belongs to """
    company_id: str
    """ Unique identifier of the company this metric value belongs to """
    date: Union[None, Unset, str] = UNSET
    """ ISO 8601 timestamp when the metric reading was taken """
    note: Union[None, Unset, str] = UNSET
    """ Optional additional notes or comments about the metric reading """
    value: Union[None, Unset, float, int] = UNSET
    """ The actual numeric measurement value (e.g., odometer reading, engine hours) """
    triggered: Union[Unset, bool] = False
    """ Whether this metric value was triggered by an automated process or workflow """
    source: Union[Unset, str] = "manual"
    """ Source of the metric value recording (e.g., 'manual', 'automatic', 'sensor') """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_id = self.metric_id

        company_id = self.company_id

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        value: Union[None, Unset, float, int]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        triggered = self.triggered

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricId": metric_id,
                "companyId": company_id,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if note is not UNSET:
            field_dict["note"] = note
        if value is not UNSET:
            field_dict["value"] = value
        if triggered is not UNSET:
            field_dict["triggered"] = triggered
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric_id = d.pop("metricId")

        company_id = d.pop("companyId")

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, float, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, int], data)

        value = _parse_value(d.pop("value", UNSET))

        triggered = d.pop("triggered", UNSET)

        source = d.pop("source", UNSET)

        api_metric_value = cls(
            metric_id=metric_id,
            company_id=company_id,
            date=date,
            note=note,
            value=value,
            triggered=triggered,
            source=source,
        )

        api_metric_value.additional_properties = d
        return api_metric_value

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

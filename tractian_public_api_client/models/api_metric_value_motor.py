from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMetricValueMotor")


@_attrs_define
class ApiMetricValueMotor:
    metric_id: str
    """ Unique identifier of the metric this value belongs to """
    date: Union[None, Unset, str] = UNSET
    """ ISO 8601 timestamp when the metric reading was taken """
    note: Union[None, Unset, str] = UNSET
    """ Optional additional notes or comments about the metric reading """
    value: Union[None, Unset, float, int] = UNSET
    """ The actual numeric measurement value (e.g., odometer reading, engine hours) """
    source: Union[None, Unset, str] = UNSET
    """ Source of the metric value recording (e.g., 'manual', 'automatic', 'sensor') """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ ID of the user who created/recorded this metric value """
    company_id: Union[None, Unset, str] = UNSET
    """ ID of the company this metric value belongs to """
    id: Union[None, Unset, str] = UNSET
    """ Unique identifier of the metric value record, assigned by the system """
    triggered: Union[Unset, bool] = False
    """ Whether this metric value was triggered by an automated process or workflow """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_id = self.metric_id

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

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        triggered = self.triggered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricId": metric_id,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if note is not UNSET:
            field_dict["note"] = note
        if value is not UNSET:
            field_dict["value"] = value
        if source is not UNSET:
            field_dict["source"] = source
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if id is not UNSET:
            field_dict["id"] = id
        if triggered is not UNSET:
            field_dict["triggered"] = triggered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric_id = d.pop("metricId")

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

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        triggered = d.pop("triggered", UNSET)

        api_metric_value_motor = cls(
            metric_id=metric_id,
            date=date,
            note=note,
            value=value,
            source=source,
            created_by_user_id=created_by_user_id,
            company_id=company_id,
            id=id,
            triggered=triggered,
        )

        api_metric_value_motor.additional_properties = d
        return api_metric_value_motor

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

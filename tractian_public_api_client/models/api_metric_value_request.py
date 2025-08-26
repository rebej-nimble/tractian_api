from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_metric_value import ApiMetricValue


T = TypeVar("T", bound="ApiMetricValueRequest")


@_attrs_define
class ApiMetricValueRequest:
    metric_id: str
    """ Unique identifier of the metric to add a value to """
    value: Union["ApiMetricValue", None, Unset] = UNSET
    """ The metric value data to be created """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_metric_value import ApiMetricValue

        metric_id = self.metric_id

        value: Union[None, Unset, dict[str, Any]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ApiMetricValue):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metricId": metric_id,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_metric_value import ApiMetricValue

        d = dict(src_dict)
        metric_id = d.pop("metricId")

        def _parse_value(data: object) -> Union["ApiMetricValue", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ApiMetricValue.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiMetricValue", None, Unset], data)

        value = _parse_value(d.pop("value", UNSET))

        api_metric_value_request = cls(
            metric_id=metric_id,
            value=value,
        )

        api_metric_value_request.additional_properties = d
        return api_metric_value_request

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

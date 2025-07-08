from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostSamplesWithTariffStation")


@_attrs_define
class CostSamplesWithTariffStation:
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Date of each sample in ISO 8601 format """
    cost_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy cost in the company's currency
            for the peak period, each value represents a sample.
             """
    cost_off_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy cost in the company's currency
            for the off-peak period, each value represents a sample.
             """
    cost_intermediate: Union[Unset, list[float]] = UNSET
    """ List of values for the energy cost in the company's currency
            for the intermediate period, each value represents a sample.
             """
    forecast: Union[Unset, list[bool]] = UNSET
    """ List of values that tells if that sample is a forecast or not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        cost_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.cost_peak, Unset):
            cost_peak = self.cost_peak

        cost_off_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.cost_off_peak, Unset):
            cost_off_peak = self.cost_off_peak

        cost_intermediate: Union[Unset, list[float]] = UNSET
        if not isinstance(self.cost_intermediate, Unset):
            cost_intermediate = self.cost_intermediate

        forecast: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if cost_peak is not UNSET:
            field_dict["costPeak"] = cost_peak
        if cost_off_peak is not UNSET:
            field_dict["costOffPeak"] = cost_off_peak
        if cost_intermediate is not UNSET:
            field_dict["costIntermediate"] = cost_intermediate
        if forecast is not UNSET:
            field_dict["forecast"] = forecast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        cost_peak = cast(list[float], d.pop("costPeak", UNSET))

        cost_off_peak = cast(list[float], d.pop("costOffPeak", UNSET))

        cost_intermediate = cast(list[float], d.pop("costIntermediate", UNSET))

        forecast = cast(list[bool], d.pop("forecast", UNSET))

        cost_samples_with_tariff_station = cls(
            sampled_at=sampled_at,
            cost_peak=cost_peak,
            cost_off_peak=cost_off_peak,
            cost_intermediate=cost_intermediate,
            forecast=forecast,
        )

        cost_samples_with_tariff_station.additional_properties = d
        return cost_samples_with_tariff_station

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

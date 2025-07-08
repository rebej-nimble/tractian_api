from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DemandSamplesWithTariffStation")


@_attrs_define
class DemandSamplesWithTariffStation:
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Date of each sample in ISO 8601 format """
    demand_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy demand in W for the peak period, each value represents a sample. """
    demand_off_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy demand in W for the off-peak period, each value represents a sample. """
    demand_intermediate: Union[Unset, list[float]] = UNSET
    """ List of values for the energy demand in W for the intermediate period, each value represents a sample. """
    forecast: Union[Unset, list[bool]] = UNSET
    """ List of values that tells if that sample is a forecast or not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        demand_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.demand_peak, Unset):
            demand_peak = self.demand_peak

        demand_off_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.demand_off_peak, Unset):
            demand_off_peak = self.demand_off_peak

        demand_intermediate: Union[Unset, list[float]] = UNSET
        if not isinstance(self.demand_intermediate, Unset):
            demand_intermediate = self.demand_intermediate

        forecast: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if demand_peak is not UNSET:
            field_dict["demandPeak"] = demand_peak
        if demand_off_peak is not UNSET:
            field_dict["demandOffPeak"] = demand_off_peak
        if demand_intermediate is not UNSET:
            field_dict["demandIntermediate"] = demand_intermediate
        if forecast is not UNSET:
            field_dict["forecast"] = forecast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        demand_peak = cast(list[float], d.pop("demandPeak", UNSET))

        demand_off_peak = cast(list[float], d.pop("demandOffPeak", UNSET))

        demand_intermediate = cast(list[float], d.pop("demandIntermediate", UNSET))

        forecast = cast(list[bool], d.pop("forecast", UNSET))

        demand_samples_with_tariff_station = cls(
            sampled_at=sampled_at,
            demand_peak=demand_peak,
            demand_off_peak=demand_off_peak,
            demand_intermediate=demand_intermediate,
            forecast=forecast,
        )

        demand_samples_with_tariff_station.additional_properties = d
        return demand_samples_with_tariff_station

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

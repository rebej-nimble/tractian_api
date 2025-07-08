from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumptionSamplesWithTariffStation")


@_attrs_define
class ConsumptionSamplesWithTariffStation:
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Date of each sample in ISO 8601 format """
    consumption_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy consumption in Wh for the peak period, each value represents a sample. """
    consumption_off_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the energy consumption in Wh for the off-peak period,
            each value represents a sample. """
    consumption_intermediate: Union[Unset, list[float]] = UNSET
    """ List of values for the energy consumption in Wh for the intermediate period,
            each value represents a sample. """
    accumulated_consumption_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the accumulated energy consumption in Wh for the peak period,
            each value represents a sample. """
    accumulated_consumption_off_peak: Union[Unset, list[float]] = UNSET
    """ List of values for the accumulated energy consumption in Wh for the off-peak period,
            each value represents a sample. """
    accumulated_consumption_intermediate: Union[Unset, list[float]] = UNSET
    """ List of values for the accumulated energy consumption in Wh for the intermediate period,
            each value represents a sample. """
    forecast: Union[Unset, list[bool]] = UNSET
    """ List of values that tells if that sample is a forecast or not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        consumption_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.consumption_peak, Unset):
            consumption_peak = self.consumption_peak

        consumption_off_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.consumption_off_peak, Unset):
            consumption_off_peak = self.consumption_off_peak

        consumption_intermediate: Union[Unset, list[float]] = UNSET
        if not isinstance(self.consumption_intermediate, Unset):
            consumption_intermediate = self.consumption_intermediate

        accumulated_consumption_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.accumulated_consumption_peak, Unset):
            accumulated_consumption_peak = self.accumulated_consumption_peak

        accumulated_consumption_off_peak: Union[Unset, list[float]] = UNSET
        if not isinstance(self.accumulated_consumption_off_peak, Unset):
            accumulated_consumption_off_peak = self.accumulated_consumption_off_peak

        accumulated_consumption_intermediate: Union[Unset, list[float]] = UNSET
        if not isinstance(self.accumulated_consumption_intermediate, Unset):
            accumulated_consumption_intermediate = (
                self.accumulated_consumption_intermediate
            )

        forecast: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if consumption_peak is not UNSET:
            field_dict["consumptionPeak"] = consumption_peak
        if consumption_off_peak is not UNSET:
            field_dict["consumptionOffPeak"] = consumption_off_peak
        if consumption_intermediate is not UNSET:
            field_dict["consumptionIntermediate"] = consumption_intermediate
        if accumulated_consumption_peak is not UNSET:
            field_dict["accumulatedConsumptionPeak"] = accumulated_consumption_peak
        if accumulated_consumption_off_peak is not UNSET:
            field_dict["accumulatedConsumptionOffPeak"] = (
                accumulated_consumption_off_peak
            )
        if accumulated_consumption_intermediate is not UNSET:
            field_dict["accumulatedConsumptionIntermediate"] = (
                accumulated_consumption_intermediate
            )
        if forecast is not UNSET:
            field_dict["forecast"] = forecast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        consumption_peak = cast(list[float], d.pop("consumptionPeak", UNSET))

        consumption_off_peak = cast(list[float], d.pop("consumptionOffPeak", UNSET))

        consumption_intermediate = cast(
            list[float], d.pop("consumptionIntermediate", UNSET)
        )

        accumulated_consumption_peak = cast(
            list[float], d.pop("accumulatedConsumptionPeak", UNSET)
        )

        accumulated_consumption_off_peak = cast(
            list[float], d.pop("accumulatedConsumptionOffPeak", UNSET)
        )

        accumulated_consumption_intermediate = cast(
            list[float], d.pop("accumulatedConsumptionIntermediate", UNSET)
        )

        forecast = cast(list[bool], d.pop("forecast", UNSET))

        consumption_samples_with_tariff_station = cls(
            sampled_at=sampled_at,
            consumption_peak=consumption_peak,
            consumption_off_peak=consumption_off_peak,
            consumption_intermediate=consumption_intermediate,
            accumulated_consumption_peak=accumulated_consumption_peak,
            accumulated_consumption_off_peak=accumulated_consumption_off_peak,
            accumulated_consumption_intermediate=accumulated_consumption_intermediate,
            forecast=forecast,
        )

        consumption_samples_with_tariff_station.additional_properties = d
        return consumption_samples_with_tariff_station

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

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCostSamplesWithoutTariffStationResponse")


@_attrs_define
class ApiCostSamplesWithoutTariffStationResponse:
    company_id: str
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Date of each sample in ISO 8601 format """
    cost: Union[Unset, list[float]] = UNSET
    """ List of values for the energy cost in the company's currency, each value represents a sample. """
    forecast: Union[Unset, list[bool]] = UNSET
    """ List of values that tells if that sample is a forecast or not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        cost: Union[Unset, list[float]] = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost

        forecast: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
            }
        )
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if cost is not UNSET:
            field_dict["cost"] = cost
        if forecast is not UNSET:
            field_dict["forecast"] = forecast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        cost = cast(list[float], d.pop("cost", UNSET))

        forecast = cast(list[bool], d.pop("forecast", UNSET))

        api_cost_samples_without_tariff_station_response = cls(
            company_id=company_id,
            sampled_at=sampled_at,
            cost=cost,
            forecast=forecast,
        )

        api_cost_samples_without_tariff_station_response.additional_properties = d
        return api_cost_samples_without_tariff_station_response

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

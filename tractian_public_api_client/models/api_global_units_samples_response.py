from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phase_values import PhaseValues


T = TypeVar("T", bound="ApiGlobalUnitsSamplesResponse")


@_attrs_define
class ApiGlobalUnitsSamplesResponse:
    company_id: str
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Date of each sample """
    average: Union[Unset, "PhaseValues"] = UNSET
    maximum: Union[Unset, "PhaseValues"] = UNSET
    minimum: Union[Unset, "PhaseValues"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        average: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.average, Unset):
            average = self.average.to_dict()

        maximum: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maximum, Unset):
            maximum = self.maximum.to_dict()

        minimum: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.minimum, Unset):
            minimum = self.minimum.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
            }
        )
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if average is not UNSET:
            field_dict["average"] = average
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if minimum is not UNSET:
            field_dict["minimum"] = minimum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phase_values import PhaseValues

        d = dict(src_dict)
        company_id = d.pop("companyId")

        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        _average = d.pop("average", UNSET)
        average: Union[Unset, PhaseValues]
        if isinstance(_average, Unset):
            average = UNSET
        else:
            average = PhaseValues.from_dict(_average)

        _maximum = d.pop("maximum", UNSET)
        maximum: Union[Unset, PhaseValues]
        if isinstance(_maximum, Unset):
            maximum = UNSET
        else:
            maximum = PhaseValues.from_dict(_maximum)

        _minimum = d.pop("minimum", UNSET)
        minimum: Union[Unset, PhaseValues]
        if isinstance(_minimum, Unset):
            minimum = UNSET
        else:
            minimum = PhaseValues.from_dict(_minimum)

        api_global_units_samples_response = cls(
            company_id=company_id,
            sampled_at=sampled_at,
            average=average,
            maximum=maximum,
            minimum=minimum,
        )

        api_global_units_samples_response.additional_properties = d
        return api_global_units_samples_response

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

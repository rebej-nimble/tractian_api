from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wave_data import WaveData


T = TypeVar("T", bound="ApiVibrationSamplesResponse")


@_attrs_define
class ApiVibrationSamplesResponse:
    """API response model for vibration samples that includes companyId for proper authorization."""

    company_id: str
    """ Company ID associated with the asset. """
    accel: "WaveData"
    """ Wave data measurements for vibration analysis. """
    powered: list[bool]
    """ Whether the sample was taken while the asset was operating or not. """
    sampled_at: list[str]
    """ Sample date in ISO 8601 format. """
    temperature: list[float]
    """ Temperature data in Celsius. """
    vel: "WaveData"
    """ Wave data measurements for vibration analysis. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        accel = self.accel.to_dict()

        powered = self.powered

        sampled_at = self.sampled_at

        temperature = self.temperature

        vel = self.vel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "accel": accel,
                "powered": powered,
                "sampledAt": sampled_at,
                "temperature": temperature,
                "vel": vel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wave_data import WaveData

        d = dict(src_dict)
        company_id = d.pop("companyId")

        accel = WaveData.from_dict(d.pop("accel"))

        powered = cast(list[bool], d.pop("powered"))

        sampled_at = cast(list[str], d.pop("sampledAt"))

        temperature = cast(list[float], d.pop("temperature"))

        vel = WaveData.from_dict(d.pop("vel"))

        api_vibration_samples_response = cls(
            company_id=company_id,
            accel=accel,
            powered=powered,
            sampled_at=sampled_at,
            temperature=temperature,
            vel=vel,
        )

        api_vibration_samples_response.additional_properties = d
        return api_vibration_samples_response

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

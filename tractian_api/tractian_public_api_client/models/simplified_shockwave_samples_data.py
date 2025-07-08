from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simplified_wave_data import SimplifiedWaveData


T = TypeVar("T", bound="SimplifiedShockwaveSamplesData")


@_attrs_define
class SimplifiedShockwaveSamplesData:
    accel: Union[Unset, "SimplifiedWaveData"] = UNSET
    powered: Union[Unset, list[bool]] = UNSET
    """ Wether the sample was taken while the asset was operating or not. """
    sampled_at: Union[Unset, list[str]] = UNSET
    """ Sample date in ISO 8601 format. """
    temperature: Union[Unset, list[float]] = UNSET
    """ Temperature data in Celsius. """
    vel: Union[Unset, "SimplifiedWaveData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accel, Unset):
            accel = self.accel.to_dict()

        powered: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.powered, Unset):
            powered = self.powered

        sampled_at: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sampled_at, Unset):
            sampled_at = self.sampled_at

        temperature: Union[Unset, list[float]] = UNSET
        if not isinstance(self.temperature, Unset):
            temperature = self.temperature

        vel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vel, Unset):
            vel = self.vel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accel is not UNSET:
            field_dict["accel"] = accel
        if powered is not UNSET:
            field_dict["powered"] = powered
        if sampled_at is not UNSET:
            field_dict["sampledAt"] = sampled_at
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if vel is not UNSET:
            field_dict["vel"] = vel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simplified_wave_data import SimplifiedWaveData

        d = dict(src_dict)
        _accel = d.pop("accel", UNSET)
        accel: Union[Unset, SimplifiedWaveData]
        if isinstance(_accel, Unset):
            accel = UNSET
        else:
            accel = SimplifiedWaveData.from_dict(_accel)

        powered = cast(list[bool], d.pop("powered", UNSET))

        sampled_at = cast(list[str], d.pop("sampledAt", UNSET))

        temperature = cast(list[float], d.pop("temperature", UNSET))

        _vel = d.pop("vel", UNSET)
        vel: Union[Unset, SimplifiedWaveData]
        if isinstance(_vel, Unset):
            vel = UNSET
        else:
            vel = SimplifiedWaveData.from_dict(_vel)

        simplified_shockwave_samples_data = cls(
            accel=accel,
            powered=powered,
            sampled_at=sampled_at,
            temperature=temperature,
            vel=vel,
        )

        simplified_shockwave_samples_data.additional_properties = d
        return simplified_shockwave_samples_data

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

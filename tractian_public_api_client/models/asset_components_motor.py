from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetComponentsMotor")


@_attrs_define
class AssetComponentsMotor:
    no_bearings: Union[Unset, bool] = False
    no_belts: Union[Unset, bool] = False
    no_gears: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_bearings = self.no_bearings

        no_belts = self.no_belts

        no_gears = self.no_gears

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_bearings is not UNSET:
            field_dict["noBearings"] = no_bearings
        if no_belts is not UNSET:
            field_dict["noBelts"] = no_belts
        if no_gears is not UNSET:
            field_dict["noGears"] = no_gears

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no_bearings = d.pop("noBearings", UNSET)

        no_belts = d.pop("noBelts", UNSET)

        no_gears = d.pop("noGears", UNSET)

        asset_components_motor = cls(
            no_bearings=no_bearings,
            no_belts=no_belts,
            no_gears=no_gears,
        )

        asset_components_motor.additional_properties = d
        return asset_components_motor

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

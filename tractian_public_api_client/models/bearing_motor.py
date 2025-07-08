from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bearing_motor_fault_frequencies_type_0 import (
        BearingMotorFaultFrequenciesType0,
    )


T = TypeVar("T", bound="BearingMotor")


@_attrs_define
class BearingMotor:
    type_: Union[None, Unset, str] = UNSET
    bearing_id: Union[None, Unset, str] = UNSET
    ball_diameter: Union[None, Unset, float] = UNSET
    ball_numbers: Union[None, Unset, int] = UNSET
    code: Union[None, Unset, str] = UNSET
    fixed_rpm: Union[None, Unset, int] = UNSET
    min_rpm: Union[None, Unset, int] = UNSET
    max_rpm: Union[None, Unset, int] = UNSET
    inner_pitch_diameter: Union[None, Unset, float] = UNSET
    outer_pitch_diameter: Union[None, Unset, float] = UNSET
    pitch_diameter: Union[None, Unset, float] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    rotation_type: Union[None, Unset, str] = UNSET
    diameter_type: Union[None, Unset, str] = UNSET
    bearing_count: Union[None, Unset, int] = UNSET
    fault_frequencies: Union["BearingMotorFaultFrequenciesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bearing_motor_fault_frequencies_type_0 import (
            BearingMotorFaultFrequenciesType0,
        )

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        bearing_id: Union[None, Unset, str]
        if isinstance(self.bearing_id, Unset):
            bearing_id = UNSET
        else:
            bearing_id = self.bearing_id

        ball_diameter: Union[None, Unset, float]
        if isinstance(self.ball_diameter, Unset):
            ball_diameter = UNSET
        else:
            ball_diameter = self.ball_diameter

        ball_numbers: Union[None, Unset, int]
        if isinstance(self.ball_numbers, Unset):
            ball_numbers = UNSET
        else:
            ball_numbers = self.ball_numbers

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        fixed_rpm: Union[None, Unset, int]
        if isinstance(self.fixed_rpm, Unset):
            fixed_rpm = UNSET
        else:
            fixed_rpm = self.fixed_rpm

        min_rpm: Union[None, Unset, int]
        if isinstance(self.min_rpm, Unset):
            min_rpm = UNSET
        else:
            min_rpm = self.min_rpm

        max_rpm: Union[None, Unset, int]
        if isinstance(self.max_rpm, Unset):
            max_rpm = UNSET
        else:
            max_rpm = self.max_rpm

        inner_pitch_diameter: Union[None, Unset, float]
        if isinstance(self.inner_pitch_diameter, Unset):
            inner_pitch_diameter = UNSET
        else:
            inner_pitch_diameter = self.inner_pitch_diameter

        outer_pitch_diameter: Union[None, Unset, float]
        if isinstance(self.outer_pitch_diameter, Unset):
            outer_pitch_diameter = UNSET
        else:
            outer_pitch_diameter = self.outer_pitch_diameter

        pitch_diameter: Union[None, Unset, float]
        if isinstance(self.pitch_diameter, Unset):
            pitch_diameter = UNSET
        else:
            pitch_diameter = self.pitch_diameter

        manufacturer: Union[None, Unset, str]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = self.manufacturer

        rotation_type: Union[None, Unset, str]
        if isinstance(self.rotation_type, Unset):
            rotation_type = UNSET
        else:
            rotation_type = self.rotation_type

        diameter_type: Union[None, Unset, str]
        if isinstance(self.diameter_type, Unset):
            diameter_type = UNSET
        else:
            diameter_type = self.diameter_type

        bearing_count: Union[None, Unset, int]
        if isinstance(self.bearing_count, Unset):
            bearing_count = UNSET
        else:
            bearing_count = self.bearing_count

        fault_frequencies: Union[None, Unset, dict[str, Any]]
        if isinstance(self.fault_frequencies, Unset):
            fault_frequencies = UNSET
        elif isinstance(self.fault_frequencies, BearingMotorFaultFrequenciesType0):
            fault_frequencies = self.fault_frequencies.to_dict()
        else:
            fault_frequencies = self.fault_frequencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bearing_id is not UNSET:
            field_dict["bearingId"] = bearing_id
        if ball_diameter is not UNSET:
            field_dict["ballDiameter"] = ball_diameter
        if ball_numbers is not UNSET:
            field_dict["ballNumbers"] = ball_numbers
        if code is not UNSET:
            field_dict["code"] = code
        if fixed_rpm is not UNSET:
            field_dict["fixedRPM"] = fixed_rpm
        if min_rpm is not UNSET:
            field_dict["minRPM"] = min_rpm
        if max_rpm is not UNSET:
            field_dict["maxRPM"] = max_rpm
        if inner_pitch_diameter is not UNSET:
            field_dict["innerPitchDiameter"] = inner_pitch_diameter
        if outer_pitch_diameter is not UNSET:
            field_dict["outerPitchDiameter"] = outer_pitch_diameter
        if pitch_diameter is not UNSET:
            field_dict["pitchDiameter"] = pitch_diameter
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if rotation_type is not UNSET:
            field_dict["rotationType"] = rotation_type
        if diameter_type is not UNSET:
            field_dict["diameterType"] = diameter_type
        if bearing_count is not UNSET:
            field_dict["bearingCount"] = bearing_count
        if fault_frequencies is not UNSET:
            field_dict["faultFrequencies"] = fault_frequencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bearing_motor_fault_frequencies_type_0 import (
            BearingMotorFaultFrequenciesType0,
        )

        d = dict(src_dict)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_bearing_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bearing_id = _parse_bearing_id(d.pop("bearingId", UNSET))

        def _parse_ball_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        ball_diameter = _parse_ball_diameter(d.pop("ballDiameter", UNSET))

        def _parse_ball_numbers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ball_numbers = _parse_ball_numbers(d.pop("ballNumbers", UNSET))

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_fixed_rpm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fixed_rpm = _parse_fixed_rpm(d.pop("fixedRPM", UNSET))

        def _parse_min_rpm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        min_rpm = _parse_min_rpm(d.pop("minRPM", UNSET))

        def _parse_max_rpm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_rpm = _parse_max_rpm(d.pop("maxRPM", UNSET))

        def _parse_inner_pitch_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        inner_pitch_diameter = _parse_inner_pitch_diameter(
            d.pop("innerPitchDiameter", UNSET)
        )

        def _parse_outer_pitch_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        outer_pitch_diameter = _parse_outer_pitch_diameter(
            d.pop("outerPitchDiameter", UNSET)
        )

        def _parse_pitch_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pitch_diameter = _parse_pitch_diameter(d.pop("pitchDiameter", UNSET))

        def _parse_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_rotation_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rotation_type = _parse_rotation_type(d.pop("rotationType", UNSET))

        def _parse_diameter_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        diameter_type = _parse_diameter_type(d.pop("diameterType", UNSET))

        def _parse_bearing_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bearing_count = _parse_bearing_count(d.pop("bearingCount", UNSET))

        def _parse_fault_frequencies(
            data: object,
        ) -> Union["BearingMotorFaultFrequenciesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fault_frequencies_type_0 = BearingMotorFaultFrequenciesType0.from_dict(
                    data
                )

                return fault_frequencies_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BearingMotorFaultFrequenciesType0", None, Unset], data)

        fault_frequencies = _parse_fault_frequencies(d.pop("faultFrequencies", UNSET))

        bearing_motor = cls(
            type_=type_,
            bearing_id=bearing_id,
            ball_diameter=ball_diameter,
            ball_numbers=ball_numbers,
            code=code,
            fixed_rpm=fixed_rpm,
            min_rpm=min_rpm,
            max_rpm=max_rpm,
            inner_pitch_diameter=inner_pitch_diameter,
            outer_pitch_diameter=outer_pitch_diameter,
            pitch_diameter=pitch_diameter,
            manufacturer=manufacturer,
            rotation_type=rotation_type,
            diameter_type=diameter_type,
            bearing_count=bearing_count,
            fault_frequencies=fault_frequencies,
        )

        bearing_motor.additional_properties = d
        return bearing_motor

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

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bearing_motor import BearingMotor
    from ..models.components_motor import ComponentsMotor


T = TypeVar("T", bound="SpecificationMotor")


@_attrs_define
class SpecificationMotor:
    axis_x: Union[None, Unset, str] = UNSET
    axis_y: Union[None, Unset, str] = UNSET
    axis_z: Union[None, Unset, str] = UNSET
    bearings: Union[None, Unset, list["BearingMotor"]] = UNSET
    max_temp: Union[None, Unset, float] = UNSET
    max_downtime: Union[None, Unset, int] = UNSET
    mode: Union[None, Unset, str] = UNSET
    power: Union[None, Unset, float] = UNSET
    rpm: Union[None, Unset, int, list[int]] = UNSET
    sensor_pt: Union[None, Unset, bool] = UNSET
    sensor_ct: Union[None, Unset, bool] = UNSET
    downtime_hourly_cost: Union[None, Unset, float] = UNSET
    components: Union["ComponentsMotor", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.components_motor import ComponentsMotor

        axis_x: Union[None, Unset, str]
        if isinstance(self.axis_x, Unset):
            axis_x = UNSET
        else:
            axis_x = self.axis_x

        axis_y: Union[None, Unset, str]
        if isinstance(self.axis_y, Unset):
            axis_y = UNSET
        else:
            axis_y = self.axis_y

        axis_z: Union[None, Unset, str]
        if isinstance(self.axis_z, Unset):
            axis_z = UNSET
        else:
            axis_z = self.axis_z

        bearings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.bearings, Unset):
            bearings = UNSET
        elif isinstance(self.bearings, list):
            bearings = []
            for bearings_type_0_item_data in self.bearings:
                bearings_type_0_item = bearings_type_0_item_data.to_dict()
                bearings.append(bearings_type_0_item)

        else:
            bearings = self.bearings

        max_temp: Union[None, Unset, float]
        if isinstance(self.max_temp, Unset):
            max_temp = UNSET
        else:
            max_temp = self.max_temp

        max_downtime: Union[None, Unset, int]
        if isinstance(self.max_downtime, Unset):
            max_downtime = UNSET
        else:
            max_downtime = self.max_downtime

        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        power: Union[None, Unset, float]
        if isinstance(self.power, Unset):
            power = UNSET
        else:
            power = self.power

        rpm: Union[None, Unset, int, list[int]]
        if isinstance(self.rpm, Unset):
            rpm = UNSET
        elif isinstance(self.rpm, list):
            rpm = self.rpm

        else:
            rpm = self.rpm

        sensor_pt: Union[None, Unset, bool]
        if isinstance(self.sensor_pt, Unset):
            sensor_pt = UNSET
        else:
            sensor_pt = self.sensor_pt

        sensor_ct: Union[None, Unset, bool]
        if isinstance(self.sensor_ct, Unset):
            sensor_ct = UNSET
        else:
            sensor_ct = self.sensor_ct

        downtime_hourly_cost: Union[None, Unset, float]
        if isinstance(self.downtime_hourly_cost, Unset):
            downtime_hourly_cost = UNSET
        else:
            downtime_hourly_cost = self.downtime_hourly_cost

        components: Union[None, Unset, dict[str, Any]]
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, ComponentsMotor):
            components = self.components.to_dict()
        else:
            components = self.components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axis_x is not UNSET:
            field_dict["axisX"] = axis_x
        if axis_y is not UNSET:
            field_dict["axisY"] = axis_y
        if axis_z is not UNSET:
            field_dict["axisZ"] = axis_z
        if bearings is not UNSET:
            field_dict["bearings"] = bearings
        if max_temp is not UNSET:
            field_dict["maxTemp"] = max_temp
        if max_downtime is not UNSET:
            field_dict["maxDowntime"] = max_downtime
        if mode is not UNSET:
            field_dict["mode"] = mode
        if power is not UNSET:
            field_dict["power"] = power
        if rpm is not UNSET:
            field_dict["rpm"] = rpm
        if sensor_pt is not UNSET:
            field_dict["sensorPt"] = sensor_pt
        if sensor_ct is not UNSET:
            field_dict["sensorCt"] = sensor_ct
        if downtime_hourly_cost is not UNSET:
            field_dict["downtimeHourlyCost"] = downtime_hourly_cost
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bearing_motor import BearingMotor
        from ..models.components_motor import ComponentsMotor

        d = dict(src_dict)

        def _parse_axis_x(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        axis_x = _parse_axis_x(d.pop("axisX", UNSET))

        def _parse_axis_y(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        axis_y = _parse_axis_y(d.pop("axisY", UNSET))

        def _parse_axis_z(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        axis_z = _parse_axis_z(d.pop("axisZ", UNSET))

        def _parse_bearings(data: object) -> Union[None, Unset, list["BearingMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bearings_type_0 = []
                _bearings_type_0 = data
                for bearings_type_0_item_data in _bearings_type_0:
                    bearings_type_0_item = BearingMotor.from_dict(
                        bearings_type_0_item_data
                    )

                    bearings_type_0.append(bearings_type_0_item)

                return bearings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["BearingMotor"]], data)

        bearings = _parse_bearings(d.pop("bearings", UNSET))

        def _parse_max_temp(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_temp = _parse_max_temp(d.pop("maxTemp", UNSET))

        def _parse_max_downtime(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_downtime = _parse_max_downtime(d.pop("maxDowntime", UNSET))

        def _parse_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_power(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        power = _parse_power(d.pop("power", UNSET))

        def _parse_rpm(data: object) -> Union[None, Unset, int, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rpm_type_1 = cast(list[int], data)

                return rpm_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, int, list[int]], data)

        rpm = _parse_rpm(d.pop("rpm", UNSET))

        def _parse_sensor_pt(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sensor_pt = _parse_sensor_pt(d.pop("sensorPt", UNSET))

        def _parse_sensor_ct(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sensor_ct = _parse_sensor_ct(d.pop("sensorCt", UNSET))

        def _parse_downtime_hourly_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        downtime_hourly_cost = _parse_downtime_hourly_cost(
            d.pop("downtimeHourlyCost", UNSET)
        )

        def _parse_components(data: object) -> Union["ComponentsMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                components_type_0 = ComponentsMotor.from_dict(data)

                return components_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ComponentsMotor", None, Unset], data)

        components = _parse_components(d.pop("components", UNSET))

        specification_motor = cls(
            axis_x=axis_x,
            axis_y=axis_y,
            axis_z=axis_z,
            bearings=bearings,
            max_temp=max_temp,
            max_downtime=max_downtime,
            mode=mode,
            power=power,
            rpm=rpm,
            sensor_pt=sensor_pt,
            sensor_ct=sensor_ct,
            downtime_hourly_cost=downtime_hourly_cost,
            components=components,
        )

        specification_motor.additional_properties = d
        return specification_motor

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

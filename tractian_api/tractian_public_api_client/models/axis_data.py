from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AxisData")


@_attrs_define
class AxisData:
    x: Union[Unset, list[Union[None, float]]] = UNSET
    """ X-axis data. """
    y: Union[Unset, list[Union[None, float]]] = UNSET
    """ Y-axis data. """
    z: Union[Unset, list[Union[None, float]]] = UNSET
    """ Z-axis data. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x: Union[Unset, list[Union[None, float]]] = UNSET
        if not isinstance(self.x, Unset):
            x = []
            for x_item_data in self.x:
                x_item: Union[None, float]
                x_item = x_item_data
                x.append(x_item)

        y: Union[Unset, list[Union[None, float]]] = UNSET
        if not isinstance(self.y, Unset):
            y = []
            for y_item_data in self.y:
                y_item: Union[None, float]
                y_item = y_item_data
                y.append(y_item)

        z: Union[Unset, list[Union[None, float]]] = UNSET
        if not isinstance(self.z, Unset):
            z = []
            for z_item_data in self.z:
                z_item: Union[None, float]
                z_item = z_item_data
                z.append(z_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = []
        _x = d.pop("x", UNSET)
        for x_item_data in _x or []:

            def _parse_x_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            x_item = _parse_x_item(x_item_data)

            x.append(x_item)

        y = []
        _y = d.pop("y", UNSET)
        for y_item_data in _y or []:

            def _parse_y_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            y_item = _parse_y_item(y_item_data)

            y.append(y_item)

        z = []
        _z = d.pop("z", UNSET)
        for z_item_data in _z or []:

            def _parse_z_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            z_item = _parse_z_item(z_item_data)

            z.append(z_item)

        axis_data = cls(
            x=x,
            y=y,
            z=z,
        )

        axis_data.additional_properties = d
        return axis_data

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

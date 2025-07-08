from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.level_motor import LevelMotor


T = TypeVar("T", bound="FieldsMotor")


@_attrs_define
class FieldsMotor:
    id: str
    levels: Union[None, Unset, list["LevelMotor"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        levels: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.levels, Unset):
            levels = UNSET
        elif isinstance(self.levels, list):
            levels = []
            for levels_type_0_item_data in self.levels:
                levels_type_0_item = levels_type_0_item_data.to_dict()
                levels.append(levels_type_0_item)

        else:
            levels = self.levels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.level_motor import LevelMotor

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_levels(data: object) -> Union[None, Unset, list["LevelMotor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                levels_type_0 = []
                _levels_type_0 = data
                for levels_type_0_item_data in _levels_type_0:
                    levels_type_0_item = LevelMotor.from_dict(levels_type_0_item_data)

                    levels_type_0.append(levels_type_0_item)

                return levels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["LevelMotor"]], data)

        levels = _parse_levels(d.pop("levels", UNSET))

        fields_motor = cls(
            id=id,
            levels=levels,
        )

        fields_motor.additional_properties = d
        return fields_motor

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

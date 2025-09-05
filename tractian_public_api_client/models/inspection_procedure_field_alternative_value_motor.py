from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_procedure_value_motor import InspectionProcedureValueMotor


T = TypeVar("T", bound="InspectionProcedureFieldAlternativeValueMotor")


@_attrs_define
class InspectionProcedureFieldAlternativeValueMotor:
    value: "InspectionProcedureValueMotor"
    level_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.to_dict()

        level_id: Union[None, Unset, str]
        if isinstance(self.level_id, Unset):
            level_id = UNSET
        else:
            level_id = self.level_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if level_id is not UNSET:
            field_dict["levelId"] = level_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inspection_procedure_value_motor import (
            InspectionProcedureValueMotor,
        )

        d = dict(src_dict)
        value = InspectionProcedureValueMotor.from_dict(d.pop("value"))

        def _parse_level_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        level_id = _parse_level_id(d.pop("levelId", UNSET))

        inspection_procedure_field_alternative_value_motor = cls(
            value=value,
            level_id=level_id,
        )

        inspection_procedure_field_alternative_value_motor.additional_properties = d
        return inspection_procedure_field_alternative_value_motor

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

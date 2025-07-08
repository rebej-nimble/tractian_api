from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_procedure_value import ActivityProcedureValue


T = TypeVar("T", bound="InspectionCustom")


@_attrs_define
class InspectionCustom:
    id: str
    name: str
    type_: Union[Unset, str] = "inspectionCustom"
    notes: Union[None, Unset, str] = UNSET
    value: Union["ActivityProcedureValue", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_procedure_value import ActivityProcedureValue

        id = self.id

        name = self.name

        type_ = self.type_

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        value: Union[None, Unset, dict[str, Any]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, ActivityProcedureValue):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if notes is not UNSET:
            field_dict["notes"] = notes
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_procedure_value import ActivityProcedureValue

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_value(data: object) -> Union["ActivityProcedureValue", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = ActivityProcedureValue.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ActivityProcedureValue", None, Unset], data)

        value = _parse_value(d.pop("value", UNSET))

        inspection_custom = cls(
            id=id,
            name=name,
            type_=type_,
            notes=notes,
            value=value,
        )

        inspection_custom.additional_properties = d
        return inspection_custom

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

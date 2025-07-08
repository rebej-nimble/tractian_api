from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_procedure_field_option import ActivityProcedureFieldOption


T = TypeVar("T", bound="Checklist")


@_attrs_define
class Checklist:
    id: str
    name: str
    type_: Union[Unset, str] = "checklist"
    notes: Union[None, Unset, str] = UNSET
    options: Union[None, Unset, list["ActivityProcedureFieldOption"]] = UNSET
    value: Union[None, Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        options: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        value: Union[None, Unset, list[int]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

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
        if options is not UNSET:
            field_dict["options"] = options
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_procedure_field_option import (
            ActivityProcedureFieldOption,
        )

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

        def _parse_options(
            data: object,
        ) -> Union[None, Unset, list["ActivityProcedureFieldOption"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = ActivityProcedureFieldOption.from_dict(
                        options_type_0_item_data
                    )

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ActivityProcedureFieldOption"]], data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = cast(list[int], data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        value = _parse_value(d.pop("value", UNSET))

        checklist = cls(
            id=id,
            name=name,
            type_=type_,
            notes=notes,
            options=options,
            value=value,
        )

        checklist.additional_properties = d
        return checklist

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

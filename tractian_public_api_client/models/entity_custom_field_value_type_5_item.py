from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EntityCustomFieldValueType5Item")


@_attrs_define
class EntityCustomFieldValueType5Item:
    additional_properties: dict[str, Union[None, bool, int, str]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_custom_field_value_type_5_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[None, bool, int, str]:
                if data is None:
                    return data
                return cast(Union[None, bool, int, str], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        entity_custom_field_value_type_5_item.additional_properties = (
            additional_properties
        )
        return entity_custom_field_value_type_5_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, bool, int, str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, bool, int, str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EntityCustomFieldValueType9")


@_attrs_define
class EntityCustomFieldValueType9:
    additional_properties: dict[str, Union[None, list[str]]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = prop

            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_custom_field_value_type_9 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union[None, list[str]]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_0 = cast(list[str], data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                return cast(Union[None, list[str]], data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        entity_custom_field_value_type_9.additional_properties = additional_properties
        return entity_custom_field_value_type_9

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[None, list[str]]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[None, list[str]]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

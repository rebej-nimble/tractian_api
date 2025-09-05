from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_custom_field_value_type_5_item import (
        EntityCustomFieldValueType5Item,
    )
    from ..models.entity_custom_field_value_type_6 import EntityCustomFieldValueType6
    from ..models.entity_custom_field_value_type_7_item import (
        EntityCustomFieldValueType7Item,
    )
    from ..models.entity_custom_field_value_type_8 import EntityCustomFieldValueType8
    from ..models.entity_custom_field_value_type_9 import EntityCustomFieldValueType9
    from ..models.entity_custom_field_value_type_10 import EntityCustomFieldValueType10


T = TypeVar("T", bound="EntityCustomField")


@_attrs_define
class EntityCustomField:
    id_custom_field: str
    field_type: str
    value: Union[
        "EntityCustomFieldValueType10",
        "EntityCustomFieldValueType6",
        "EntityCustomFieldValueType8",
        "EntityCustomFieldValueType9",
        None,
        Unset,
        bool,
        float,
        int,
        list["EntityCustomFieldValueType5Item"],
        list["EntityCustomFieldValueType7Item"],
        list[int],
        list[str],
        str,
    ] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_custom_field_value_type_6 import (
            EntityCustomFieldValueType6,
        )
        from ..models.entity_custom_field_value_type_8 import (
            EntityCustomFieldValueType8,
        )
        from ..models.entity_custom_field_value_type_9 import (
            EntityCustomFieldValueType9,
        )
        from ..models.entity_custom_field_value_type_10 import (
            EntityCustomFieldValueType10,
        )

        id_custom_field = self.id_custom_field

        field_type = self.field_type

        value: Union[
            None,
            Unset,
            bool,
            dict[str, Any],
            float,
            int,
            list[dict[str, Any]],
            list[int],
            list[str],
            str,
        ]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, list):
            value = []
            for value_type_5_item_data in self.value:
                value_type_5_item = value_type_5_item_data.to_dict()
                value.append(value_type_5_item)

        elif isinstance(self.value, EntityCustomFieldValueType6):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_7_item_data in self.value:
                value_type_7_item = value_type_7_item_data.to_dict()
                value.append(value_type_7_item)

        elif isinstance(self.value, EntityCustomFieldValueType8):
            value = self.value.to_dict()
        elif isinstance(self.value, EntityCustomFieldValueType9):
            value = self.value.to_dict()
        elif isinstance(self.value, EntityCustomFieldValueType10):
            value = self.value.to_dict()
        else:
            value = self.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idCustomField": id_custom_field,
                "fieldType": field_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_custom_field_value_type_5_item import (
            EntityCustomFieldValueType5Item,
        )
        from ..models.entity_custom_field_value_type_6 import (
            EntityCustomFieldValueType6,
        )
        from ..models.entity_custom_field_value_type_7_item import (
            EntityCustomFieldValueType7Item,
        )
        from ..models.entity_custom_field_value_type_8 import (
            EntityCustomFieldValueType8,
        )
        from ..models.entity_custom_field_value_type_9 import (
            EntityCustomFieldValueType9,
        )
        from ..models.entity_custom_field_value_type_10 import (
            EntityCustomFieldValueType10,
        )

        d = dict(src_dict)
        id_custom_field = d.pop("idCustomField")

        field_type = d.pop("fieldType")

        def _parse_value(
            data: object,
        ) -> Union[
            "EntityCustomFieldValueType10",
            "EntityCustomFieldValueType6",
            "EntityCustomFieldValueType8",
            "EntityCustomFieldValueType9",
            None,
            Unset,
            bool,
            float,
            int,
            list["EntityCustomFieldValueType5Item"],
            list["EntityCustomFieldValueType7Item"],
            list[int],
            list[str],
            str,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_1 = cast(list[str], data)

                return value_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(list[int], data)

                return value_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_5 = []
                _value_type_5 = data
                for value_type_5_item_data in _value_type_5:
                    value_type_5_item = EntityCustomFieldValueType5Item.from_dict(
                        value_type_5_item_data
                    )

                    value_type_5.append(value_type_5_item)

                return value_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_6 = EntityCustomFieldValueType6.from_dict(data)

                return value_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_7 = []
                _value_type_7 = data
                for value_type_7_item_data in _value_type_7:
                    value_type_7_item = EntityCustomFieldValueType7Item.from_dict(
                        value_type_7_item_data
                    )

                    value_type_7.append(value_type_7_item)

                return value_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_8 = EntityCustomFieldValueType8.from_dict(data)

                return value_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_9 = EntityCustomFieldValueType9.from_dict(data)

                return value_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_10 = EntityCustomFieldValueType10.from_dict(data)

                return value_type_10
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "EntityCustomFieldValueType10",
                    "EntityCustomFieldValueType6",
                    "EntityCustomFieldValueType8",
                    "EntityCustomFieldValueType9",
                    None,
                    Unset,
                    bool,
                    float,
                    int,
                    list["EntityCustomFieldValueType5Item"],
                    list["EntityCustomFieldValueType7Item"],
                    list[int],
                    list[str],
                    str,
                ],
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        entity_custom_field = cls(
            id_custom_field=id_custom_field,
            field_type=field_type,
            value=value,
            name=name,
        )

        entity_custom_field.additional_properties = d
        return entity_custom_field

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

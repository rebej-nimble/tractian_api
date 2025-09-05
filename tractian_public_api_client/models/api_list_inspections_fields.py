from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_list_inspections_level import ApiListInspectionsLevel
    from ..models.api_list_inspections_option import ApiListInspectionsOption


T = TypeVar("T", bound="ApiListInspectionsFields")


@_attrs_define
class ApiListInspectionsFields:
    id: str
    type_: str
    name: str
    help_text: Union[None, Unset, str] = UNSET
    options: Union[None, Unset, list["ApiListInspectionsOption"]] = UNSET
    levels: Union[None, Unset, list["ApiListInspectionsLevel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        name = self.name

        help_text: Union[None, Unset, str]
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

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
                "type": type_,
                "name": name,
            }
        )
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if options is not UNSET:
            field_dict["options"] = options
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_list_inspections_level import ApiListInspectionsLevel
        from ..models.api_list_inspections_option import ApiListInspectionsOption

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        name = d.pop("name")

        def _parse_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        def _parse_options(
            data: object,
        ) -> Union[None, Unset, list["ApiListInspectionsOption"]]:
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
                    options_type_0_item = ApiListInspectionsOption.from_dict(
                        options_type_0_item_data
                    )

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApiListInspectionsOption"]], data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_levels(
            data: object,
        ) -> Union[None, Unset, list["ApiListInspectionsLevel"]]:
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
                    levels_type_0_item = ApiListInspectionsLevel.from_dict(
                        levels_type_0_item_data
                    )

                    levels_type_0.append(levels_type_0_item)

                return levels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApiListInspectionsLevel"]], data)

        levels = _parse_levels(d.pop("levels", UNSET))

        api_list_inspections_fields = cls(
            id=id,
            type_=type_,
            name=name,
            help_text=help_text,
            options=options,
            levels=levels,
        )

        api_list_inspections_fields.additional_properties = d
        return api_list_inspections_fields

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

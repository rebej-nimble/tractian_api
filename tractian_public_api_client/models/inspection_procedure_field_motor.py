from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inspection_procedure_empty_value_motor import (
        InspectionProcedureEmptyValueMotor,
    )
    from ..models.inspection_procedure_field_alternative_value_motor import (
        InspectionProcedureFieldAlternativeValueMotor,
    )
    from ..models.inspection_procedure_value_motor import InspectionProcedureValueMotor
    from ..models.level_motor import LevelMotor
    from ..models.metrics_field_values_motor import MetricsFieldValuesMotor
    from ..models.option import Option


T = TypeVar("T", bound="InspectionProcedureFieldMotor")


@_attrs_define
class InspectionProcedureFieldMotor:
    id: str
    type_: str
    name: str
    help_text: Union[None, Unset, str] = UNSET
    options: Union[None, Unset, list["Option"]] = UNSET
    levels: Union[None, Unset, list["LevelMotor"]] = UNSET
    value: Union[
        "InspectionProcedureValueMotor",
        None,
        Unset,
        bool,
        float,
        int,
        list["InspectionProcedureFieldAlternativeValueMotor"],
        list["MetricsFieldValuesMotor"],
        list[Union["InspectionProcedureEmptyValueMotor", int]],
        list[int],
        str,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inspection_procedure_empty_value_motor import (
            InspectionProcedureEmptyValueMotor,
        )
        from ..models.inspection_procedure_value_motor import (
            InspectionProcedureValueMotor,
        )

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

        value: Union[
            None,
            Unset,
            bool,
            dict[str, Any],
            float,
            int,
            list[Union[dict[str, Any], int]],
            list[dict[str, Any]],
            list[int],
            str,
        ]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, InspectionProcedureValueMotor):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_5_item_data in self.value:
                value_type_5_item = value_type_5_item_data.to_dict()
                value.append(value_type_5_item)

        elif isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, list):
            value = []
            for value_type_7_item_data in self.value:
                value_type_7_item: Union[dict[str, Any], int]
                if isinstance(
                    value_type_7_item_data, InspectionProcedureEmptyValueMotor
                ):
                    value_type_7_item = value_type_7_item_data.to_dict()
                else:
                    value_type_7_item = value_type_7_item_data
                value.append(value_type_7_item)

        elif isinstance(self.value, list):
            value = []
            for value_type_8_item_data in self.value:
                value_type_8_item = value_type_8_item_data.to_dict()
                value.append(value_type_8_item)

        else:
            value = self.value

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
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inspection_procedure_empty_value_motor import (
            InspectionProcedureEmptyValueMotor,
        )
        from ..models.inspection_procedure_field_alternative_value_motor import (
            InspectionProcedureFieldAlternativeValueMotor,
        )
        from ..models.inspection_procedure_value_motor import (
            InspectionProcedureValueMotor,
        )
        from ..models.level_motor import LevelMotor
        from ..models.metrics_field_values_motor import MetricsFieldValuesMotor
        from ..models.option import Option

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

        def _parse_options(data: object) -> Union[None, Unset, list["Option"]]:
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
                    options_type_0_item = Option.from_dict(options_type_0_item_data)

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Option"]], data)

        options = _parse_options(d.pop("options", UNSET))

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

        def _parse_value(
            data: object,
        ) -> Union[
            "InspectionProcedureValueMotor",
            None,
            Unset,
            bool,
            float,
            int,
            list["InspectionProcedureFieldAlternativeValueMotor"],
            list["MetricsFieldValuesMotor"],
            list[Union["InspectionProcedureEmptyValueMotor", int]],
            list[int],
            str,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_4 = InspectionProcedureValueMotor.from_dict(data)

                return value_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_5 = []
                _value_type_5 = data
                for value_type_5_item_data in _value_type_5:
                    value_type_5_item = (
                        InspectionProcedureFieldAlternativeValueMotor.from_dict(
                            value_type_5_item_data
                        )
                    )

                    value_type_5.append(value_type_5_item)

                return value_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_6 = cast(list[int], data)

                return value_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_7 = []
                _value_type_7 = data
                for value_type_7_item_data in _value_type_7:

                    def _parse_value_type_7_item(
                        data: object,
                    ) -> Union["InspectionProcedureEmptyValueMotor", int]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_7_item_type_1 = (
                                InspectionProcedureEmptyValueMotor.from_dict(data)
                            )

                            return value_type_7_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(
                            Union["InspectionProcedureEmptyValueMotor", int], data
                        )

                    value_type_7_item = _parse_value_type_7_item(value_type_7_item_data)

                    value_type_7.append(value_type_7_item)

                return value_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_8 = []
                _value_type_8 = data
                for value_type_8_item_data in _value_type_8:
                    value_type_8_item = MetricsFieldValuesMotor.from_dict(
                        value_type_8_item_data
                    )

                    value_type_8.append(value_type_8_item)

                return value_type_8
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "InspectionProcedureValueMotor",
                    None,
                    Unset,
                    bool,
                    float,
                    int,
                    list["InspectionProcedureFieldAlternativeValueMotor"],
                    list["MetricsFieldValuesMotor"],
                    list[Union["InspectionProcedureEmptyValueMotor", int]],
                    list[int],
                    str,
                ],
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        inspection_procedure_field_motor = cls(
            id=id,
            type_=type_,
            name=name,
            help_text=help_text,
            options=options,
            levels=levels,
            value=value,
        )

        inspection_procedure_field_motor.additional_properties = d
        return inspection_procedure_field_motor

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

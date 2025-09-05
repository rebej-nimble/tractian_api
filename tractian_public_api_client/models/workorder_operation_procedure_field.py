from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_alternative_value_motor import ActivityAlternativeValueMotor
    from ..models.metrics_field_values import MetricsFieldValues
    from ..models.work_order_operation_procedure_empty_value_motor import (
        WorkOrderOperationProcedureEmptyValueMotor,
    )
    from ..models.work_order_operation_procedure_field_option import (
        WorkOrderOperationProcedureFieldOption,
    )
    from ..models.work_order_operation_procedure_value import (
        WorkOrderOperationProcedureValue,
    )


T = TypeVar("T", bound="WorkorderOperationProcedureField")


@_attrs_define
class WorkorderOperationProcedureField:
    id: str
    name: str
    type_: str
    notes: Union[None, Unset, str] = UNSET
    help_text: Union[None, Unset, str] = UNSET
    metric_ids: Union[None, Unset, list[str]] = UNSET
    value: Union[
        "WorkOrderOperationProcedureValue",
        None,
        Unset,
        bool,
        float,
        int,
        list["ActivityAlternativeValueMotor"],
        list["MetricsFieldValues"],
        list[Union["WorkOrderOperationProcedureEmptyValueMotor", int]],
        list[int],
        str,
    ] = UNSET
    options: Union[None, Unset, list["WorkOrderOperationProcedureFieldOption"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.work_order_operation_procedure_empty_value_motor import (
            WorkOrderOperationProcedureEmptyValueMotor,
        )
        from ..models.work_order_operation_procedure_value import (
            WorkOrderOperationProcedureValue,
        )

        id = self.id

        name = self.name

        type_ = self.type_

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        help_text: Union[None, Unset, str]
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        metric_ids: Union[None, Unset, list[str]]
        if isinstance(self.metric_ids, Unset):
            metric_ids = UNSET
        elif isinstance(self.metric_ids, list):
            metric_ids = self.metric_ids

        else:
            metric_ids = self.metric_ids

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
        elif isinstance(self.value, WorkOrderOperationProcedureValue):
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
                    value_type_7_item_data, WorkOrderOperationProcedureEmptyValueMotor
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if metric_ids is not UNSET:
            field_dict["metricIds"] = metric_ids
        if value is not UNSET:
            field_dict["value"] = value
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_alternative_value_motor import (
            ActivityAlternativeValueMotor,
        )
        from ..models.metrics_field_values import MetricsFieldValues
        from ..models.work_order_operation_procedure_empty_value_motor import (
            WorkOrderOperationProcedureEmptyValueMotor,
        )
        from ..models.work_order_operation_procedure_field_option import (
            WorkOrderOperationProcedureFieldOption,
        )
        from ..models.work_order_operation_procedure_value import (
            WorkOrderOperationProcedureValue,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        def _parse_metric_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metric_ids_type_0 = cast(list[str], data)

                return metric_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        metric_ids = _parse_metric_ids(d.pop("metricIds", UNSET))

        def _parse_value(
            data: object,
        ) -> Union[
            "WorkOrderOperationProcedureValue",
            None,
            Unset,
            bool,
            float,
            int,
            list["ActivityAlternativeValueMotor"],
            list["MetricsFieldValues"],
            list[Union["WorkOrderOperationProcedureEmptyValueMotor", int]],
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
                value_type_4 = WorkOrderOperationProcedureValue.from_dict(data)

                return value_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_5 = []
                _value_type_5 = data
                for value_type_5_item_data in _value_type_5:
                    value_type_5_item = ActivityAlternativeValueMotor.from_dict(
                        value_type_5_item_data
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
                    ) -> Union["WorkOrderOperationProcedureEmptyValueMotor", int]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_7_item_type_1 = (
                                WorkOrderOperationProcedureEmptyValueMotor.from_dict(
                                    data
                                )
                            )

                            return value_type_7_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(
                            Union["WorkOrderOperationProcedureEmptyValueMotor", int],
                            data,
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
                    value_type_8_item = MetricsFieldValues.from_dict(
                        value_type_8_item_data
                    )

                    value_type_8.append(value_type_8_item)

                return value_type_8
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "WorkOrderOperationProcedureValue",
                    None,
                    Unset,
                    bool,
                    float,
                    int,
                    list["ActivityAlternativeValueMotor"],
                    list["MetricsFieldValues"],
                    list[Union["WorkOrderOperationProcedureEmptyValueMotor", int]],
                    list[int],
                    str,
                ],
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        def _parse_options(
            data: object,
        ) -> Union[None, Unset, list["WorkOrderOperationProcedureFieldOption"]]:
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
                    options_type_0_item = (
                        WorkOrderOperationProcedureFieldOption.from_dict(
                            options_type_0_item_data
                        )
                    )

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["WorkOrderOperationProcedureFieldOption"]], data
            )

        options = _parse_options(d.pop("options", UNSET))

        workorder_operation_procedure_field = cls(
            id=id,
            name=name,
            type_=type_,
            notes=notes,
            help_text=help_text,
            metric_ids=metric_ids,
            value=value,
            options=options,
        )

        workorder_operation_procedure_field.additional_properties = d
        return workorder_operation_procedure_field

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

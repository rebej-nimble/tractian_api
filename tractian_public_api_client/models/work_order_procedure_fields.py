from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_order_file_value_motor import WorkOrderFileValueMotor
    from ..models.work_order_procedure_alternative_value_motor import (
        WorkOrderProcedureAlternativeValueMotor,
    )
    from ..models.work_order_procedure_empty_value_motor import (
        WorkOrderProcedureEmptyValueMotor,
    )
    from ..models.work_order_procedure_value_motor import WorkOrderProcedureValueMotor
    from ..models.work_order_signature_value_motor import WorkOrderSignatureValueMotor


T = TypeVar("T", bound="WorkOrderProcedureFields")


@_attrs_define
class WorkOrderProcedureFields:
    type_: str
    name: str
    help_text: Union[None, Unset, str] = UNSET
    value: Union[
        "WorkOrderProcedureValueMotor",
        "WorkOrderSignatureValueMotor",
        None,
        Unset,
        bool,
        float,
        int,
        list["WorkOrderFileValueMotor"],
        list["WorkOrderProcedureAlternativeValueMotor"],
        list[Union["WorkOrderProcedureEmptyValueMotor", int]],
        list[int],
        str,
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.work_order_procedure_empty_value_motor import (
            WorkOrderProcedureEmptyValueMotor,
        )
        from ..models.work_order_procedure_value_motor import (
            WorkOrderProcedureValueMotor,
        )
        from ..models.work_order_signature_value_motor import (
            WorkOrderSignatureValueMotor,
        )

        type_ = self.type_

        name = self.name

        help_text: Union[None, Unset, str]
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

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
        elif isinstance(self.value, WorkOrderProcedureValueMotor):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = []
            for value_type_5_item_data in self.value:
                value_type_5_item = value_type_5_item_data.to_dict()
                value.append(value_type_5_item)

        elif isinstance(self.value, list):
            value = []
            for value_type_6_item_data in self.value:
                value_type_6_item = value_type_6_item_data.to_dict()
                value.append(value_type_6_item)

        elif isinstance(self.value, WorkOrderSignatureValueMotor):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, list):
            value = []
            for value_type_9_item_data in self.value:
                value_type_9_item: Union[dict[str, Any], int]
                if isinstance(
                    value_type_9_item_data, WorkOrderProcedureEmptyValueMotor
                ):
                    value_type_9_item = value_type_9_item_data.to_dict()
                else:
                    value_type_9_item = value_type_9_item_data
                value.append(value_type_9_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_order_file_value_motor import WorkOrderFileValueMotor
        from ..models.work_order_procedure_alternative_value_motor import (
            WorkOrderProcedureAlternativeValueMotor,
        )
        from ..models.work_order_procedure_empty_value_motor import (
            WorkOrderProcedureEmptyValueMotor,
        )
        from ..models.work_order_procedure_value_motor import (
            WorkOrderProcedureValueMotor,
        )
        from ..models.work_order_signature_value_motor import (
            WorkOrderSignatureValueMotor,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        def _parse_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        def _parse_value(
            data: object,
        ) -> Union[
            "WorkOrderProcedureValueMotor",
            "WorkOrderSignatureValueMotor",
            None,
            Unset,
            bool,
            float,
            int,
            list["WorkOrderFileValueMotor"],
            list["WorkOrderProcedureAlternativeValueMotor"],
            list[Union["WorkOrderProcedureEmptyValueMotor", int]],
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
                value_type_4 = WorkOrderProcedureValueMotor.from_dict(data)

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
                        WorkOrderProcedureAlternativeValueMotor.from_dict(
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
                value_type_6 = []
                _value_type_6 = data
                for value_type_6_item_data in _value_type_6:
                    value_type_6_item = WorkOrderFileValueMotor.from_dict(
                        value_type_6_item_data
                    )

                    value_type_6.append(value_type_6_item)

                return value_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_7 = WorkOrderSignatureValueMotor.from_dict(data)

                return value_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_8 = cast(list[int], data)

                return value_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_9 = []
                _value_type_9 = data
                for value_type_9_item_data in _value_type_9:

                    def _parse_value_type_9_item(
                        data: object,
                    ) -> Union["WorkOrderProcedureEmptyValueMotor", int]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            value_type_9_item_type_1 = (
                                WorkOrderProcedureEmptyValueMotor.from_dict(data)
                            )

                            return value_type_9_item_type_1
                        except:  # noqa: E722
                            pass
                        return cast(
                            Union["WorkOrderProcedureEmptyValueMotor", int], data
                        )

                    value_type_9_item = _parse_value_type_9_item(value_type_9_item_data)

                    value_type_9.append(value_type_9_item)

                return value_type_9
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "WorkOrderProcedureValueMotor",
                    "WorkOrderSignatureValueMotor",
                    None,
                    Unset,
                    bool,
                    float,
                    int,
                    list["WorkOrderFileValueMotor"],
                    list["WorkOrderProcedureAlternativeValueMotor"],
                    list[Union["WorkOrderProcedureEmptyValueMotor", int]],
                    list[int],
                    str,
                ],
                data,
            )

        value = _parse_value(d.pop("value", UNSET))

        work_order_procedure_fields = cls(
            type_=type_,
            name=name,
            help_text=help_text,
            value=value,
        )

        work_order_procedure_fields.additional_properties = d
        return work_order_procedure_fields

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

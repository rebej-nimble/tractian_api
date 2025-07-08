from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_info_request_motor_option_type_0 import (
        ParentInfoRequestMotorOptionType0,
    )
    from ..models.parent_work_order_operation_procedure_request_motor import (
        ParentWorkOrderOperationProcedureRequestMotor,
    )


T = TypeVar("T", bound="ParentInfoRequestMotor")


@_attrs_define
class ParentInfoRequestMotor:
    work_order_operation_procedure_id: str
    work_order_operation_procedure_field_id: str
    option: Union["ParentInfoRequestMotorOptionType0", int]
    parent_work_order_operation_procedure: Union[
        "ParentWorkOrderOperationProcedureRequestMotor", None, Unset
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.parent_info_request_motor_option_type_0 import (
            ParentInfoRequestMotorOptionType0,
        )
        from ..models.parent_work_order_operation_procedure_request_motor import (
            ParentWorkOrderOperationProcedureRequestMotor,
        )

        work_order_operation_procedure_id = self.work_order_operation_procedure_id

        work_order_operation_procedure_field_id = (
            self.work_order_operation_procedure_field_id
        )

        option: Union[dict[str, Any], int]
        if isinstance(self.option, ParentInfoRequestMotorOptionType0):
            option = self.option.to_dict()
        else:
            option = self.option

        parent_work_order_operation_procedure: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent_work_order_operation_procedure, Unset):
            parent_work_order_operation_procedure = UNSET
        elif isinstance(
            self.parent_work_order_operation_procedure,
            ParentWorkOrderOperationProcedureRequestMotor,
        ):
            parent_work_order_operation_procedure = (
                self.parent_work_order_operation_procedure.to_dict()
            )
        else:
            parent_work_order_operation_procedure = (
                self.parent_work_order_operation_procedure
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workOrderOperationProcedureId": work_order_operation_procedure_id,
                "workOrderOperationProcedureFieldId": work_order_operation_procedure_field_id,
                "option": option,
            }
        )
        if parent_work_order_operation_procedure is not UNSET:
            field_dict["parentWorkOrderOperationProcedure"] = (
                parent_work_order_operation_procedure
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parent_info_request_motor_option_type_0 import (
            ParentInfoRequestMotorOptionType0,
        )
        from ..models.parent_work_order_operation_procedure_request_motor import (
            ParentWorkOrderOperationProcedureRequestMotor,
        )

        d = dict(src_dict)
        work_order_operation_procedure_id = d.pop("workOrderOperationProcedureId")

        work_order_operation_procedure_field_id = d.pop(
            "workOrderOperationProcedureFieldId"
        )

        def _parse_option(
            data: object,
        ) -> Union["ParentInfoRequestMotorOptionType0", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                option_type_0 = ParentInfoRequestMotorOptionType0.from_dict(data)

                return option_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ParentInfoRequestMotorOptionType0", int], data)

        option = _parse_option(d.pop("option"))

        def _parse_parent_work_order_operation_procedure(
            data: object,
        ) -> Union["ParentWorkOrderOperationProcedureRequestMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_work_order_operation_procedure_type_0 = (
                    ParentWorkOrderOperationProcedureRequestMotor.from_dict(data)
                )

                return parent_work_order_operation_procedure_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["ParentWorkOrderOperationProcedureRequestMotor", None, Unset],
                data,
            )

        parent_work_order_operation_procedure = (
            _parse_parent_work_order_operation_procedure(
                d.pop("parentWorkOrderOperationProcedure", UNSET)
            )
        )

        parent_info_request_motor = cls(
            work_order_operation_procedure_id=work_order_operation_procedure_id,
            work_order_operation_procedure_field_id=work_order_operation_procedure_field_id,
            option=option,
            parent_work_order_operation_procedure=parent_work_order_operation_procedure,
        )

        parent_info_request_motor.additional_properties = d
        return parent_info_request_motor

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

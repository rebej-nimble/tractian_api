from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.inspection_procedure_option_value import (
        InspectionProcedureOptionValue,
    )


T = TypeVar("T", bound="UpdateInspectionProcedureTractianRequest")


@_attrs_define
class UpdateInspectionProcedureTractianRequest:
    value: Union["InspectionProcedureOptionValue", None, bool, list[int], str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inspection_procedure_option_value import (
            InspectionProcedureOptionValue,
        )

        value: Union[None, bool, dict[str, Any], list[int], str]
        if isinstance(self.value, list):
            value = self.value

        elif isinstance(self.value, InspectionProcedureOptionValue):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inspection_procedure_option_value import (
            InspectionProcedureOptionValue,
        )

        d = dict(src_dict)

        def _parse_value(
            data: object,
        ) -> Union["InspectionProcedureOptionValue", None, bool, list[int], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = cast(list[int], data)

                return value_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = InspectionProcedureOptionValue.from_dict(data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union["InspectionProcedureOptionValue", None, bool, list[int], str],
                data,
            )

        value = _parse_value(d.pop("value"))

        update_inspection_procedure_tractian_request = cls(
            value=value,
        )

        update_inspection_procedure_tractian_request.additional_properties = d
        return update_inspection_procedure_tractian_request

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

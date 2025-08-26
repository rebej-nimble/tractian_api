from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workorder_operation_procedure_field import (
        WorkorderOperationProcedureField,
    )


T = TypeVar("T", bound="WorkorderOperationProcedure")


@_attrs_define
class WorkorderOperationProcedure:
    id: str
    title: str
    fields: list["WorkorderOperationProcedureField"]
    procedure_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        procedure_id: Union[None, Unset, str]
        if isinstance(self.procedure_id, Unset):
            procedure_id = UNSET
        else:
            procedure_id = self.procedure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "fields": fields,
            }
        )
        if procedure_id is not UNSET:
            field_dict["procedureId"] = procedure_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workorder_operation_procedure_field import (
            WorkorderOperationProcedureField,
        )

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = WorkorderOperationProcedureField.from_dict(fields_item_data)

            fields.append(fields_item)

        def _parse_procedure_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        procedure_id = _parse_procedure_id(d.pop("procedureId", UNSET))

        workorder_operation_procedure = cls(
            id=id,
            title=title,
            fields=fields,
            procedure_id=procedure_id,
        )

        workorder_operation_procedure.additional_properties = d
        return workorder_operation_procedure

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

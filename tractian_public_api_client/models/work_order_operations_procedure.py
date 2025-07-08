from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_order_operations_procedure_fields import (
        WorkOrderOperationsProcedureFields,
    )


T = TypeVar("T", bound="WorkOrderOperationsProcedure")


@_attrs_define
class WorkOrderOperationsProcedure:
    fields: list["WorkOrderOperationsProcedureFields"]
    name: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_order_operations_procedure_fields import (
            WorkOrderOperationsProcedureFields,
        )

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = WorkOrderOperationsProcedureFields.from_dict(fields_item_data)

            fields.append(fields_item)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        work_order_operations_procedure = cls(
            fields=fields,
            name=name,
            title=title,
        )

        work_order_operations_procedure.additional_properties = d
        return work_order_operations_procedure

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

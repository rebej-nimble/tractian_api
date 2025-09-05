from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_list_inspections_fields import ApiListInspectionsFields


T = TypeVar("T", bound="ApiListInspectionsProcedure")


@_attrs_define
class ApiListInspectionsProcedure:
    title: str
    id: str
    fields: list["ApiListInspectionsFields"]
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        id = self.id

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "id": id,
                "fields": fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_list_inspections_fields import ApiListInspectionsFields

        d = dict(src_dict)
        title = d.pop("title")

        id = d.pop("id")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = ApiListInspectionsFields.from_dict(fields_item_data)

            fields.append(fields_item)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        api_list_inspections_procedure = cls(
            title=title,
            id=id,
            fields=fields,
            description=description,
        )

        api_list_inspections_procedure.additional_properties = d
        return api_list_inspections_procedure

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

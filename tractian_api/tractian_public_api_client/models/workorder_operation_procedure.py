from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checklist import Checklist
    from ..models.heading import Heading
    from ..models.inspection_custom import InspectionCustom
    from ..models.inspection_list import InspectionList
    from ..models.metrics import Metrics
    from ..models.yes_no_custom import YesNoCustom


T = TypeVar("T", bound="WorkorderOperationProcedure")


@_attrs_define
class WorkorderOperationProcedure:
    id: str
    title: str
    fields: list[
        Union[
            "Checklist",
            "Heading",
            "InspectionCustom",
            "InspectionList",
            "Metrics",
            "YesNoCustom",
        ]
    ]
    procedure_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checklist import Checklist
        from ..models.heading import Heading
        from ..models.inspection_custom import InspectionCustom
        from ..models.metrics import Metrics
        from ..models.yes_no_custom import YesNoCustom

        id = self.id

        title = self.title

        fields = []
        for fields_item_data in self.fields:
            fields_item: dict[str, Any]
            if isinstance(fields_item_data, Heading):
                fields_item = fields_item_data.to_dict()
            elif isinstance(fields_item_data, Metrics):
                fields_item = fields_item_data.to_dict()
            elif isinstance(fields_item_data, InspectionCustom):
                fields_item = fields_item_data.to_dict()
            elif isinstance(fields_item_data, Checklist):
                fields_item = fields_item_data.to_dict()
            elif isinstance(fields_item_data, YesNoCustom):
                fields_item = fields_item_data.to_dict()
            else:
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
        from ..models.checklist import Checklist
        from ..models.heading import Heading
        from ..models.inspection_custom import InspectionCustom
        from ..models.inspection_list import InspectionList
        from ..models.metrics import Metrics
        from ..models.yes_no_custom import YesNoCustom

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:

            def _parse_fields_item(
                data: object,
            ) -> Union[
                "Checklist",
                "Heading",
                "InspectionCustom",
                "InspectionList",
                "Metrics",
                "YesNoCustom",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    fields_item_type_0 = Heading.from_dict(data)

                    return fields_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    fields_item_type_1 = Metrics.from_dict(data)

                    return fields_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    fields_item_type_2 = InspectionCustom.from_dict(data)

                    return fields_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    fields_item_type_3 = Checklist.from_dict(data)

                    return fields_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    fields_item_type_4 = YesNoCustom.from_dict(data)

                    return fields_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                fields_item_type_5 = InspectionList.from_dict(data)

                return fields_item_type_5

            fields_item = _parse_fields_item(fields_item_data)

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

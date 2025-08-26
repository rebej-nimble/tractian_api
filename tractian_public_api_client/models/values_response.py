from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.head_values_response import HeadValuesResponse


T = TypeVar("T", bound="ValuesResponse")


@_attrs_define
class ValuesResponse:
    head: Union["HeadValuesResponse", None, Unset] = UNSET
    records: Union[None, Unset, list[list[Union[float, int]]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.head_values_response import HeadValuesResponse

        head: Union[None, Unset, dict[str, Any]]
        if isinstance(self.head, Unset):
            head = UNSET
        elif isinstance(self.head, HeadValuesResponse):
            head = self.head.to_dict()
        else:
            head = self.head

        records: Union[None, Unset, list[list[Union[float, int]]]]
        if isinstance(self.records, Unset):
            records = UNSET
        elif isinstance(self.records, list):
            records = []
            for records_type_0_item_data in self.records:
                records_type_0_item = []
                for records_type_0_item_item_data in records_type_0_item_data:
                    records_type_0_item_item: Union[float, int]
                    records_type_0_item_item = records_type_0_item_item_data
                    records_type_0_item.append(records_type_0_item_item)

                records.append(records_type_0_item)

        else:
            records = self.records

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if head is not UNSET:
            field_dict["head"] = head
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.head_values_response import HeadValuesResponse

        d = dict(src_dict)

        def _parse_head(data: object) -> Union["HeadValuesResponse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                head_type_0 = HeadValuesResponse.from_dict(data)

                return head_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HeadValuesResponse", None, Unset], data)

        head = _parse_head(d.pop("head", UNSET))

        def _parse_records(
            data: object,
        ) -> Union[None, Unset, list[list[Union[float, int]]]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = []
                _records_type_0 = data
                for records_type_0_item_data in _records_type_0:
                    records_type_0_item = []
                    _records_type_0_item = records_type_0_item_data
                    for records_type_0_item_item_data in _records_type_0_item:

                        def _parse_records_type_0_item_item(
                            data: object,
                        ) -> Union[float, int]:
                            return cast(Union[float, int], data)

                        records_type_0_item_item = _parse_records_type_0_item_item(
                            records_type_0_item_item_data
                        )

                        records_type_0_item.append(records_type_0_item_item)

                    records_type_0.append(records_type_0_item)

                return records_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[list[Union[float, int]]]], data)

        records = _parse_records(d.pop("records", UNSET))

        values_response = cls(
            head=head,
            records=records,
        )

        values_response.additional_properties = d
        return values_response

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

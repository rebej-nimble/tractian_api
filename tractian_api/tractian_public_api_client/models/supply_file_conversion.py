from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SupplyFileConversion")


@_attrs_define
class SupplyFileConversion:
    input_: Union[None, str]
    output: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_: Union[None, str]
        input_ = self.input_

        output: Union[None, str]
        output = self.output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "output": output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_input_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        input_ = _parse_input_(d.pop("input"))

        def _parse_output(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        output = _parse_output(d.pop("output"))

        supply_file_conversion = cls(
            input_=input_,
            output=output,
        )

        supply_file_conversion.additional_properties = d
        return supply_file_conversion

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

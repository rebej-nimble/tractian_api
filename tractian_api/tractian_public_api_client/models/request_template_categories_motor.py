from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestTemplateCategoriesMotor")


@_attrs_define
class RequestTemplateCategoriesMotor:
    id: str
    name: str
    color: str
    company_id: str
    code: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    is_corrective: Union[None, Unset, bool] = UNSET
    is_preventive: Union[None, Unset, bool] = UNSET
    include_in_indicators: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        company_id = self.company_id

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_corrective: Union[None, Unset, bool]
        if isinstance(self.is_corrective, Unset):
            is_corrective = UNSET
        else:
            is_corrective = self.is_corrective

        is_preventive: Union[None, Unset, bool]
        if isinstance(self.is_preventive, Unset):
            is_preventive = UNSET
        else:
            is_preventive = self.is_preventive

        include_in_indicators: Union[None, Unset, bool]
        if isinstance(self.include_in_indicators, Unset):
            include_in_indicators = UNSET
        else:
            include_in_indicators = self.include_in_indicators

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
                "companyId": company_id,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if is_corrective is not UNSET:
            field_dict["isCorrective"] = is_corrective
        if is_preventive is not UNSET:
            field_dict["isPreventive"] = is_preventive
        if include_in_indicators is not UNSET:
            field_dict["includeInIndicators"] = include_in_indicators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        color = d.pop("color")

        company_id = d.pop("companyId")

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_corrective(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_corrective = _parse_is_corrective(d.pop("isCorrective", UNSET))

        def _parse_is_preventive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_preventive = _parse_is_preventive(d.pop("isPreventive", UNSET))

        def _parse_include_in_indicators(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_in_indicators = _parse_include_in_indicators(
            d.pop("includeInIndicators", UNSET)
        )

        request_template_categories_motor = cls(
            id=id,
            name=name,
            color=color,
            company_id=company_id,
            code=code,
            description=description,
            is_corrective=is_corrective,
            is_preventive=is_preventive,
            include_in_indicators=include_in_indicators,
        )

        request_template_categories_motor.additional_properties = d
        return request_template_categories_motor

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

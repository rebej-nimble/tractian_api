from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.priority_motor import PriorityMotor


T = TypeVar("T", bound="ApiCategoryMotorResponse")


@_attrs_define
class ApiCategoryMotorResponse:
    id: str
    """ Unique identifier of the category. """
    name: str
    """ Name of the category. """
    company_id: str
    """ Identifier of the company to which the category belongs. """
    color: str
    """ Color code associated with the category. """
    code: Union[None, Unset, str] = UNSET
    """ Optional code for the category. """
    type_: Union[None, Unset, str] = UNSET
    """ Optional type of the category. """
    description: Union[None, Unset, str] = UNSET
    """ Optional description of the category. """
    disabled: Union[None, Unset, bool] = UNSET
    """ Indicates if the category is disabled. """
    include_in_indicators: Union[None, Unset, bool] = UNSET
    """ Whether to include this category in indicators. """
    priority_id: Union[None, Unset, str] = UNSET
    """ Identifier for the priority associated with the category. """
    priority: Union["PriorityMotor", None, Unset] = UNSET
    """ Priority details for the category. """
    is_preventive: Union[None, Unset, bool] = UNSET
    """ Indicates if the category is preventive. """
    is_corrective: Union[None, Unset, bool] = UNSET
    """ Indicates if the category is corrective. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.priority_motor import PriorityMotor

        id = self.id

        name = self.name

        company_id = self.company_id

        color = self.color

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        disabled: Union[None, Unset, bool]
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        include_in_indicators: Union[None, Unset, bool]
        if isinstance(self.include_in_indicators, Unset):
            include_in_indicators = UNSET
        else:
            include_in_indicators = self.include_in_indicators

        priority_id: Union[None, Unset, str]
        if isinstance(self.priority_id, Unset):
            priority_id = UNSET
        else:
            priority_id = self.priority_id

        priority: Union[None, Unset, dict[str, Any]]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, PriorityMotor):
            priority = self.priority.to_dict()
        else:
            priority = self.priority

        is_preventive: Union[None, Unset, bool]
        if isinstance(self.is_preventive, Unset):
            is_preventive = UNSET
        else:
            is_preventive = self.is_preventive

        is_corrective: Union[None, Unset, bool]
        if isinstance(self.is_corrective, Unset):
            is_corrective = UNSET
        else:
            is_corrective = self.is_corrective

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "companyId": company_id,
                "color": color,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if include_in_indicators is not UNSET:
            field_dict["includeInIndicators"] = include_in_indicators
        if priority_id is not UNSET:
            field_dict["priorityId"] = priority_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if is_preventive is not UNSET:
            field_dict["isPreventive"] = is_preventive
        if is_corrective is not UNSET:
            field_dict["isCorrective"] = is_corrective

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.priority_motor import PriorityMotor

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        company_id = d.pop("companyId")

        color = d.pop("color")

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_disabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))

        def _parse_include_in_indicators(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_in_indicators = _parse_include_in_indicators(
            d.pop("includeInIndicators", UNSET)
        )

        def _parse_priority_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        priority_id = _parse_priority_id(d.pop("priorityId", UNSET))

        def _parse_priority(data: object) -> Union["PriorityMotor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                priority_type_0 = PriorityMotor.from_dict(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PriorityMotor", None, Unset], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_is_preventive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_preventive = _parse_is_preventive(d.pop("isPreventive", UNSET))

        def _parse_is_corrective(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_corrective = _parse_is_corrective(d.pop("isCorrective", UNSET))

        api_category_motor_response = cls(
            id=id,
            name=name,
            company_id=company_id,
            color=color,
            code=code,
            type_=type_,
            description=description,
            disabled=disabled,
            include_in_indicators=include_in_indicators,
            priority_id=priority_id,
            priority=priority,
            is_preventive=is_preventive,
            is_corrective=is_corrective,
        )

        api_category_motor_response.additional_properties = d
        return api_category_motor_response

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

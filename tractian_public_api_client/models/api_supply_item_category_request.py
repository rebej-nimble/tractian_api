from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_category_type_enum import (
    ItemCategoryTypeEnum,
    check_item_category_type_enum,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyItemCategoryRequest")


@_attrs_define
class ApiSupplyItemCategoryRequest:
    name: Union[None, Unset, str] = UNSET
    """ The name of the item category """
    company_id: Union[None, Unset, str] = UNSET
    """ The id of the company """
    type_: Union[ItemCategoryTypeEnum, None, Unset] = UNSET
    """ The type of the item category """
    color: Union[None, Unset, str] = "#972D35"
    """ The color of the item category. if not provided, a random color will be generated """
    description: Union[None, Unset, str] = UNSET
    """ The description of the item category """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time the item category was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time the item category was updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who created the item category """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The id of the user who updated the item category """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, str):
            type_ = self.type_
        else:
            type_ = self.type_

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_type_(data: object) -> Union[ItemCategoryTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = check_item_category_type_enum(data)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ItemCategoryTypeEnum, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        api_supply_item_category_request = cls(
            name=name,
            company_id=company_id,
            type_=type_,
            color=color,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
        )

        api_supply_item_category_request.additional_properties = d
        return api_supply_item_category_request

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

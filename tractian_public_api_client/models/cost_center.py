from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostCenter")


@_attrs_define
class CostCenter:
    company_id: str
    """ ID of the company that owns the cost center """
    name: str
    """ Human-readable name of the cost center """
    identifier_code: Union[None, Unset, str] = UNSET
    """ External identifier code used for element integration """
    description: Union[None, Unset, str] = UNSET
    """ Detailed description of the cost center purpose and usage """
    cost_center_code: Union[None, Unset, str] = UNSET
    """ Cost center code used in external accounting systems """
    parent_id: Union[None, Unset, str] = UNSET
    """ ID of the parent cost center for hierarchical organization """
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    """ List of user IDs that have access to this cost center """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ List of team IDs that have access to this cost center """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name = self.name

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cost_center_code: Union[None, Unset, str]
        if isinstance(self.cost_center_code, Unset):
            cost_center_code = UNSET
        else:
            cost_center_code = self.cost_center_code

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        assigned_user_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = UNSET
        elif isinstance(self.assigned_user_ids, list):
            assigned_user_ids = self.assigned_user_ids

        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "name": name,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if description is not UNSET:
            field_dict["description"] = description
        if cost_center_code is not UNSET:
            field_dict["costCenterCode"] = cost_center_code
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId")

        name = d.pop("name")

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cost_center_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_center_code = _parse_cost_center_code(d.pop("costCenterCode", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_assigned_user_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_user_ids_type_0 = cast(list[str], data)

                return assigned_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds", UNSET))

        def _parse_assigned_team_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds", UNSET))

        cost_center = cls(
            company_id=company_id,
            name=name,
            identifier_code=identifier_code,
            description=description,
            cost_center_code=cost_center_code,
            parent_id=parent_id,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
        )

        cost_center.additional_properties = d
        return cost_center

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

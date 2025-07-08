from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.requests_template_category import RequestsTemplateCategory
    from ..models.requests_template_identified_asset_failures import (
        RequestsTemplateIdentifiedAssetFailures,
    )


T = TypeVar("T", bound="RequestsTemplate")


@_attrs_define
class RequestsTemplate:
    title: Union[None, Unset, str] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    category_ids: Union[None, Unset, list[str]] = UNSET
    categories: Union[None, Unset, list["RequestsTemplateCategory"]] = UNSET
    assigned_team_ids: Union[Unset, list[str]] = UNSET
    assigned_user_ids: Union[Unset, list[str]] = UNSET
    identified_asset_failures: Union[
        Unset, list["RequestsTemplateIdentifiedAssetFailures"]
    ] = UNSET
    linked_work_order_ids: Union[Unset, list[str]] = UNSET
    linked_request_ids: Union[Unset, list[str]] = UNSET
    description: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    priority_id: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    company_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        asset_id: Union[None, Unset, str]
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = self.asset_id

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        category_ids: Union[None, Unset, list[str]]
        if isinstance(self.category_ids, Unset):
            category_ids = UNSET
        elif isinstance(self.category_ids, list):
            category_ids = self.category_ids

        else:
            category_ids = self.category_ids

        categories: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        assigned_team_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = self.assigned_team_ids

        assigned_user_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = self.assigned_user_ids

        identified_asset_failures: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.identified_asset_failures, Unset):
            identified_asset_failures = []
            for identified_asset_failures_item_data in self.identified_asset_failures:
                identified_asset_failures_item = (
                    identified_asset_failures_item_data.to_dict()
                )
                identified_asset_failures.append(identified_asset_failures_item)

        linked_work_order_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.linked_work_order_ids, Unset):
            linked_work_order_ids = self.linked_work_order_ids

        linked_request_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.linked_request_ids, Unset):
            linked_request_ids = self.linked_request_ids

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        priority_id: Union[None, Unset, str]
        if isinstance(self.priority_id, Unset):
            priority_id = UNSET
        else:
            priority_id = self.priority_id

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if category_ids is not UNSET:
            field_dict["categoryIds"] = category_ids
        if categories is not UNSET:
            field_dict["categories"] = categories
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if identified_asset_failures is not UNSET:
            field_dict["identifiedAssetFailures"] = identified_asset_failures
        if linked_work_order_ids is not UNSET:
            field_dict["linkedWorkOrderIds"] = linked_work_order_ids
        if linked_request_ids is not UNSET:
            field_dict["linkedRequestIds"] = linked_request_ids
        if description is not UNSET:
            field_dict["description"] = description
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if priority_id is not UNSET:
            field_dict["priorityId"] = priority_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if company_id is not UNSET:
            field_dict["companyId"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requests_template_category import RequestsTemplateCategory
        from ..models.requests_template_identified_asset_failures import (
            RequestsTemplateIdentifiedAssetFailures,
        )

        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_asset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_id = _parse_asset_id(d.pop("assetId", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        def _parse_category_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                category_ids_type_0 = cast(list[str], data)

                return category_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        category_ids = _parse_category_ids(d.pop("categoryIds", UNSET))

        def _parse_categories(
            data: object,
        ) -> Union[None, Unset, list["RequestsTemplateCategory"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = RequestsTemplateCategory.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["RequestsTemplateCategory"]], data)

        categories = _parse_categories(d.pop("categories", UNSET))

        assigned_team_ids = cast(list[str], d.pop("assignedTeamIds", UNSET))

        assigned_user_ids = cast(list[str], d.pop("assignedUserIds", UNSET))

        identified_asset_failures = []
        _identified_asset_failures = d.pop("identifiedAssetFailures", UNSET)
        for identified_asset_failures_item_data in _identified_asset_failures or []:
            identified_asset_failures_item = (
                RequestsTemplateIdentifiedAssetFailures.from_dict(
                    identified_asset_failures_item_data
                )
            )

            identified_asset_failures.append(identified_asset_failures_item)

        linked_work_order_ids = cast(list[str], d.pop("linkedWorkOrderIds", UNSET))

        linked_request_ids = cast(list[str], d.pop("linkedRequestIds", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_priority_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        priority_id = _parse_priority_id(d.pop("priorityId", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        requests_template = cls(
            title=title,
            asset_id=asset_id,
            location_id=location_id,
            category_ids=category_ids,
            categories=categories,
            assigned_team_ids=assigned_team_ids,
            assigned_user_ids=assigned_user_ids,
            identified_asset_failures=identified_asset_failures,
            linked_work_order_ids=linked_work_order_ids,
            linked_request_ids=linked_request_ids,
            description=description,
            parent_id=parent_id,
            priority_id=priority_id,
            tags=tags,
            company_id=company_id,
        )

        requests_template.additional_properties = d
        return requests_template

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

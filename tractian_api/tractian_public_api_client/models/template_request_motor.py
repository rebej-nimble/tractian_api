from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_custom_field import EntityCustomField
    from ..models.request_template_categories_motor import (
        RequestTemplateCategoriesMotor,
    )
    from ..models.template_request_motor_asset_failures import (
        TemplateRequestMotorAssetFailures,
    )
    from ..models.template_request_motor_attachment import (
        TemplateRequestMotorAttachment,
    )


T = TypeVar("T", bound="TemplateRequestMotor")


@_attrs_define
class TemplateRequestMotor:
    title: Union[None, Unset, str] = UNSET
    custom_fields: Union[Unset, list["EntityCustomField"]] = UNSET
    asset_id: Union[None, Unset, str] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    category_ids: Union[None, Unset, list[str]] = UNSET
    categories: Union[None, Unset, list["RequestTemplateCategoriesMotor"]] = UNSET
    assigned_team_ids: Union[Unset, list[str]] = UNSET
    assigned_user_ids: Union[Unset, list[str]] = UNSET
    identified_asset_failures: Union[
        Unset, list["TemplateRequestMotorAssetFailures"]
    ] = UNSET
    linked_work_order_ids: Union[Unset, list[str]] = UNSET
    linked_request_ids: Union[Unset, list[str]] = UNSET
    description: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    priority_id: Union[None, Unset, str] = UNSET
    attachments: Union[None, Unset, list["TemplateRequestMotorAttachment"]] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    company_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

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

        attachments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

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
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
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
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if company_id is not UNSET:
            field_dict["companyId"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_custom_field import EntityCustomField
        from ..models.request_template_categories_motor import (
            RequestTemplateCategoriesMotor,
        )
        from ..models.template_request_motor_asset_failures import (
            TemplateRequestMotorAssetFailures,
        )
        from ..models.template_request_motor_attachment import (
            TemplateRequestMotorAttachment,
        )

        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = EntityCustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

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
        ) -> Union[None, Unset, list["RequestTemplateCategoriesMotor"]]:
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
                    categories_type_0_item = RequestTemplateCategoriesMotor.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["RequestTemplateCategoriesMotor"]], data
            )

        categories = _parse_categories(d.pop("categories", UNSET))

        assigned_team_ids = cast(list[str], d.pop("assignedTeamIds", UNSET))

        assigned_user_ids = cast(list[str], d.pop("assignedUserIds", UNSET))

        identified_asset_failures = []
        _identified_asset_failures = d.pop("identifiedAssetFailures", UNSET)
        for identified_asset_failures_item_data in _identified_asset_failures or []:
            identified_asset_failures_item = (
                TemplateRequestMotorAssetFailures.from_dict(
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

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["TemplateRequestMotorAttachment"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = TemplateRequestMotorAttachment.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["TemplateRequestMotorAttachment"]], data
            )

        attachments = _parse_attachments(d.pop("attachments", UNSET))

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

        template_request_motor = cls(
            title=title,
            custom_fields=custom_fields,
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
            attachments=attachments,
            tags=tags,
            company_id=company_id,
        )

        template_request_motor.additional_properties = d
        return template_request_motor

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

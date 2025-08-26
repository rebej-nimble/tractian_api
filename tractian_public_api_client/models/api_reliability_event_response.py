from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_reliability_event_insight_response import (
        ApiReliabilityEventInsightResponse,
    )


T = TypeVar("T", bound="ApiReliabilityEventResponse")


@_attrs_define
class ApiReliabilityEventResponse:
    id: str
    """ Unique identifier of the event. """
    type_: str
    """ Type of the event. """
    company_id: str
    """ Identifier of the company to which the event belongs. """
    created_at: str
    """ Timestamp when the event was created. """
    created_by_user_id: str
    """ Identifier of the user who created the event. """
    asset_id: Union[None, Unset, str] = UNSET
    """ Optional identifier of the asset related to the event. """
    location_id: Union[None, Unset, str] = UNSET
    """ Optional identifier of the location related to the event. """
    description: Union[None, Unset, str] = UNSET
    """ Optional description of the event. """
    start_date: Union[None, Unset, str] = UNSET
    """ Optional start date of the event. """
    end_date: Union[None, Unset, str] = UNSET
    """ Optional end date of the event. """
    insights: Union[None, Unset, list["ApiReliabilityEventInsightResponse"]] = UNSET
    """ List of insights associated with the event. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        company_id = self.company_id

        created_at = self.created_at

        created_by_user_id = self.created_by_user_id

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

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        insights: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.insights, Unset):
            insights = UNSET
        elif isinstance(self.insights, list):
            insights = []
            for insights_type_0_item_data in self.insights:
                insights_type_0_item = insights_type_0_item_data.to_dict()
                insights.append(insights_type_0_item)

        else:
            insights = self.insights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "companyId": company_id,
                "createdAt": created_at,
                "createdByUserId": created_by_user_id,
            }
        )
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if insights is not UNSET:
            field_dict["insights"] = insights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_reliability_event_insight_response import (
            ApiReliabilityEventInsightResponse,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        company_id = d.pop("companyId")

        created_at = d.pop("createdAt")

        created_by_user_id = d.pop("createdByUserId")

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_insights(
            data: object,
        ) -> Union[None, Unset, list["ApiReliabilityEventInsightResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                insights_type_0 = []
                _insights_type_0 = data
                for insights_type_0_item_data in _insights_type_0:
                    insights_type_0_item = ApiReliabilityEventInsightResponse.from_dict(
                        insights_type_0_item_data
                    )

                    insights_type_0.append(insights_type_0_item)

                return insights_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ApiReliabilityEventInsightResponse"]], data
            )

        insights = _parse_insights(d.pop("insights", UNSET))

        api_reliability_event_response = cls(
            id=id,
            type_=type_,
            company_id=company_id,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            asset_id=asset_id,
            location_id=location_id,
            description=description,
            start_date=start_date,
            end_date=end_date,
            insights=insights,
        )

        api_reliability_event_response.additional_properties = d
        return api_reliability_event_response

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

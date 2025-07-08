from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsightCerberus")


@_attrs_define
class InsightCerberus:
    id: str
    type_: str
    number: int
    created_at: str
    asset_id: str
    inspection_id: Union[None, Unset, str] = UNSET
    event_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        number = self.number

        created_at = self.created_at

        asset_id = self.asset_id

        inspection_id: Union[None, Unset, str]
        if isinstance(self.inspection_id, Unset):
            inspection_id = UNSET
        else:
            inspection_id = self.inspection_id

        event_id: Union[None, Unset, str]
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "number": number,
                "createdAt": created_at,
                "assetId": asset_id,
            }
        )
        if inspection_id is not UNSET:
            field_dict["inspectionId"] = inspection_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        number = d.pop("number")

        created_at = d.pop("createdAt")

        asset_id = d.pop("assetId")

        def _parse_inspection_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inspection_id = _parse_inspection_id(d.pop("inspectionId", UNSET))

        def _parse_event_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        event_id = _parse_event_id(d.pop("eventId", UNSET))

        insight_cerberus = cls(
            id=id,
            type_=type_,
            number=number,
            created_at=created_at,
            asset_id=asset_id,
            inspection_id=inspection_id,
            event_id=event_id,
        )

        insight_cerberus.additional_properties = d
        return insight_cerberus

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

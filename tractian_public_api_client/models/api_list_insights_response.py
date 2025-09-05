from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simplified_prescription import SimplifiedPrescription


T = TypeVar("T", bound="ApiListInsightsResponse")


@_attrs_define
class ApiListInsightsResponse:
    id: str
    type_: str
    number: int
    created_at: str
    asset_id: str
    inspection_id: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    event_id: Union[None, Unset, str] = UNSET
    prescriptions: Union[None, Unset, list["SimplifiedPrescription"]] = UNSET
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

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        event_id: Union[None, Unset, str]
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        prescriptions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.prescriptions, Unset):
            prescriptions = UNSET
        elif isinstance(self.prescriptions, list):
            prescriptions = []
            for prescriptions_type_0_item_data in self.prescriptions:
                prescriptions_type_0_item = prescriptions_type_0_item_data.to_dict()
                prescriptions.append(prescriptions_type_0_item)

        else:
            prescriptions = self.prescriptions

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
        if description is not UNSET:
            field_dict["description"] = description
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if prescriptions is not UNSET:
            field_dict["prescriptions"] = prescriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simplified_prescription import SimplifiedPrescription

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_event_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        event_id = _parse_event_id(d.pop("eventId", UNSET))

        def _parse_prescriptions(
            data: object,
        ) -> Union[None, Unset, list["SimplifiedPrescription"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prescriptions_type_0 = []
                _prescriptions_type_0 = data
                for prescriptions_type_0_item_data in _prescriptions_type_0:
                    prescriptions_type_0_item = SimplifiedPrescription.from_dict(
                        prescriptions_type_0_item_data
                    )

                    prescriptions_type_0.append(prescriptions_type_0_item)

                return prescriptions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SimplifiedPrescription"]], data)

        prescriptions = _parse_prescriptions(d.pop("prescriptions", UNSET))

        api_list_insights_response = cls(
            id=id,
            type_=type_,
            number=number,
            created_at=created_at,
            asset_id=asset_id,
            inspection_id=inspection_id,
            description=description,
            event_id=event_id,
            prescriptions=prescriptions,
        )

        api_list_insights_response.additional_properties = d
        return api_list_insights_response

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

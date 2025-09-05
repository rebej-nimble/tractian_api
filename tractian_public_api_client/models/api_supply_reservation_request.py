from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_item_reservation_request import (
        ApiSupplyItemReservationRequest,
    )


T = TypeVar("T", bound="ApiSupplyReservationRequest")


@_attrs_define
class ApiSupplyReservationRequest:
    company_id: str
    """ The company id of the reservation """
    cost_center_id: str
    """ The cost center id of the reservation """
    item_reservations: list["ApiSupplyItemReservationRequest"]
    """ The list of item reservations of the reservation """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time the reservation was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time the reservation was updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id of the creator """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id of the updater """
    work_order_id: Union[None, Unset, str] = UNSET
    """ The work order id linked to the reservation """
    external_id: Union[None, Unset, str] = UNSET
    """ External id, can be used to link the reservation to an external system """
    assigned_user_ids: Union[None, Unset, str] = UNSET
    """ The array of assigned user ids """
    assigned_team_ids: Union[None, Unset, str] = UNSET
    """ The array of assigned team ids """
    canceled: Union[None, Unset, bool] = UNSET
    """ The cancellation status of the reservation """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        cost_center_id = self.cost_center_id

        item_reservations = []
        for item_reservations_item_data in self.item_reservations:
            item_reservations_item = item_reservations_item_data.to_dict()
            item_reservations.append(item_reservations_item)

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

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        assigned_user_ids: Union[None, Unset, str]
        if isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = UNSET
        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, Unset, str]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        else:
            assigned_team_ids = self.assigned_team_ids

        canceled: Union[None, Unset, bool]
        if isinstance(self.canceled, Unset):
            canceled = UNSET
        else:
            canceled = self.canceled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "costCenterId": cost_center_id,
                "itemReservations": item_reservations,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if canceled is not UNSET:
            field_dict["canceled"] = canceled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_item_reservation_request import (
            ApiSupplyItemReservationRequest,
        )

        d = dict(src_dict)
        company_id = d.pop("companyId")

        cost_center_id = d.pop("costCenterId")

        item_reservations = []
        _item_reservations = d.pop("itemReservations")
        for item_reservations_item_data in _item_reservations:
            item_reservations_item = ApiSupplyItemReservationRequest.from_dict(
                item_reservations_item_data
            )

            item_reservations.append(item_reservations_item)

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

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_assigned_user_ids(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds", UNSET))

        def _parse_assigned_team_ids(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds", UNSET))

        def _parse_canceled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        canceled = _parse_canceled(d.pop("canceled", UNSET))

        api_supply_reservation_request = cls(
            company_id=company_id,
            cost_center_id=cost_center_id,
            item_reservations=item_reservations,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            work_order_id=work_order_id,
            external_id=external_id,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            canceled=canceled,
        )

        api_supply_reservation_request.additional_properties = d
        return api_supply_reservation_request

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

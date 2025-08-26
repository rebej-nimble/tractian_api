from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSupplyItemReservationRequest")


@_attrs_define
class ApiSupplyItemReservationRequest:
    item_id: str
    """ The item id of the reservation """
    item_storage_id: str
    """ The item storage id of the reservation """
    cost_center_id: str
    """ The cost center id of the reservation """
    quantity: float
    """ The quantity of the reservation """
    company_id: str
    """ The company id of the reservation """
    external_id: Union[None, Unset, str] = UNSET
    """ External id, can be used to link the reservation to an external system """
    work_order_operation_id: Union[None, Unset, str] = UNSET
    """ The work order operation id of the reservation """
    work_order_item_id: Union[None, Unset, str] = UNSET
    """ The work order item id of the reservation """
    created_at: Union[None, Unset, str] = UNSET
    """ The date and time the reservation was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date and time the reservation was updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id of the creator """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The user id of the updater """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        item_storage_id = self.item_storage_id

        cost_center_id = self.cost_center_id

        quantity = self.quantity

        company_id = self.company_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        work_order_operation_id: Union[None, Unset, str]
        if isinstance(self.work_order_operation_id, Unset):
            work_order_operation_id = UNSET
        else:
            work_order_operation_id = self.work_order_operation_id

        work_order_item_id: Union[None, Unset, str]
        if isinstance(self.work_order_item_id, Unset):
            work_order_item_id = UNSET
        else:
            work_order_item_id = self.work_order_item_id

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
        field_dict.update(
            {
                "itemId": item_id,
                "itemStorageId": item_storage_id,
                "costCenterId": cost_center_id,
                "quantity": quantity,
                "companyId": company_id,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if work_order_item_id is not UNSET:
            field_dict["workOrderItemId"] = work_order_item_id
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
        item_id = d.pop("itemId")

        item_storage_id = d.pop("itemStorageId")

        cost_center_id = d.pop("costCenterId")

        quantity = d.pop("quantity")

        company_id = d.pop("companyId")

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_work_order_operation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_operation_id = _parse_work_order_operation_id(
            d.pop("workOrderOperationId", UNSET)
        )

        def _parse_work_order_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_item_id = _parse_work_order_item_id(d.pop("workOrderItemId", UNSET))

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

        api_supply_item_reservation_request = cls(
            item_id=item_id,
            item_storage_id=item_storage_id,
            cost_center_id=cost_center_id,
            quantity=quantity,
            company_id=company_id,
            external_id=external_id,
            work_order_operation_id=work_order_operation_id,
            work_order_item_id=work_order_item_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
        )

        api_supply_item_reservation_request.additional_properties = d
        return api_supply_item_reservation_request

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

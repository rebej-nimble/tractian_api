from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.withdrawn_batch import WithdrawnBatch
    from ..models.withdrawn_position import WithdrawnPosition


T = TypeVar("T", bound="ApiSupplyItemReservationResponse")


@_attrs_define
class ApiSupplyItemReservationResponse:
    withdrawn_by_user_id: Union[None, Unset, str] = UNSET
    withdrawn_at: Union[None, Unset, str] = UNSET
    withdrawn_batches: Union[None, Unset, list["WithdrawnBatch"]] = UNSET
    withdrawn_positions: Union[None, Unset, list["WithdrawnPosition"]] = UNSET
    returned_by_user_id: Union[None, Unset, str] = UNSET
    return_due_date: Union[None, Unset, str] = UNSET
    returned_at: Union[None, Unset, str] = UNSET
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    canceled_at: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    number: Union[None, Unset, int] = UNSET
    created_at: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    created_by_user_id: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    company_id: Union[None, Unset, str] = UNSET
    reservation_id: Union[None, Unset, str] = UNSET
    work_order_operation_id: Union[None, Unset, str] = UNSET
    work_order_item_id: Union[None, Unset, str] = UNSET
    item_id: Union[None, Unset, str] = UNSET
    item_storage_id: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    status: Union[None, Unset, str] = UNSET
    reservation_number: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        withdrawn_by_user_id: Union[None, Unset, str]
        if isinstance(self.withdrawn_by_user_id, Unset):
            withdrawn_by_user_id = UNSET
        else:
            withdrawn_by_user_id = self.withdrawn_by_user_id

        withdrawn_at: Union[None, Unset, str]
        if isinstance(self.withdrawn_at, Unset):
            withdrawn_at = UNSET
        else:
            withdrawn_at = self.withdrawn_at

        withdrawn_batches: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.withdrawn_batches, Unset):
            withdrawn_batches = UNSET
        elif isinstance(self.withdrawn_batches, list):
            withdrawn_batches = []
            for withdrawn_batches_type_0_item_data in self.withdrawn_batches:
                withdrawn_batches_type_0_item = (
                    withdrawn_batches_type_0_item_data.to_dict()
                )
                withdrawn_batches.append(withdrawn_batches_type_0_item)

        else:
            withdrawn_batches = self.withdrawn_batches

        withdrawn_positions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.withdrawn_positions, Unset):
            withdrawn_positions = UNSET
        elif isinstance(self.withdrawn_positions, list):
            withdrawn_positions = []
            for withdrawn_positions_type_0_item_data in self.withdrawn_positions:
                withdrawn_positions_type_0_item = (
                    withdrawn_positions_type_0_item_data.to_dict()
                )
                withdrawn_positions.append(withdrawn_positions_type_0_item)

        else:
            withdrawn_positions = self.withdrawn_positions

        returned_by_user_id: Union[None, Unset, str]
        if isinstance(self.returned_by_user_id, Unset):
            returned_by_user_id = UNSET
        else:
            returned_by_user_id = self.returned_by_user_id

        return_due_date: Union[None, Unset, str]
        if isinstance(self.return_due_date, Unset):
            return_due_date = UNSET
        else:
            return_due_date = self.return_due_date

        returned_at: Union[None, Unset, str]
        if isinstance(self.returned_at, Unset):
            returned_at = UNSET
        else:
            returned_at = self.returned_at

        canceled_by_user_id: Union[None, Unset, str]
        if isinstance(self.canceled_by_user_id, Unset):
            canceled_by_user_id = UNSET
        else:
            canceled_by_user_id = self.canceled_by_user_id

        canceled_at: Union[None, Unset, str]
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = self.canceled_at

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

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

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        reservation_id: Union[None, Unset, str]
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

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

        item_id: Union[None, Unset, str]
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        else:
            item_id = self.item_id

        item_storage_id: Union[None, Unset, str]
        if isinstance(self.item_storage_id, Unset):
            item_storage_id = UNSET
        else:
            item_storage_id = self.item_storage_id

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        reservation_number: Union[None, Unset, int]
        if isinstance(self.reservation_number, Unset):
            reservation_number = UNSET
        else:
            reservation_number = self.reservation_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if withdrawn_by_user_id is not UNSET:
            field_dict["withdrawnByUserId"] = withdrawn_by_user_id
        if withdrawn_at is not UNSET:
            field_dict["withdrawnAt"] = withdrawn_at
        if withdrawn_batches is not UNSET:
            field_dict["withdrawnBatches"] = withdrawn_batches
        if withdrawn_positions is not UNSET:
            field_dict["withdrawnPositions"] = withdrawn_positions
        if returned_by_user_id is not UNSET:
            field_dict["returnedByUserId"] = returned_by_user_id
        if return_due_date is not UNSET:
            field_dict["returnDueDate"] = return_due_date
        if returned_at is not UNSET:
            field_dict["returnedAt"] = returned_at
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if id is not UNSET:
            field_dict["id"] = id
        if number is not UNSET:
            field_dict["number"] = number
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if work_order_operation_id is not UNSET:
            field_dict["workOrderOperationId"] = work_order_operation_id
        if work_order_item_id is not UNSET:
            field_dict["workOrderItemId"] = work_order_item_id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if item_storage_id is not UNSET:
            field_dict["itemStorageId"] = item_storage_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if status is not UNSET:
            field_dict["status"] = status
        if reservation_number is not UNSET:
            field_dict["reservationNumber"] = reservation_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.withdrawn_batch import WithdrawnBatch
        from ..models.withdrawn_position import WithdrawnPosition

        d = dict(src_dict)

        def _parse_withdrawn_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        withdrawn_by_user_id = _parse_withdrawn_by_user_id(
            d.pop("withdrawnByUserId", UNSET)
        )

        def _parse_withdrawn_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        withdrawn_at = _parse_withdrawn_at(d.pop("withdrawnAt", UNSET))

        def _parse_withdrawn_batches(
            data: object,
        ) -> Union[None, Unset, list["WithdrawnBatch"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                withdrawn_batches_type_0 = []
                _withdrawn_batches_type_0 = data
                for withdrawn_batches_type_0_item_data in _withdrawn_batches_type_0:
                    withdrawn_batches_type_0_item = WithdrawnBatch.from_dict(
                        withdrawn_batches_type_0_item_data
                    )

                    withdrawn_batches_type_0.append(withdrawn_batches_type_0_item)

                return withdrawn_batches_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WithdrawnBatch"]], data)

        withdrawn_batches = _parse_withdrawn_batches(d.pop("withdrawnBatches", UNSET))

        def _parse_withdrawn_positions(
            data: object,
        ) -> Union[None, Unset, list["WithdrawnPosition"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                withdrawn_positions_type_0 = []
                _withdrawn_positions_type_0 = data
                for withdrawn_positions_type_0_item_data in _withdrawn_positions_type_0:
                    withdrawn_positions_type_0_item = WithdrawnPosition.from_dict(
                        withdrawn_positions_type_0_item_data
                    )

                    withdrawn_positions_type_0.append(withdrawn_positions_type_0_item)

                return withdrawn_positions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["WithdrawnPosition"]], data)

        withdrawn_positions = _parse_withdrawn_positions(
            d.pop("withdrawnPositions", UNSET)
        )

        def _parse_returned_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        returned_by_user_id = _parse_returned_by_user_id(
            d.pop("returnedByUserId", UNSET)
        )

        def _parse_return_due_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        return_due_date = _parse_return_due_date(d.pop("returnDueDate", UNSET))

        def _parse_returned_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        returned_at = _parse_returned_at(d.pop("returnedAt", UNSET))

        def _parse_canceled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_by_user_id = _parse_canceled_by_user_id(
            d.pop("canceledByUserId", UNSET)
        )

        def _parse_canceled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))

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

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_reservation_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))

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

        def _parse_item_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_id = _parse_item_id(d.pop("itemId", UNSET))

        def _parse_item_storage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_storage_id = _parse_item_storage_id(d.pop("itemStorageId", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_reservation_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reservation_number = _parse_reservation_number(
            d.pop("reservationNumber", UNSET)
        )

        api_supply_item_reservation_response = cls(
            withdrawn_by_user_id=withdrawn_by_user_id,
            withdrawn_at=withdrawn_at,
            withdrawn_batches=withdrawn_batches,
            withdrawn_positions=withdrawn_positions,
            returned_by_user_id=returned_by_user_id,
            return_due_date=return_due_date,
            returned_at=returned_at,
            canceled_by_user_id=canceled_by_user_id,
            canceled_at=canceled_at,
            id=id,
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            company_id=company_id,
            reservation_id=reservation_id,
            work_order_operation_id=work_order_operation_id,
            work_order_item_id=work_order_item_id,
            item_id=item_id,
            item_storage_id=item_storage_id,
            quantity=quantity,
            status=status,
            reservation_number=reservation_number,
        )

        api_supply_item_reservation_response.additional_properties = d
        return api_supply_item_reservation_response

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

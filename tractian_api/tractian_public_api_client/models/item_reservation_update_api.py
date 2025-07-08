from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_reservation_request_selected_batches_api import (
        ItemReservationRequestSelectedBatchesAPI,
    )


T = TypeVar("T", bound="ItemReservationUpdateAPI")


@_attrs_define
class ItemReservationUpdateAPI:
    quantity: float
    """ Total quantity of the item to be reserved. """
    selected_batches: Union[None, list["ItemReservationRequestSelectedBatchesAPI"]]
    """ List of selected batches from which the item will be reserved. """
    identifier_code: Union[None, Unset, str] = UNSET
    """ Unique identifier code of the item, if applicable. This field should be used to store the customer's unique
    code for the reservation. """

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        selected_batches: Union[None, list[dict[str, Any]]]
        if isinstance(self.selected_batches, list):
            selected_batches = []
            for selected_batches_type_0_item_data in self.selected_batches:
                selected_batches_type_0_item = (
                    selected_batches_type_0_item_data.to_dict()
                )
                selected_batches.append(selected_batches_type_0_item)

        else:
            selected_batches = self.selected_batches

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
                "selectedBatches": selected_batches,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_reservation_request_selected_batches_api import (
            ItemReservationRequestSelectedBatchesAPI,
        )

        d = dict(src_dict)
        quantity = d.pop("quantity")

        def _parse_selected_batches(
            data: object,
        ) -> Union[None, list["ItemReservationRequestSelectedBatchesAPI"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_batches_type_0 = []
                _selected_batches_type_0 = data
                for selected_batches_type_0_item_data in _selected_batches_type_0:
                    selected_batches_type_0_item = (
                        ItemReservationRequestSelectedBatchesAPI.from_dict(
                            selected_batches_type_0_item_data
                        )
                    )

                    selected_batches_type_0.append(selected_batches_type_0_item)

                return selected_batches_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, list["ItemReservationRequestSelectedBatchesAPI"]], data
            )

        selected_batches = _parse_selected_batches(d.pop("selectedBatches"))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        item_reservation_update_api = cls(
            quantity=quantity,
            selected_batches=selected_batches,
            identifier_code=identifier_code,
        )

        return item_reservation_update_api

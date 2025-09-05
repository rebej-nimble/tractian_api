from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supply_item_storage_inbound_batch_request import (
        SupplyItemStorageInboundBatchRequest,
    )
    from ..models.supply_item_storage_position_request import (
        SupplyItemStoragePositionRequest,
    )


T = TypeVar("T", bound="SupplyItemStorageRequest")


@_attrs_define
class SupplyItemStorageRequest:
    company_id: str
    storage_id: str
    max_storage: Union[None, float]
    min_storage: Union[None, float]
    supply_point: Union[None, float]
    storage_positions: list["SupplyItemStoragePositionRequest"]
    new_inbound_batch: Union["SupplyItemStorageInboundBatchRequest", None, Unset] = (
        UNSET
    )
    """ Required when item storage position quantity is not 0 """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.supply_item_storage_inbound_batch_request import (
            SupplyItemStorageInboundBatchRequest,
        )

        company_id = self.company_id

        storage_id = self.storage_id

        max_storage: Union[None, float]
        max_storage = self.max_storage

        min_storage: Union[None, float]
        min_storage = self.min_storage

        supply_point: Union[None, float]
        supply_point = self.supply_point

        storage_positions = []
        for storage_positions_item_data in self.storage_positions:
            storage_positions_item = storage_positions_item_data.to_dict()
            storage_positions.append(storage_positions_item)

        new_inbound_batch: Union[None, Unset, dict[str, Any]]
        if isinstance(self.new_inbound_batch, Unset):
            new_inbound_batch = UNSET
        elif isinstance(self.new_inbound_batch, SupplyItemStorageInboundBatchRequest):
            new_inbound_batch = self.new_inbound_batch.to_dict()
        else:
            new_inbound_batch = self.new_inbound_batch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "storageId": storage_id,
                "maxStorage": max_storage,
                "minStorage": min_storage,
                "supplyPoint": supply_point,
                "storagePositions": storage_positions,
            }
        )
        if new_inbound_batch is not UNSET:
            field_dict["newInboundBatch"] = new_inbound_batch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supply_item_storage_inbound_batch_request import (
            SupplyItemStorageInboundBatchRequest,
        )
        from ..models.supply_item_storage_position_request import (
            SupplyItemStoragePositionRequest,
        )

        d = dict(src_dict)
        company_id = d.pop("companyId")

        storage_id = d.pop("storageId")

        def _parse_max_storage(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        max_storage = _parse_max_storage(d.pop("maxStorage"))

        def _parse_min_storage(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        min_storage = _parse_min_storage(d.pop("minStorage"))

        def _parse_supply_point(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        supply_point = _parse_supply_point(d.pop("supplyPoint"))

        storage_positions = []
        _storage_positions = d.pop("storagePositions")
        for storage_positions_item_data in _storage_positions:
            storage_positions_item = SupplyItemStoragePositionRequest.from_dict(
                storage_positions_item_data
            )

            storage_positions.append(storage_positions_item)

        def _parse_new_inbound_batch(
            data: object,
        ) -> Union["SupplyItemStorageInboundBatchRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_inbound_batch_type_0 = (
                    SupplyItemStorageInboundBatchRequest.from_dict(data)
                )

                return new_inbound_batch_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["SupplyItemStorageInboundBatchRequest", None, Unset], data
            )

        new_inbound_batch = _parse_new_inbound_batch(d.pop("newInboundBatch", UNSET))

        supply_item_storage_request = cls(
            company_id=company_id,
            storage_id=storage_id,
            max_storage=max_storage,
            min_storage=min_storage,
            supply_point=supply_point,
            storage_positions=storage_positions,
            new_inbound_batch=new_inbound_batch,
        )

        supply_item_storage_request.additional_properties = d
        return supply_item_storage_request

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

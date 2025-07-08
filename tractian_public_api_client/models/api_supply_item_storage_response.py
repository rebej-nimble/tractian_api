from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stock_level import StockLevel, check_stock_level
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.balance import Balance
    from ..models.deleted_info import DeletedInfo
    from ..models.inbound_batch import InboundBatch
    from ..models.storage_position import StoragePosition


T = TypeVar("T", bound="ApiSupplyItemStorageResponse")


@_attrs_define
class ApiSupplyItemStorageResponse:
    id: str
    item_id: str
    storage_id: str
    storage_name: str
    created_at: str
    created_by_user_id: str
    balance: "Balance"
    company_id: str
    inbound_batches: Union[Unset, list["InboundBatch"]] = UNSET
    max_storage: Union[None, Unset, float] = UNSET
    min_storage: Union[None, Unset, float] = UNSET
    supply_point: Union[None, Unset, float] = UNSET
    average_price: Union[None, Unset, float] = UNSET
    updated_at: Union[None, Unset, str] = UNSET
    updated_by_user_id: Union[None, Unset, str] = UNSET
    deleted: Union["DeletedInfo", None, Unset] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    stock_level: Union[None, StockLevel, Unset] = UNSET
    total_price: Union[None, Unset, float] = UNSET
    new_inbound_batch: Union[None, Unset, str] = UNSET
    storage_positions: Union[None, Unset, list["StoragePosition"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deleted_info import DeletedInfo

        id = self.id

        item_id = self.item_id

        storage_id = self.storage_id

        storage_name = self.storage_name

        created_at = self.created_at

        created_by_user_id = self.created_by_user_id

        balance = self.balance.to_dict()

        company_id = self.company_id

        inbound_batches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inbound_batches, Unset):
            inbound_batches = []
            for inbound_batches_item_data in self.inbound_batches:
                inbound_batches_item = inbound_batches_item_data.to_dict()
                inbound_batches.append(inbound_batches_item)

        max_storage: Union[None, Unset, float]
        if isinstance(self.max_storage, Unset):
            max_storage = UNSET
        else:
            max_storage = self.max_storage

        min_storage: Union[None, Unset, float]
        if isinstance(self.min_storage, Unset):
            min_storage = UNSET
        else:
            min_storage = self.min_storage

        supply_point: Union[None, Unset, float]
        if isinstance(self.supply_point, Unset):
            supply_point = UNSET
        else:
            supply_point = self.supply_point

        average_price: Union[None, Unset, float]
        if isinstance(self.average_price, Unset):
            average_price = UNSET
        else:
            average_price = self.average_price

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        deleted: Union[None, Unset, dict[str, Any]]
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        elif isinstance(self.deleted, DeletedInfo):
            deleted = self.deleted.to_dict()
        else:
            deleted = self.deleted

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        stock_level: Union[None, Unset, str]
        if isinstance(self.stock_level, Unset):
            stock_level = UNSET
        elif isinstance(self.stock_level, str):
            stock_level = self.stock_level
        else:
            stock_level = self.stock_level

        total_price: Union[None, Unset, float]
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        new_inbound_batch: Union[None, Unset, str]
        if isinstance(self.new_inbound_batch, Unset):
            new_inbound_batch = UNSET
        else:
            new_inbound_batch = self.new_inbound_batch

        storage_positions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.storage_positions, Unset):
            storage_positions = UNSET
        elif isinstance(self.storage_positions, list):
            storage_positions = []
            for storage_positions_type_0_item_data in self.storage_positions:
                storage_positions_type_0_item = (
                    storage_positions_type_0_item_data.to_dict()
                )
                storage_positions.append(storage_positions_type_0_item)

        else:
            storage_positions = self.storage_positions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "itemId": item_id,
                "storageId": storage_id,
                "storageName": storage_name,
                "createdAt": created_at,
                "createdByUserId": created_by_user_id,
                "balance": balance,
                "companyId": company_id,
            }
        )
        if inbound_batches is not UNSET:
            field_dict["inboundBatches"] = inbound_batches
        if max_storage is not UNSET:
            field_dict["maxStorage"] = max_storage
        if min_storage is not UNSET:
            field_dict["minStorage"] = min_storage
        if supply_point is not UNSET:
            field_dict["supplyPoint"] = supply_point
        if average_price is not UNSET:
            field_dict["averagePrice"] = average_price
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if stock_level is not UNSET:
            field_dict["stockLevel"] = stock_level
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if new_inbound_batch is not UNSET:
            field_dict["newInboundBatch"] = new_inbound_batch
        if storage_positions is not UNSET:
            field_dict["storagePositions"] = storage_positions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.balance import Balance
        from ..models.deleted_info import DeletedInfo
        from ..models.inbound_batch import InboundBatch
        from ..models.storage_position import StoragePosition

        d = dict(src_dict)
        id = d.pop("id")

        item_id = d.pop("itemId")

        storage_id = d.pop("storageId")

        storage_name = d.pop("storageName")

        created_at = d.pop("createdAt")

        created_by_user_id = d.pop("createdByUserId")

        balance = Balance.from_dict(d.pop("balance"))

        company_id = d.pop("companyId")

        inbound_batches = []
        _inbound_batches = d.pop("inboundBatches", UNSET)
        for inbound_batches_item_data in _inbound_batches or []:
            inbound_batches_item = InboundBatch.from_dict(inbound_batches_item_data)

            inbound_batches.append(inbound_batches_item)

        def _parse_max_storage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_storage = _parse_max_storage(d.pop("maxStorage", UNSET))

        def _parse_min_storage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_storage = _parse_min_storage(d.pop("minStorage", UNSET))

        def _parse_supply_point(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        supply_point = _parse_supply_point(d.pop("supplyPoint", UNSET))

        def _parse_average_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        average_price = _parse_average_price(d.pop("averagePrice", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        def _parse_deleted(data: object) -> Union["DeletedInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_type_0 = DeletedInfo.from_dict(data)

                return deleted_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DeletedInfo", None, Unset], data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_stock_level(data: object) -> Union[None, StockLevel, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stock_level_type_0 = check_stock_level(data)

                return stock_level_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, StockLevel, Unset], data)

        stock_level = _parse_stock_level(d.pop("stockLevel", UNSET))

        def _parse_total_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))

        def _parse_new_inbound_batch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        new_inbound_batch = _parse_new_inbound_batch(d.pop("newInboundBatch", UNSET))

        def _parse_storage_positions(
            data: object,
        ) -> Union[None, Unset, list["StoragePosition"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                storage_positions_type_0 = []
                _storage_positions_type_0 = data
                for storage_positions_type_0_item_data in _storage_positions_type_0:
                    storage_positions_type_0_item = StoragePosition.from_dict(
                        storage_positions_type_0_item_data
                    )

                    storage_positions_type_0.append(storage_positions_type_0_item)

                return storage_positions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["StoragePosition"]], data)

        storage_positions = _parse_storage_positions(d.pop("storagePositions", UNSET))

        api_supply_item_storage_response = cls(
            id=id,
            item_id=item_id,
            storage_id=storage_id,
            storage_name=storage_name,
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            balance=balance,
            company_id=company_id,
            inbound_batches=inbound_batches,
            max_storage=max_storage,
            min_storage=min_storage,
            supply_point=supply_point,
            average_price=average_price,
            updated_at=updated_at,
            updated_by_user_id=updated_by_user_id,
            deleted=deleted,
            identifier_code=identifier_code,
            stock_level=stock_level,
            total_price=total_price,
            new_inbound_batch=new_inbound_batch,
            storage_positions=storage_positions,
        )

        api_supply_item_storage_response.additional_properties = d
        return api_supply_item_storage_response

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

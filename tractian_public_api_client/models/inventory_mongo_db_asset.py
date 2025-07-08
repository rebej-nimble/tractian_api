from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_mongo_db_asset_asset_type_0 import (
        InventoryMongoDBAssetAssetType0,
    )


T = TypeVar("T", bound="InventoryMongoDBAsset")


@_attrs_define
class InventoryMongoDBAsset:
    asset_id: str
    amount: int
    selected_batches: Union[None, Unset, str] = UNSET
    asset: Union["InventoryMongoDBAssetAssetType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_mongo_db_asset_asset_type_0 import (
            InventoryMongoDBAssetAssetType0,
        )

        asset_id = self.asset_id

        amount = self.amount

        selected_batches: Union[None, Unset, str]
        if isinstance(self.selected_batches, Unset):
            selected_batches = UNSET
        else:
            selected_batches = self.selected_batches

        asset: Union[None, Unset, dict[str, Any]]
        if isinstance(self.asset, Unset):
            asset = UNSET
        elif isinstance(self.asset, InventoryMongoDBAssetAssetType0):
            asset = self.asset.to_dict()
        else:
            asset = self.asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "amount": amount,
            }
        )
        if selected_batches is not UNSET:
            field_dict["selectedBatches"] = selected_batches
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_mongo_db_asset_asset_type_0 import (
            InventoryMongoDBAssetAssetType0,
        )

        d = dict(src_dict)
        asset_id = d.pop("assetId")

        amount = d.pop("amount")

        def _parse_selected_batches(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        selected_batches = _parse_selected_batches(d.pop("selectedBatches", UNSET))

        def _parse_asset(
            data: object,
        ) -> Union["InventoryMongoDBAssetAssetType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_type_0 = InventoryMongoDBAssetAssetType0.from_dict(data)

                return asset_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InventoryMongoDBAssetAssetType0", None, Unset], data)

        asset = _parse_asset(d.pop("asset", UNSET))

        inventory_mongo_db_asset = cls(
            asset_id=asset_id,
            amount=amount,
            selected_batches=selected_batches,
            asset=asset,
        )

        inventory_mongo_db_asset.additional_properties = d
        return inventory_mongo_db_asset

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

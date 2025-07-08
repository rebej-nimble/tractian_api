from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_mongo_db_asset import InventoryMongoDBAsset


T = TypeVar("T", bound="InventoryMongoDB")


@_attrs_define
class InventoryMongoDB:
    field_id: str
    code: str
    company_id: str
    name: str
    image: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    unit_cost: Union[None, Unset, float] = 0.0
    maximum_quantity: Union[None, Unset, int] = UNSET
    minimum_quantity: Union[None, Unset, int] = UNSET
    available_quantity: Union[None, Unset, float, int] = UNSET
    needs_restock: Union[None, Unset, bool] = False
    assets: Union[None, Unset, list["InventoryMongoDBAsset"]] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        code = self.code

        company_id = self.company_id

        name = self.name

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        unit_cost: Union[None, Unset, float]
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        maximum_quantity: Union[None, Unset, int]
        if isinstance(self.maximum_quantity, Unset):
            maximum_quantity = UNSET
        else:
            maximum_quantity = self.maximum_quantity

        minimum_quantity: Union[None, Unset, int]
        if isinstance(self.minimum_quantity, Unset):
            minimum_quantity = UNSET
        else:
            minimum_quantity = self.minimum_quantity

        available_quantity: Union[None, Unset, float, int]
        if isinstance(self.available_quantity, Unset):
            available_quantity = UNSET
        else:
            available_quantity = self.available_quantity

        needs_restock: Union[None, Unset, bool]
        if isinstance(self.needs_restock, Unset):
            needs_restock = UNSET
        else:
            needs_restock = self.needs_restock

        assets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.assets, Unset):
            assets = UNSET
        elif isinstance(self.assets, list):
            assets = []
            for assets_type_0_item_data in self.assets:
                assets_type_0_item = assets_type_0_item_data.to_dict()
                assets.append(assets_type_0_item)

        else:
            assets = self.assets

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "code": code,
                "companyId": company_id,
                "name": name,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if maximum_quantity is not UNSET:
            field_dict["maximumQuantity"] = maximum_quantity
        if minimum_quantity is not UNSET:
            field_dict["minimumQuantity"] = minimum_quantity
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if needs_restock is not UNSET:
            field_dict["needsRestock"] = needs_restock
        if assets is not UNSET:
            field_dict["assets"] = assets
        if location_id is not UNSET:
            field_dict["locationId"] = location_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_mongo_db_asset import InventoryMongoDBAsset

        d = dict(src_dict)
        field_id = d.pop("_id")

        code = d.pop("code")

        company_id = d.pop("companyId")

        name = d.pop("name")

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_unit_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        def _parse_maximum_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        maximum_quantity = _parse_maximum_quantity(d.pop("maximumQuantity", UNSET))

        def _parse_minimum_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        minimum_quantity = _parse_minimum_quantity(d.pop("minimumQuantity", UNSET))

        def _parse_available_quantity(data: object) -> Union[None, Unset, float, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, int], data)

        available_quantity = _parse_available_quantity(
            d.pop("availableQuantity", UNSET)
        )

        def _parse_needs_restock(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        needs_restock = _parse_needs_restock(d.pop("needsRestock", UNSET))

        def _parse_assets(
            data: object,
        ) -> Union[None, Unset, list["InventoryMongoDBAsset"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assets_type_0 = []
                _assets_type_0 = data
                for assets_type_0_item_data in _assets_type_0:
                    assets_type_0_item = InventoryMongoDBAsset.from_dict(
                        assets_type_0_item_data
                    )

                    assets_type_0.append(assets_type_0_item)

                return assets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["InventoryMongoDBAsset"]], data)

        assets = _parse_assets(d.pop("assets", UNSET))

        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))

        inventory_mongo_db = cls(
            field_id=field_id,
            code=code,
            company_id=company_id,
            name=name,
            image=image,
            identifier_code=identifier_code,
            unit_cost=unit_cost,
            maximum_quantity=maximum_quantity,
            minimum_quantity=minimum_quantity,
            available_quantity=available_quantity,
            needs_restock=needs_restock,
            assets=assets,
            location_id=location_id,
        )

        inventory_mongo_db.additional_properties = d
        return inventory_mongo_db

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

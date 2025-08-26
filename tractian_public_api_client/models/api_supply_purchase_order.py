from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_supply_purchase_order_status import (
    ApiSupplyPurchaseOrderStatus,
    check_api_supply_purchase_order_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_purchase_order_item import ApiSupplyPurchaseOrderItem


T = TypeVar("T", bound="ApiSupplyPurchaseOrder")


@_attrs_define
class ApiSupplyPurchaseOrder:
    id: str
    number: int
    created_at: str
    updated_at: str
    created_by_user_id: str
    updated_by_user_id: str
    status: ApiSupplyPurchaseOrderStatus
    supplier_id: str
    company_id: str
    purchase_order_items: Union[None, Unset, list["ApiSupplyPurchaseOrderItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        created_at = self.created_at

        updated_at = self.updated_at

        created_by_user_id = self.created_by_user_id

        updated_by_user_id = self.updated_by_user_id

        status: str = self.status

        supplier_id = self.supplier_id

        company_id = self.company_id

        purchase_order_items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.purchase_order_items, Unset):
            purchase_order_items = UNSET
        elif isinstance(self.purchase_order_items, list):
            purchase_order_items = []
            for purchase_order_items_type_0_item_data in self.purchase_order_items:
                purchase_order_items_type_0_item = (
                    purchase_order_items_type_0_item_data.to_dict()
                )
                purchase_order_items.append(purchase_order_items_type_0_item)

        else:
            purchase_order_items = self.purchase_order_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
                "status": status,
                "supplierId": supplier_id,
                "companyId": company_id,
            }
        )
        if purchase_order_items is not UNSET:
            field_dict["purchaseOrderItems"] = purchase_order_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_purchase_order_item import ApiSupplyPurchaseOrderItem

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        created_by_user_id = d.pop("createdByUserId")

        updated_by_user_id = d.pop("updatedByUserId")

        status = check_api_supply_purchase_order_status(d.pop("status"))

        supplier_id = d.pop("supplierId")

        company_id = d.pop("companyId")

        def _parse_purchase_order_items(
            data: object,
        ) -> Union[None, Unset, list["ApiSupplyPurchaseOrderItem"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purchase_order_items_type_0 = []
                _purchase_order_items_type_0 = data
                for (
                    purchase_order_items_type_0_item_data
                ) in _purchase_order_items_type_0:
                    purchase_order_items_type_0_item = (
                        ApiSupplyPurchaseOrderItem.from_dict(
                            purchase_order_items_type_0_item_data
                        )
                    )

                    purchase_order_items_type_0.append(purchase_order_items_type_0_item)

                return purchase_order_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApiSupplyPurchaseOrderItem"]], data)

        purchase_order_items = _parse_purchase_order_items(
            d.pop("purchaseOrderItems", UNSET)
        )

        api_supply_purchase_order = cls(
            id=id,
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            status=status,
            supplier_id=supplier_id,
            company_id=company_id,
            purchase_order_items=purchase_order_items,
        )

        api_supply_purchase_order.additional_properties = d
        return api_supply_purchase_order

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

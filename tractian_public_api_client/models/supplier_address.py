from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_supplier_address_coordinates import (
        ApiSupplySupplierAddressCoordinates,
    )


T = TypeVar("T", bound="SupplierAddress")


@_attrs_define
class SupplierAddress:
    company_id: str
    """ Unique identifier of the company the supplier address belongs to """
    address: str
    """ Address of the supplier address """
    supplier_id: str
    """ Unique identifier of the supplier the supplier address belongs to """
    coordinates: "ApiSupplySupplierAddressCoordinates"
    city: str
    """ City of the supplier address """
    state: str
    """ State of the supplier address """
    country: str
    """ Country of the supplier address """
    identifier_code: Union[None, Unset, str] = UNSET
    """ Identifier code """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        address = self.address

        supplier_id = self.supplier_id

        coordinates = self.coordinates.to_dict()

        city = self.city

        state = self.state

        country = self.country

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
                "address": address,
                "supplierId": supplier_id,
                "coordinates": coordinates,
                "city": city,
                "state": state,
                "country": country,
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_supplier_address_coordinates import (
            ApiSupplySupplierAddressCoordinates,
        )

        d = dict(src_dict)
        company_id = d.pop("companyId")

        address = d.pop("address")

        supplier_id = d.pop("supplierId")

        coordinates = ApiSupplySupplierAddressCoordinates.from_dict(
            d.pop("coordinates")
        )

        city = d.pop("city")

        state = d.pop("state")

        country = d.pop("country")

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        supplier_address = cls(
            company_id=company_id,
            address=address,
            supplier_id=supplier_id,
            coordinates=coordinates,
            city=city,
            state=state,
            country=country,
            identifier_code=identifier_code,
        )

        supplier_address.additional_properties = d
        return supplier_address

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

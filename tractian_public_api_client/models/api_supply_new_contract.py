from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supply_file_request import SupplyFileRequest


T = TypeVar("T", bound="ApiSupplyNewContract")


@_attrs_define
class ApiSupplyNewContract:
    id: str
    company_id: str
    supplier_id: str
    title: str
    position: float
    attachment: Union[None, Unset, list["SupplyFileRequest"]] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = self.company_id

        supplier_id = self.supplier_id

        title = self.title

        position = self.position

        attachment: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.attachment, Unset):
            attachment = UNSET
        elif isinstance(self.attachment, list):
            attachment = []
            for attachment_type_0_item_data in self.attachment:
                attachment_type_0_item = attachment_type_0_item_data.to_dict()
                attachment.append(attachment_type_0_item)

        else:
            attachment = self.attachment

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "companyId": company_id,
                "supplierId": supplier_id,
                "title": title,
                "position": position,
            }
        )
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supply_file_request import SupplyFileRequest

        d = dict(src_dict)
        id = d.pop("id")

        company_id = d.pop("companyId")

        supplier_id = d.pop("supplierId")

        title = d.pop("title")

        position = d.pop("position")

        def _parse_attachment(
            data: object,
        ) -> Union[None, Unset, list["SupplyFileRequest"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachment_type_0 = []
                _attachment_type_0 = data
                for attachment_type_0_item_data in _attachment_type_0:
                    attachment_type_0_item = SupplyFileRequest.from_dict(
                        attachment_type_0_item_data
                    )

                    attachment_type_0.append(attachment_type_0_item)

                return attachment_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SupplyFileRequest"]], data)

        attachment = _parse_attachment(d.pop("attachment", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        api_supply_new_contract = cls(
            id=id,
            company_id=company_id,
            supplier_id=supplier_id,
            title=title,
            position=position,
            attachment=attachment,
            external_id=external_id,
        )

        api_supply_new_contract.additional_properties = d
        return api_supply_new_contract

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

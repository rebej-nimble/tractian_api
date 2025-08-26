from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_attachment import ApiSupplyAttachment
    from ..models.transfer_request_item import TransferRequestItem


T = TypeVar("T", bound="ApiSupplyTransferRequestsRequest")


@_attrs_define
class ApiSupplyTransferRequestsRequest:
    company_id: str
    """ Company id of the supply transaction """
    notes: Union[None, Unset, str] = UNSET
    """ Notes about the supply transaction """
    attachments: Union[None, Unset, list["ApiSupplyAttachment"]] = UNSET
    """ Attachments about the supply transaction """
    transfer_request_items: Union[None, Unset, list["TransferRequestItem"]] = UNSET
    """ Items in transfer request """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        attachments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

        transfer_request_items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.transfer_request_items, Unset):
            transfer_request_items = UNSET
        elif isinstance(self.transfer_request_items, list):
            transfer_request_items = []
            for transfer_request_items_type_0_item_data in self.transfer_request_items:
                transfer_request_items_type_0_item = (
                    transfer_request_items_type_0_item_data.to_dict()
                )
                transfer_request_items.append(transfer_request_items_type_0_item)

        else:
            transfer_request_items = self.transfer_request_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if transfer_request_items is not UNSET:
            field_dict["transferRequestItems"] = transfer_request_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_attachment import ApiSupplyAttachment
        from ..models.transfer_request_item import TransferRequestItem

        d = dict(src_dict)
        company_id = d.pop("companyId")

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["ApiSupplyAttachment"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = ApiSupplyAttachment.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ApiSupplyAttachment"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_transfer_request_items(
            data: object,
        ) -> Union[None, Unset, list["TransferRequestItem"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transfer_request_items_type_0 = []
                _transfer_request_items_type_0 = data
                for (
                    transfer_request_items_type_0_item_data
                ) in _transfer_request_items_type_0:
                    transfer_request_items_type_0_item = TransferRequestItem.from_dict(
                        transfer_request_items_type_0_item_data
                    )

                    transfer_request_items_type_0.append(
                        transfer_request_items_type_0_item
                    )

                return transfer_request_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TransferRequestItem"]], data)

        transfer_request_items = _parse_transfer_request_items(
            d.pop("transferRequestItems", UNSET)
        )

        api_supply_transfer_requests_request = cls(
            company_id=company_id,
            notes=notes,
            attachments=attachments,
            transfer_request_items=transfer_request_items,
        )

        api_supply_transfer_requests_request.additional_properties = d
        return api_supply_transfer_requests_request

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

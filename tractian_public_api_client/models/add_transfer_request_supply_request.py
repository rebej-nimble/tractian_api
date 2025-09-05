from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attachment_inventory_item_supply import AttachmentInventoryItemSupply


T = TypeVar("T", bound="AddTransferRequestSupplyRequest")


@_attrs_define
class AddTransferRequestSupplyRequest:
    created_at: Union[None, str]
    updated_at: Union[None, str]
    created_by_user_id: Union[None, str]
    updated_by_user_id: Union[None, str]
    company_id: str
    external_id: Union[None, str]
    work_order_id: Union[None, str]
    notes: Union[None, str]
    attachments: Union[None, list["AttachmentInventoryItemSupply"]]
    attachment_ids: Union[None, list[str]]
    asset_ids: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[None, str]
        created_at = self.created_at

        updated_at: Union[None, str]
        updated_at = self.updated_at

        created_by_user_id: Union[None, str]
        created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, str]
        updated_by_user_id = self.updated_by_user_id

        company_id = self.company_id

        external_id: Union[None, str]
        external_id = self.external_id

        work_order_id: Union[None, str]
        work_order_id = self.work_order_id

        notes: Union[None, str]
        notes = self.notes

        attachments: Union[None, list[dict[str, Any]]]
        if isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

        attachment_ids: Union[None, list[str]]
        if isinstance(self.attachment_ids, list):
            attachment_ids = self.attachment_ids

        else:
            attachment_ids = self.attachment_ids

        asset_ids: Union[None, list[str]]
        if isinstance(self.asset_ids, list):
            asset_ids = self.asset_ids

        else:
            asset_ids = self.asset_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
                "createdByUserId": created_by_user_id,
                "updatedByUserId": updated_by_user_id,
                "companyId": company_id,
                "externalId": external_id,
                "workOrderId": work_order_id,
                "notes": notes,
                "attachments": attachments,
                "attachmentIds": attachment_ids,
                "assetIds": asset_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_inventory_item_supply import (
            AttachmentInventoryItemSupply,
        )

        d = dict(src_dict)

        def _parse_created_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_at = _parse_created_at(d.pop("createdAt"))

        def _parse_updated_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))

        def _parse_created_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId"))

        def _parse_updated_by_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId"))

        company_id = d.pop("companyId")

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("externalId"))

        def _parse_work_order_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId"))

        def _parse_notes(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        notes = _parse_notes(d.pop("notes"))

        def _parse_attachments(
            data: object,
        ) -> Union[None, list["AttachmentInventoryItemSupply"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = AttachmentInventoryItemSupply.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["AttachmentInventoryItemSupply"]], data)

        attachments = _parse_attachments(d.pop("attachments"))

        def _parse_attachment_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachment_ids_type_0 = cast(list[str], data)

                return attachment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        attachment_ids = _parse_attachment_ids(d.pop("attachmentIds"))

        def _parse_asset_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_ids_type_0 = cast(list[str], data)

                return asset_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        asset_ids = _parse_asset_ids(d.pop("assetIds"))

        add_transfer_request_supply_request = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            company_id=company_id,
            external_id=external_id,
            work_order_id=work_order_id,
            notes=notes,
            attachments=attachments,
            attachment_ids=attachment_ids,
            asset_ids=asset_ids,
        )

        add_transfer_request_supply_request.additional_properties = d
        return add_transfer_request_supply_request

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

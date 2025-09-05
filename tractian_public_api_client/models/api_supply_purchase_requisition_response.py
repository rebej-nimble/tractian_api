from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_requisition_supply_status import (
    PurchaseRequisitionSupplyStatus,
    check_purchase_requisition_supply_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_purchase_requisition_item import (
        ApiSupplyPurchaseRequisitionItem,
    )
    from ..models.boolean_custom_field import BooleanCustomField
    from ..models.check_list_custom_field import CheckListCustomField
    from ..models.currency_custom_field import CurrencyCustomField
    from ..models.date_custom_field import DateCustomField
    from ..models.number_custom_field import NumberCustomField
    from ..models.selection_list_custom_field import SelectionListCustomField
    from ..models.text_custom_field import TextCustomField


T = TypeVar("T", bound="ApiSupplyPurchaseRequisitionResponse")


@_attrs_define
class ApiSupplyPurchaseRequisitionResponse:
    id: str
    number: int
    created_at: str
    updated_at: str
    created_by_user_id: str
    updated_by_user_id: str
    company_id: str
    status: PurchaseRequisitionSupplyStatus
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    canceled_at: Union[None, Unset, str] = UNSET
    identifier_code: Union[None, Unset, str] = UNSET
    priority: Union[None, Unset, str] = UNSET
    work_order_id: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    attachment_ids: Union[None, Unset, list[str]] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    system_created: Union[None, Unset, bool] = UNSET
    reject_reason_notes: Union[None, Unset, str] = UNSET
    reject_reason_id: Union[None, Unset, str] = UNSET
    reviewed_at: Union[None, Unset, str] = UNSET
    purchase_requisition_items: Union[
        None, Unset, list["ApiSupplyPurchaseRequisitionItem"]
    ] = UNSET
    custom_fields: Union[
        None,
        Unset,
        list[
            Union[
                "BooleanCustomField",
                "CheckListCustomField",
                "CurrencyCustomField",
                "DateCustomField",
                "NumberCustomField",
                "SelectionListCustomField",
                "TextCustomField",
            ]
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField

        id = self.id

        number = self.number

        created_at = self.created_at

        updated_at = self.updated_at

        created_by_user_id = self.created_by_user_id

        updated_by_user_id = self.updated_by_user_id

        company_id = self.company_id

        status: str = self.status

        canceled_by_user_id: Union[None, Unset, str]
        if isinstance(self.canceled_by_user_id, Unset):
            canceled_by_user_id = UNSET
        else:
            canceled_by_user_id = self.canceled_by_user_id

        canceled_at: Union[None, Unset, str]
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = self.canceled_at

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        attachment_ids: Union[None, Unset, list[str]]
        if isinstance(self.attachment_ids, Unset):
            attachment_ids = UNSET
        elif isinstance(self.attachment_ids, list):
            attachment_ids = self.attachment_ids

        else:
            attachment_ids = self.attachment_ids

        assigned_user_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_user_ids, Unset):
            assigned_user_ids = UNSET
        elif isinstance(self.assigned_user_ids, list):
            assigned_user_ids = self.assigned_user_ids

        else:
            assigned_user_ids = self.assigned_user_ids

        assigned_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids

        else:
            assigned_team_ids = self.assigned_team_ids

        system_created: Union[None, Unset, bool]
        if isinstance(self.system_created, Unset):
            system_created = UNSET
        else:
            system_created = self.system_created

        reject_reason_notes: Union[None, Unset, str]
        if isinstance(self.reject_reason_notes, Unset):
            reject_reason_notes = UNSET
        else:
            reject_reason_notes = self.reject_reason_notes

        reject_reason_id: Union[None, Unset, str]
        if isinstance(self.reject_reason_id, Unset):
            reject_reason_id = UNSET
        else:
            reject_reason_id = self.reject_reason_id

        reviewed_at: Union[None, Unset, str]
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        else:
            reviewed_at = self.reviewed_at

        purchase_requisition_items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.purchase_requisition_items, Unset):
            purchase_requisition_items = UNSET
        elif isinstance(self.purchase_requisition_items, list):
            purchase_requisition_items = []
            for (
                purchase_requisition_items_type_0_item_data
            ) in self.purchase_requisition_items:
                purchase_requisition_items_type_0_item = (
                    purchase_requisition_items_type_0_item_data.to_dict()
                )
                purchase_requisition_items.append(
                    purchase_requisition_items_type_0_item
                )

        else:
            purchase_requisition_items = self.purchase_requisition_items

        custom_fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, list):
            custom_fields = []
            for custom_fields_type_0_item_data in self.custom_fields:
                custom_fields_type_0_item: dict[str, Any]
                if isinstance(custom_fields_type_0_item_data, BooleanCustomField):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                elif isinstance(custom_fields_type_0_item_data, CheckListCustomField):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                elif isinstance(custom_fields_type_0_item_data, CurrencyCustomField):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                elif isinstance(custom_fields_type_0_item_data, DateCustomField):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                elif isinstance(custom_fields_type_0_item_data, NumberCustomField):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                elif isinstance(
                    custom_fields_type_0_item_data, SelectionListCustomField
                ):
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                else:
                    custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()

                custom_fields.append(custom_fields_type_0_item)

        else:
            custom_fields = self.custom_fields

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
                "companyId": company_id,
                "status": status,
            }
        )
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if priority is not UNSET:
            field_dict["priority"] = priority
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if attachment_ids is not UNSET:
            field_dict["attachmentIds"] = attachment_ids
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if system_created is not UNSET:
            field_dict["systemCreated"] = system_created
        if reject_reason_notes is not UNSET:
            field_dict["rejectReasonNotes"] = reject_reason_notes
        if reject_reason_id is not UNSET:
            field_dict["rejectReasonId"] = reject_reason_id
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if purchase_requisition_items is not UNSET:
            field_dict["purchaseRequisitionItems"] = purchase_requisition_items
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_purchase_requisition_item import (
            ApiSupplyPurchaseRequisitionItem,
        )
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField
        from ..models.text_custom_field import TextCustomField

        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        created_by_user_id = d.pop("createdByUserId")

        updated_by_user_id = d.pop("updatedByUserId")

        company_id = d.pop("companyId")

        status = check_purchase_requisition_supply_status(d.pop("status"))

        def _parse_canceled_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_by_user_id = _parse_canceled_by_user_id(
            d.pop("canceledByUserId", UNSET)
        )

        def _parse_canceled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        canceled_at = _parse_canceled_at(d.pop("canceledAt", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_priority(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_attachment_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachment_ids_type_0 = cast(list[str], data)

                return attachment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        attachment_ids = _parse_attachment_ids(d.pop("attachmentIds", UNSET))

        def _parse_assigned_user_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_user_ids_type_0 = cast(list[str], data)

                return assigned_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_user_ids = _parse_assigned_user_ids(d.pop("assignedUserIds", UNSET))

        def _parse_assigned_team_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assignedTeamIds", UNSET))

        def _parse_system_created(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        system_created = _parse_system_created(d.pop("systemCreated", UNSET))

        def _parse_reject_reason_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reject_reason_notes = _parse_reject_reason_notes(
            d.pop("rejectReasonNotes", UNSET)
        )

        def _parse_reject_reason_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reject_reason_id = _parse_reject_reason_id(d.pop("rejectReasonId", UNSET))

        def _parse_reviewed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewedAt", UNSET))

        def _parse_purchase_requisition_items(
            data: object,
        ) -> Union[None, Unset, list["ApiSupplyPurchaseRequisitionItem"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purchase_requisition_items_type_0 = []
                _purchase_requisition_items_type_0 = data
                for (
                    purchase_requisition_items_type_0_item_data
                ) in _purchase_requisition_items_type_0:
                    purchase_requisition_items_type_0_item = (
                        ApiSupplyPurchaseRequisitionItem.from_dict(
                            purchase_requisition_items_type_0_item_data
                        )
                    )

                    purchase_requisition_items_type_0.append(
                        purchase_requisition_items_type_0_item
                    )

                return purchase_requisition_items_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ApiSupplyPurchaseRequisitionItem"]], data
            )

        purchase_requisition_items = _parse_purchase_requisition_items(
            d.pop("purchaseRequisitionItems", UNSET)
        )

        def _parse_custom_fields(
            data: object,
        ) -> Union[
            None,
            Unset,
            list[
                Union[
                    "BooleanCustomField",
                    "CheckListCustomField",
                    "CurrencyCustomField",
                    "DateCustomField",
                    "NumberCustomField",
                    "SelectionListCustomField",
                    "TextCustomField",
                ]
            ],
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_fields_type_0 = []
                _custom_fields_type_0 = data
                for custom_fields_type_0_item_data in _custom_fields_type_0:

                    def _parse_custom_fields_type_0_item(
                        data: object,
                    ) -> Union[
                        "BooleanCustomField",
                        "CheckListCustomField",
                        "CurrencyCustomField",
                        "DateCustomField",
                        "NumberCustomField",
                        "SelectionListCustomField",
                        "TextCustomField",
                    ]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_0 = (
                                BooleanCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_1 = (
                                CheckListCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_1
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_2 = (
                                CurrencyCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_2
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_3 = (
                                DateCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_3
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_4 = (
                                NumberCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_4
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            custom_fields_type_0_item_type_5 = (
                                SelectionListCustomField.from_dict(data)
                            )

                            return custom_fields_type_0_item_type_5
                        except:  # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        custom_fields_type_0_item_type_6 = TextCustomField.from_dict(
                            data
                        )

                        return custom_fields_type_0_item_type_6

                    custom_fields_type_0_item = _parse_custom_fields_type_0_item(
                        custom_fields_type_0_item_data
                    )

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list[
                        Union[
                            "BooleanCustomField",
                            "CheckListCustomField",
                            "CurrencyCustomField",
                            "DateCustomField",
                            "NumberCustomField",
                            "SelectionListCustomField",
                            "TextCustomField",
                        ]
                    ],
                ],
                data,
            )

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))

        api_supply_purchase_requisition_response = cls(
            id=id,
            number=number,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            company_id=company_id,
            status=status,
            canceled_by_user_id=canceled_by_user_id,
            canceled_at=canceled_at,
            identifier_code=identifier_code,
            priority=priority,
            work_order_id=work_order_id,
            notes=notes,
            attachment_ids=attachment_ids,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            system_created=system_created,
            reject_reason_notes=reject_reason_notes,
            reject_reason_id=reject_reason_id,
            reviewed_at=reviewed_at,
            purchase_requisition_items=purchase_requisition_items,
            custom_fields=custom_fields,
        )

        api_supply_purchase_requisition_response.additional_properties = d
        return api_supply_purchase_requisition_response

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

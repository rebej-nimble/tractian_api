from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.purchase_requisition_priority import (
    PurchaseRequisitionPriority,
    check_purchase_requisition_priority,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_purchase_requisition_item_request import (
        ApiSupplyPurchaseRequisitionItemRequest,
    )
    from ..models.boolean_custom_field import BooleanCustomField
    from ..models.check_list_custom_field import CheckListCustomField
    from ..models.currency_custom_field import CurrencyCustomField
    from ..models.date_custom_field import DateCustomField
    from ..models.number_custom_field import NumberCustomField
    from ..models.selection_list_custom_field import SelectionListCustomField
    from ..models.text_custom_field import TextCustomField


T = TypeVar("T", bound="ApiSupplyPurchaseRequisitionRequest")


@_attrs_define
class ApiSupplyPurchaseRequisitionRequest:
    company_id: str
    """ The company id """
    created_at: Union[None, Unset, str] = UNSET
    """ The date when the purchase requisition was created """
    updated_at: Union[None, Unset, str] = UNSET
    """ The date when the purchase requisition was updated """
    created_by_user_id: Union[None, Unset, str] = UNSET
    """ The userId who created the purchase requisition """
    updated_by_user_id: Union[None, Unset, str] = UNSET
    """ The userId who updated the purchase requisition """
    work_order_id: Union[None, Unset, str] = UNSET
    """ The work order id, to be attached to the purchase requisition """
    identifier_code: Union[None, Unset, str] = UNSET
    """ The identifier code of the purchase requisition """
    priority: Union[None, PurchaseRequisitionPriority, Unset] = UNSET
    """ The priority of the purchase requisition """
    notes: Union[None, Unset, str] = UNSET
    """ The notes of the purchase requisition, free text field """
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    """ The user ids assigned to the purchase requisition """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ The team ids assigned to the purchase requisition """
    reject_reason_notes: Union[None, Unset, str] = UNSET
    """ The reason for rejecting the purchase requisition, free text field """
    reject_reason_id: Union[None, Unset, str] = UNSET
    """ The reason for rejecting the purchase requisition """
    reviewed_at: Union[None, Unset, str] = UNSET
    """ The date and time the purchase requisition was reviewed """
    purchase_requisition_items: Union[
        None, Unset, list["ApiSupplyPurchaseRequisitionItemRequest"]
    ] = UNSET
    """ The items of the purchase requisition """
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
    """ The custom fields of the purchase requisition """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField

        company_id = self.company_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        created_by_user_id: Union[None, Unset, str]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        updated_by_user_id: Union[None, Unset, str]
        if isinstance(self.updated_by_user_id, Unset):
            updated_by_user_id = UNSET
        else:
            updated_by_user_id = self.updated_by_user_id

        work_order_id: Union[None, Unset, str]
        if isinstance(self.work_order_id, Unset):
            work_order_id = UNSET
        else:
            work_order_id = self.work_order_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, str):
            priority = self.priority
        else:
            priority = self.priority

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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
                "companyId": company_id,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if updated_by_user_id is not UNSET:
            field_dict["updatedByUserId"] = updated_by_user_id
        if work_order_id is not UNSET:
            field_dict["workOrderId"] = work_order_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if priority is not UNSET:
            field_dict["priority"] = priority
        if notes is not UNSET:
            field_dict["notes"] = notes
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
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
        from ..models.api_supply_purchase_requisition_item_request import (
            ApiSupplyPurchaseRequisitionItemRequest,
        )
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField
        from ..models.text_custom_field import TextCustomField

        d = dict(src_dict)
        company_id = d.pop("companyId")

        def _parse_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

        def _parse_updated_by_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_user_id = _parse_updated_by_user_id(d.pop("updatedByUserId", UNSET))

        def _parse_work_order_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_order_id = _parse_work_order_id(d.pop("workOrderId", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_priority(
            data: object,
        ) -> Union[None, PurchaseRequisitionPriority, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = check_purchase_requisition_priority(data)

                return priority_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PurchaseRequisitionPriority, Unset], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

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
        ) -> Union[None, Unset, list["ApiSupplyPurchaseRequisitionItemRequest"]]:
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
                        ApiSupplyPurchaseRequisitionItemRequest.from_dict(
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
                Union[None, Unset, list["ApiSupplyPurchaseRequisitionItemRequest"]],
                data,
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

        api_supply_purchase_requisition_request = cls(
            company_id=company_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by_user_id=created_by_user_id,
            updated_by_user_id=updated_by_user_id,
            work_order_id=work_order_id,
            identifier_code=identifier_code,
            priority=priority,
            notes=notes,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            reject_reason_notes=reject_reason_notes,
            reject_reason_id=reject_reason_id,
            reviewed_at=reviewed_at,
            purchase_requisition_items=purchase_requisition_items,
            custom_fields=custom_fields,
        )

        api_supply_purchase_requisition_request.additional_properties = d
        return api_supply_purchase_requisition_request

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

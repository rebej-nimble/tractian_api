from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_supply_other_costs import ApiSupplyOtherCosts
    from ..models.boolean_custom_field import BooleanCustomField
    from ..models.check_list_custom_field import CheckListCustomField
    from ..models.currency_custom_field import CurrencyCustomField
    from ..models.date_custom_field import DateCustomField
    from ..models.number_custom_field import NumberCustomField
    from ..models.selection_list_custom_field import SelectionListCustomField
    from ..models.supply_file_request import SupplyFileRequest
    from ..models.text_custom_field import TextCustomField


T = TypeVar("T", bound="ApiSupplyPurchaseOrderRequest")


@_attrs_define
class ApiSupplyPurchaseOrderRequest:
    id: str
    identifier_code: Union[None, Unset, str] = UNSET
    """ The identifier code of the purchase order """
    external_id: Union[None, Unset, str] = UNSET
    """ The external id of the purchase order """
    notes: Union[None, Unset, str] = UNSET
    """ The notes of the purchase order """
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    """ The assigned user ids of the purchase order """
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
    """ The assigned team ids of the purchase order """
    canceled_by_user_id: Union[None, Unset, str] = UNSET
    """ The canceled by user id of the purchase order """
    canceled_at: Union[None, Unset, str] = UNSET
    """ The canceled at of the purchase order """
    supplier_id: Union[None, Unset, str] = UNSET
    """ The supplier id of the purchase order """
    contract_id: Union[None, Unset, str] = UNSET
    """ The contract id of the purchase order """
    external_code: Union[None, Unset, str] = UNSET
    """ The external code of the purchase order """
    payment_term_id: Union[None, Unset, str] = UNSET
    """ The payment term id of the purchase order """
    payment_method_id: Union[None, Unset, str] = UNSET
    """ The payment method id of the purchase order """
    shipping_cost: Union[None, Unset, float] = UNSET
    """ The shipping cost of the purchase order """
    shipping_type_id: Union[None, Unset, str] = UNSET
    """ The shipping type id of the purchase order """
    other_costs: Union["ApiSupplyOtherCosts", None, Unset] = UNSET
    """ The other costs of the purchase order """
    new_contract: Union["ApiSupplyOtherCosts", None, Unset] = UNSET
    """ The new contract of the purchase order """
    attachments: Union[None, Unset, list["SupplyFileRequest"]] = UNSET
    """ The attachments of the purchase order """
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
        from ..models.api_supply_other_costs import ApiSupplyOtherCosts
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField

        id = self.id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        supplier_id: Union[None, Unset, str]
        if isinstance(self.supplier_id, Unset):
            supplier_id = UNSET
        else:
            supplier_id = self.supplier_id

        contract_id: Union[None, Unset, str]
        if isinstance(self.contract_id, Unset):
            contract_id = UNSET
        else:
            contract_id = self.contract_id

        external_code: Union[None, Unset, str]
        if isinstance(self.external_code, Unset):
            external_code = UNSET
        else:
            external_code = self.external_code

        payment_term_id: Union[None, Unset, str]
        if isinstance(self.payment_term_id, Unset):
            payment_term_id = UNSET
        else:
            payment_term_id = self.payment_term_id

        payment_method_id: Union[None, Unset, str]
        if isinstance(self.payment_method_id, Unset):
            payment_method_id = UNSET
        else:
            payment_method_id = self.payment_method_id

        shipping_cost: Union[None, Unset, float]
        if isinstance(self.shipping_cost, Unset):
            shipping_cost = UNSET
        else:
            shipping_cost = self.shipping_cost

        shipping_type_id: Union[None, Unset, str]
        if isinstance(self.shipping_type_id, Unset):
            shipping_type_id = UNSET
        else:
            shipping_type_id = self.shipping_type_id

        other_costs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.other_costs, Unset):
            other_costs = UNSET
        elif isinstance(self.other_costs, ApiSupplyOtherCosts):
            other_costs = self.other_costs.to_dict()
        else:
            other_costs = self.other_costs

        new_contract: Union[None, Unset, dict[str, Any]]
        if isinstance(self.new_contract, Unset):
            new_contract = UNSET
        elif isinstance(self.new_contract, ApiSupplyOtherCosts):
            new_contract = self.new_contract.to_dict()
        else:
            new_contract = self.new_contract

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
            }
        )
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if canceled_by_user_id is not UNSET:
            field_dict["canceledByUserId"] = canceled_by_user_id
        if canceled_at is not UNSET:
            field_dict["canceledAt"] = canceled_at
        if supplier_id is not UNSET:
            field_dict["supplierId"] = supplier_id
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if external_code is not UNSET:
            field_dict["externalCode"] = external_code
        if payment_term_id is not UNSET:
            field_dict["paymentTermId"] = payment_term_id
        if payment_method_id is not UNSET:
            field_dict["paymentMethodId"] = payment_method_id
        if shipping_cost is not UNSET:
            field_dict["shippingCost"] = shipping_cost
        if shipping_type_id is not UNSET:
            field_dict["shippingTypeId"] = shipping_type_id
        if other_costs is not UNSET:
            field_dict["otherCosts"] = other_costs
        if new_contract is not UNSET:
            field_dict["newContract"] = new_contract
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_supply_other_costs import ApiSupplyOtherCosts
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField
        from ..models.supply_file_request import SupplyFileRequest
        from ..models.text_custom_field import TextCustomField

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        def _parse_supplier_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supplier_id = _parse_supplier_id(d.pop("supplierId", UNSET))

        def _parse_contract_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contract_id = _parse_contract_id(d.pop("contractId", UNSET))

        def _parse_external_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_code = _parse_external_code(d.pop("externalCode", UNSET))

        def _parse_payment_term_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_term_id = _parse_payment_term_id(d.pop("paymentTermId", UNSET))

        def _parse_payment_method_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_method_id = _parse_payment_method_id(d.pop("paymentMethodId", UNSET))

        def _parse_shipping_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shipping_cost = _parse_shipping_cost(d.pop("shippingCost", UNSET))

        def _parse_shipping_type_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_type_id = _parse_shipping_type_id(d.pop("shippingTypeId", UNSET))

        def _parse_other_costs(
            data: object,
        ) -> Union["ApiSupplyOtherCosts", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_costs_type_0 = ApiSupplyOtherCosts.from_dict(data)

                return other_costs_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplyOtherCosts", None, Unset], data)

        other_costs = _parse_other_costs(d.pop("otherCosts", UNSET))

        def _parse_new_contract(
            data: object,
        ) -> Union["ApiSupplyOtherCosts", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_contract_type_0 = ApiSupplyOtherCosts.from_dict(data)

                return new_contract_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiSupplyOtherCosts", None, Unset], data)

        new_contract = _parse_new_contract(d.pop("newContract", UNSET))

        def _parse_attachments(
            data: object,
        ) -> Union[None, Unset, list["SupplyFileRequest"]]:
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
                    attachments_type_0_item = SupplyFileRequest.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SupplyFileRequest"]], data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

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

        api_supply_purchase_order_request = cls(
            id=id,
            identifier_code=identifier_code,
            external_id=external_id,
            notes=notes,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            canceled_by_user_id=canceled_by_user_id,
            canceled_at=canceled_at,
            supplier_id=supplier_id,
            contract_id=contract_id,
            external_code=external_code,
            payment_term_id=payment_term_id,
            payment_method_id=payment_method_id,
            shipping_cost=shipping_cost,
            shipping_type_id=shipping_type_id,
            other_costs=other_costs,
            new_contract=new_contract,
            attachments=attachments,
            custom_fields=custom_fields,
        )

        api_supply_purchase_order_request.additional_properties = d
        return api_supply_purchase_order_request

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

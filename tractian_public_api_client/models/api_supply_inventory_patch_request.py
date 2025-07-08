from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supply_abc_classification import (
    SupplyAbcClassification,
    check_supply_abc_classification,
)
from ..models.supply_stock_valuation_method import (
    SupplyStockValuationMethod,
    check_supply_stock_valuation_method,
)
from ..models.supply_xyz_classification import (
    SupplyXyzClassification,
    check_supply_xyz_classification,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_custom_field import BooleanCustomField
    from ..models.check_list_custom_field import CheckListCustomField
    from ..models.currency_custom_field import CurrencyCustomField
    from ..models.date_custom_field import DateCustomField
    from ..models.number_custom_field import NumberCustomField
    from ..models.selection_list_custom_field import SelectionListCustomField
    from ..models.supply_code_request import SupplyCodeRequest
    from ..models.supply_file_request import SupplyFileRequest
    from ..models.text_custom_field import TextCustomField


T = TypeVar("T", bound="ApiSupplyInventoryPatchRequest")


@_attrs_define
class ApiSupplyInventoryPatchRequest:
    name: str
    """ Name of the item. """
    description: Union[None, Unset, str] = UNSET
    """ Description of the item. """
    company_id: Union[None, Unset, str] = UNSET
    """ Supply item company id. """
    identifier_code: Union[None, Unset, str] = UNSET
    assigned_user_ids: Union[None, Unset, list[str]] = UNSET
    assigned_team_ids: Union[None, Unset, list[str]] = UNSET
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
    measurement_unit_id: Union[None, Unset, str] = UNSET
    """ Measurement unit id. """
    stock_valuation_method: Union[None, SupplyStockValuationMethod, Unset] = UNSET
    item_category_id: Union[None, Unset, str] = UNSET
    """ Item category id. """
    abc_classification: Union[None, SupplyAbcClassification, Unset] = UNSET
    xyz_classification: Union[None, SupplyXyzClassification, Unset] = UNSET
    ncm_and_hs_code: Union[None, Unset, str] = UNSET
    code: Union["SupplyCodeRequest", None, Unset] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    lead_time: Union[None, Unset, int] = UNSET
    purchase_user_ids: Union[None, Unset, list[str]] = UNSET
    purchase_team_ids: Union[None, Unset, list[str]] = UNSET
    supplier_ids: Union[None, Unset, list[str]] = UNSET
    attachments: Union[None, Unset, list["SupplyFileRequest"]] = UNSET
    image: Union["SupplyFileRequest", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField
        from ..models.supply_code_request import SupplyCodeRequest
        from ..models.supply_file_request import SupplyFileRequest

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        company_id: Union[None, Unset, str]
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        identifier_code: Union[None, Unset, str]
        if isinstance(self.identifier_code, Unset):
            identifier_code = UNSET
        else:
            identifier_code = self.identifier_code

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

        measurement_unit_id: Union[None, Unset, str]
        if isinstance(self.measurement_unit_id, Unset):
            measurement_unit_id = UNSET
        else:
            measurement_unit_id = self.measurement_unit_id

        stock_valuation_method: Union[None, Unset, str]
        if isinstance(self.stock_valuation_method, Unset):
            stock_valuation_method = UNSET
        elif isinstance(self.stock_valuation_method, str):
            stock_valuation_method = self.stock_valuation_method
        else:
            stock_valuation_method = self.stock_valuation_method

        item_category_id: Union[None, Unset, str]
        if isinstance(self.item_category_id, Unset):
            item_category_id = UNSET
        else:
            item_category_id = self.item_category_id

        abc_classification: Union[None, Unset, str]
        if isinstance(self.abc_classification, Unset):
            abc_classification = UNSET
        elif isinstance(self.abc_classification, str):
            abc_classification = self.abc_classification
        else:
            abc_classification = self.abc_classification

        xyz_classification: Union[None, Unset, str]
        if isinstance(self.xyz_classification, Unset):
            xyz_classification = UNSET
        elif isinstance(self.xyz_classification, str):
            xyz_classification = self.xyz_classification
        else:
            xyz_classification = self.xyz_classification

        ncm_and_hs_code: Union[None, Unset, str]
        if isinstance(self.ncm_and_hs_code, Unset):
            ncm_and_hs_code = UNSET
        else:
            ncm_and_hs_code = self.ncm_and_hs_code

        code: Union[None, Unset, dict[str, Any]]
        if isinstance(self.code, Unset):
            code = UNSET
        elif isinstance(self.code, SupplyCodeRequest):
            code = self.code.to_dict()
        else:
            code = self.code

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        lead_time: Union[None, Unset, int]
        if isinstance(self.lead_time, Unset):
            lead_time = UNSET
        else:
            lead_time = self.lead_time

        purchase_user_ids: Union[None, Unset, list[str]]
        if isinstance(self.purchase_user_ids, Unset):
            purchase_user_ids = UNSET
        elif isinstance(self.purchase_user_ids, list):
            purchase_user_ids = self.purchase_user_ids

        else:
            purchase_user_ids = self.purchase_user_ids

        purchase_team_ids: Union[None, Unset, list[str]]
        if isinstance(self.purchase_team_ids, Unset):
            purchase_team_ids = UNSET
        elif isinstance(self.purchase_team_ids, list):
            purchase_team_ids = self.purchase_team_ids

        else:
            purchase_team_ids = self.purchase_team_ids

        supplier_ids: Union[None, Unset, list[str]]
        if isinstance(self.supplier_ids, Unset):
            supplier_ids = UNSET
        elif isinstance(self.supplier_ids, list):
            supplier_ids = self.supplier_ids

        else:
            supplier_ids = self.supplier_ids

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

        image: Union[None, Unset, dict[str, Any]]
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, SupplyFileRequest):
            image = self.image.to_dict()
        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if identifier_code is not UNSET:
            field_dict["identifierCode"] = identifier_code
        if assigned_user_ids is not UNSET:
            field_dict["assignedUserIds"] = assigned_user_ids
        if assigned_team_ids is not UNSET:
            field_dict["assignedTeamIds"] = assigned_team_ids
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if measurement_unit_id is not UNSET:
            field_dict["measurementUnitId"] = measurement_unit_id
        if stock_valuation_method is not UNSET:
            field_dict["stockValuationMethod"] = stock_valuation_method
        if item_category_id is not UNSET:
            field_dict["itemCategoryId"] = item_category_id
        if abc_classification is not UNSET:
            field_dict["abcClassification"] = abc_classification
        if xyz_classification is not UNSET:
            field_dict["xyzClassification"] = xyz_classification
        if ncm_and_hs_code is not UNSET:
            field_dict["ncmAndHsCode"] = ncm_and_hs_code
        if code is not UNSET:
            field_dict["code"] = code
        if tags is not UNSET:
            field_dict["tags"] = tags
        if lead_time is not UNSET:
            field_dict["leadTime"] = lead_time
        if purchase_user_ids is not UNSET:
            field_dict["purchaseUserIds"] = purchase_user_ids
        if purchase_team_ids is not UNSET:
            field_dict["purchaseTeamIds"] = purchase_team_ids
        if supplier_ids is not UNSET:
            field_dict["supplierIds"] = supplier_ids
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_custom_field import BooleanCustomField
        from ..models.check_list_custom_field import CheckListCustomField
        from ..models.currency_custom_field import CurrencyCustomField
        from ..models.date_custom_field import DateCustomField
        from ..models.number_custom_field import NumberCustomField
        from ..models.selection_list_custom_field import SelectionListCustomField
        from ..models.supply_code_request import SupplyCodeRequest
        from ..models.supply_file_request import SupplyFileRequest
        from ..models.text_custom_field import TextCustomField

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_company_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_id = _parse_company_id(d.pop("companyId", UNSET))

        def _parse_identifier_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier_code = _parse_identifier_code(d.pop("identifierCode", UNSET))

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

        def _parse_measurement_unit_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        measurement_unit_id = _parse_measurement_unit_id(
            d.pop("measurementUnitId", UNSET)
        )

        def _parse_stock_valuation_method(
            data: object,
        ) -> Union[None, SupplyStockValuationMethod, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stock_valuation_method_type_0 = check_supply_stock_valuation_method(
                    data
                )

                return stock_valuation_method_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SupplyStockValuationMethod, Unset], data)

        stock_valuation_method = _parse_stock_valuation_method(
            d.pop("stockValuationMethod", UNSET)
        )

        def _parse_item_category_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_category_id = _parse_item_category_id(d.pop("itemCategoryId", UNSET))

        def _parse_abc_classification(
            data: object,
        ) -> Union[None, SupplyAbcClassification, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                abc_classification_type_0 = check_supply_abc_classification(data)

                return abc_classification_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SupplyAbcClassification, Unset], data)

        abc_classification = _parse_abc_classification(
            d.pop("abcClassification", UNSET)
        )

        def _parse_xyz_classification(
            data: object,
        ) -> Union[None, SupplyXyzClassification, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                xyz_classification_type_0 = check_supply_xyz_classification(data)

                return xyz_classification_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SupplyXyzClassification, Unset], data)

        xyz_classification = _parse_xyz_classification(
            d.pop("xyzClassification", UNSET)
        )

        def _parse_ncm_and_hs_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ncm_and_hs_code = _parse_ncm_and_hs_code(d.pop("ncmAndHsCode", UNSET))

        def _parse_code(data: object) -> Union["SupplyCodeRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                code_type_0 = SupplyCodeRequest.from_dict(data)

                return code_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SupplyCodeRequest", None, Unset], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_lead_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lead_time = _parse_lead_time(d.pop("leadTime", UNSET))

        def _parse_purchase_user_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purchase_user_ids_type_0 = cast(list[str], data)

                return purchase_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        purchase_user_ids = _parse_purchase_user_ids(d.pop("purchaseUserIds", UNSET))

        def _parse_purchase_team_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purchase_team_ids_type_0 = cast(list[str], data)

                return purchase_team_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        purchase_team_ids = _parse_purchase_team_ids(d.pop("purchaseTeamIds", UNSET))

        def _parse_supplier_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supplier_ids_type_0 = cast(list[str], data)

                return supplier_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        supplier_ids = _parse_supplier_ids(d.pop("supplierIds", UNSET))

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

        def _parse_image(data: object) -> Union["SupplyFileRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_0 = SupplyFileRequest.from_dict(data)

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SupplyFileRequest", None, Unset], data)

        image = _parse_image(d.pop("image", UNSET))

        api_supply_inventory_patch_request = cls(
            name=name,
            description=description,
            company_id=company_id,
            identifier_code=identifier_code,
            assigned_user_ids=assigned_user_ids,
            assigned_team_ids=assigned_team_ids,
            custom_fields=custom_fields,
            measurement_unit_id=measurement_unit_id,
            stock_valuation_method=stock_valuation_method,
            item_category_id=item_category_id,
            abc_classification=abc_classification,
            xyz_classification=xyz_classification,
            ncm_and_hs_code=ncm_and_hs_code,
            code=code,
            tags=tags,
            lead_time=lead_time,
            purchase_user_ids=purchase_user_ids,
            purchase_team_ids=purchase_team_ids,
            supplier_ids=supplier_ids,
            attachments=attachments,
            image=image,
        )

        api_supply_inventory_patch_request.additional_properties = d
        return api_supply_inventory_patch_request

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

"""Contains all the data models used in inputs/outputs"""

from .activity_alternative_value_motor import ActivityAlternativeValueMotor
from .activity_procedure_field_option import ActivityProcedureFieldOption
from .activity_procedure_value import ActivityProcedureValue
from .add_asset_motor import AddAssetMotor
from .add_asset_motor_attachment import AddAssetMotorAttachment
from .add_asset_motor_attachment_file_convertion import (
    AddAssetMotorAttachmentFileConvertion,
)
from .api_supply_inventory_adjustment_request import ApiSupplyInventoryAdjustmentRequest
from .api_supply_inventory_patch_request import ApiSupplyInventoryPatchRequest
from .api_supply_item_category import ApiSupplyItemCategory
from .api_supply_item_category_request import ApiSupplyItemCategoryRequest
from .api_supply_item_storage_response import ApiSupplyItemStorageResponse
from .asset import Asset
from .asset_attachment_motor import AssetAttachmentMotor
from .asset_components_motor import AssetComponentsMotor
from .asset_criticality_motor import AssetCriticalityMotor
from .asset_image_motor import AssetImageMotor
from .asset_inventory_item_motor import AssetInventoryItemMotor
from .asset_location_motor import AssetLocationMotor
from .asset_user_motor import AssetUserMotor
from .axis_data import AxisData
from .balance import Balance
from .batch import Batch
from .bearing_motor import BearingMotor
from .bearing_motor_fault_frequencies_type_0 import BearingMotorFaultFrequenciesType0
from .boolean_custom_field import BooleanCustomField
from .category_other_costs import CategoryOtherCosts
from .check_list_custom_field import CheckListCustomField
from .checklist import Checklist
from .code import Code
from .code_type import CodeType
from .comments_motor import CommentsMotor
from .components_motor import ComponentsMotor
from .consumption_samples_with_tariff_station import ConsumptionSamplesWithTariffStation
from .consumption_samples_without_tariff_station import (
    ConsumptionSamplesWithoutTariffStation,
)
from .cost_samples_with_tariff_station import CostSamplesWithTariffStation
from .cost_samples_without_tariff_station import CostSamplesWithoutTariffStation
from .currency_custom_field import CurrencyCustomField
from .current_review_cycle_motor import CurrentReviewCycleMotor
from .date_custom_field import DateCustomField
from .deleted import Deleted
from .deleted_info import DeletedInfo
from .demand_samples_with_tariff_station import DemandSamplesWithTariffStation
from .demand_samples_without_tariff_station import DemandSamplesWithoutTariffStation
from .disabled import Disabled
from .disabled_info import DisabledInfo
from .entity_custom_field import EntityCustomField
from .entity_custom_field_value_type_5_item import EntityCustomFieldValueType5Item
from .entity_custom_field_value_type_6 import EntityCustomFieldValueType6
from .entity_custom_field_value_type_7_item import EntityCustomFieldValueType7Item
from .entity_custom_field_value_type_8 import EntityCustomFieldValueType8
from .entity_custom_field_value_type_9 import EntityCustomFieldValueType9
from .entity_custom_field_value_type_10 import EntityCustomFieldValueType10
from .event_cerberus import EventCerberus
from .event_type import EventType
from .feedback_request_user_motor import FeedbackRequestUserMotor
from .feedback_requests_motor import FeedbackRequestsMotor
from .fields_motor import FieldsMotor
from .file_motor import FileMotor
from .fix_status import FixStatus
from .generated_workorder import GeneratedWorkorder
from .global_units_samples import GlobalUnitsSamples
from .heading import Heading
from .http_validation_error import HTTPValidationError
from .identified_asset_failures import IdentifiedAssetFailures
from .inbound_batch import InboundBatch
from .insight_cerberus import InsightCerberus
from .insight_status import InsightStatus
from .inspection_custom import InspectionCustom
from .inspection_list import InspectionList
from .inspection_motor import InspectionMotor
from .inspection_status import InspectionStatus
from .inventory_adjustment_position_supply_request import (
    InventoryAdjustmentPositionSupplyRequest,
)
from .inventory_adjustment_type_enum import InventoryAdjustmentTypeEnum
from .inventory_adjustments_inbound_batch_supply_request import (
    InventoryAdjustmentsInboundBatchSupplyRequest,
)
from .inventory_items_cost import InventoryItemsCost
from .inventory_mongo_db import InventoryMongoDB
from .inventory_mongo_db_asset import InventoryMongoDBAsset
from .inventory_mongo_db_asset_asset_type_0 import InventoryMongoDBAssetAssetType0
from .inventory_motor_request_api import InventoryMotorRequestAPI
from .inventory_motor_request_batch_api import InventoryMotorRequestBatchAPI
from .inventory_motor_request_disabled_api import InventoryMotorRequestDisabledAPI
from .inventory_motor_restock_batches_request_api import (
    InventoryMotorRestockBatchesRequestAPI,
)
from .inventory_motor_restock_request_api import InventoryMotorRestockRequestAPI
from .inventory_restock_api import InventoryRestockAPI
from .inventory_restock_batches_api import InventoryRestockBatchesAPI
from .item_category_type_enum import ItemCategoryTypeEnum
from .item_reservation_motor import ItemReservationMotor
from .item_reservation_motor_delete import ItemReservationMotorDelete
from .item_reservation_motor_selected_batch import ItemReservationMotorSelectedBatch
from .item_reservation_request_api import ItemReservationRequestAPI
from .item_reservation_request_selected_batches_api import (
    ItemReservationRequestSelectedBatchesAPI,
)
from .item_reservation_update_api import ItemReservationUpdateAPI
from .level_motor import LevelMotor
from .location import Location
from .material_type import MaterialType
from .measurement_unit import MeasurementUnit
from .metrics import Metrics
from .metrics_field_values import MetricsFieldValues
from .new_inbound_batch_supply_request import NewInboundBatchSupplyRequest
from .number_custom_field import NumberCustomField
from .other_cost import OtherCost
from .pagination_api_supply_item_category_response import (
    PaginationApiSupplyItemCategoryResponse,
)
from .pagination_api_supply_item_storage_response import (
    PaginationApiSupplyItemStorageResponse,
)
from .pagination_dto_asset_motor import PaginationDTOAssetMotor
from .pagination_event_cerberus import PaginationEventCerberus
from .pagination_insight_cerberus import PaginationInsightCerberus
from .pagination_item_reservation_motor import PaginationItemReservationMotor
from .pagination_requests_motor import PaginationRequestsMotor
from .pagination_work_order_operation_motor import PaginationWorkOrderOperationMotor
from .pagination_work_orders_motor import PaginationWorkOrdersMotor
from .pagination_work_orders_others_costs_motor import (
    PaginationWorkOrdersOthersCostsMotor,
)
from .parent_info_request_motor import ParentInfoRequestMotor
from .parent_info_request_motor_option_type_0 import ParentInfoRequestMotorOptionType0
from .parent_work_order_operation_procedure_fields import (
    ParentWorkOrderOperationProcedureFields,
)
from .parent_work_order_operation_procedure_fields_levels import (
    ParentWorkOrderOperationProcedureFieldsLevels,
)
from .parent_work_order_operation_procedure_request_motor import (
    ParentWorkOrderOperationProcedureRequestMotor,
)
from .phase_values import PhaseValues
from .procedure_motor import ProcedureMotor
from .purchase_orders import PurchaseOrders
from .request import Request
from .request_template_categories_motor import RequestTemplateCategoriesMotor
from .requests_motor import RequestsMotor
from .requests_template import RequestsTemplate
from .requests_template_category import RequestsTemplateCategory
from .requests_template_identified_asset_failures import (
    RequestsTemplateIdentifiedAssetFailures,
)
from .selection_list_custom_field import SelectionListCustomField
from .simplified_rpm_sample_data import SimplifiedRpmSampleData
from .simplified_shockwave_samples_data import SimplifiedShockwaveSamplesData
from .simplified_wave_data import SimplifiedWaveData
from .specification_motor import SpecificationMotor
from .specifications import Specifications
from .stock_level import StockLevel
from .storage_position import StoragePosition
from .summary import Summary
from .supply_abc_classification import SupplyAbcClassification
from .supply_category_inventory_item import SupplyCategoryInventoryItem
from .supply_code_request import SupplyCodeRequest
from .supply_file_conversion import SupplyFileConversion
from .supply_file_request import SupplyFileRequest
from .supply_item_related_asset_request import SupplyItemRelatedAssetRequest
from .supply_item_storage_inbound_batch_request import (
    SupplyItemStorageInboundBatchRequest,
)
from .supply_item_storage_position_request import SupplyItemStoragePositionRequest
from .supply_item_storage_request import SupplyItemStorageRequest
from .supply_stock_valuation_method import SupplyStockValuationMethod
from .supply_xyz_classification import SupplyXyzClassification
from .template_request_motor import TemplateRequestMotor
from .template_request_motor_asset_failures import TemplateRequestMotorAssetFailures
from .template_request_motor_attachment import TemplateRequestMotorAttachment
from .text_custom_field import TextCustomField
from .time_spent_cost import TimeSpentCost
from .total_cost import TotalCost
from .update_events_tractian_request import UpdateEventsTractianRequest
from .update_insight_status_tractian_request import UpdateInsightStatusTractianRequest
from .update_inspection_procedure_tractian_request import (
    UpdateInspectionProcedureTractianRequest,
)
from .update_inspection_status_tractian_request import (
    UpdateInspectionStatusTractianRequest,
)
from .validation_error import ValidationError
from .work_order_asset_motor import WorkOrderAssetMotor
from .work_order_completed_by_user import WorkOrderCompletedByUser
from .work_order_deleted_info import WorkOrderDeletedInfo
from .work_order_file_value_motor import WorkOrderFileValueMotor
from .work_order_location_motor import WorkOrderLocationMotor
from .work_order_motor_attachment import WorkOrderMotorAttachment
from .work_order_operation_asset_motor import WorkOrderOperationAssetMotor
from .work_order_operation_inventory import WorkOrderOperationInventory
from .work_order_operation_inventory_inventory import (
    WorkOrderOperationInventoryInventory,
)
from .work_order_operation_inventory_selected_batch import (
    WorkOrderOperationInventorySelectedBatch,
)
from .work_order_operation_motor import WorkOrderOperationMotor
from .work_order_operations import WorkOrderOperations
from .work_order_operations_procedure import WorkOrderOperationsProcedure
from .work_order_operations_procedure_fields import WorkOrderOperationsProcedureFields
from .work_order_procedure_alternative_value_motor import (
    WorkOrderProcedureAlternativeValueMotor,
)
from .work_order_procedure_empty_value_motor import WorkOrderProcedureEmptyValueMotor
from .work_order_procedure_fields import WorkOrderProcedureFields
from .work_order_procedure_value_motor import WorkOrderProcedureValueMotor
from .work_order_procedures import WorkOrderProcedures
from .work_order_signature_value_motor import WorkOrderSignatureValueMotor
from .work_order_timers import WorkOrderTimers
from .work_orders_elapsed_intervals_motor import WorkOrdersElapsedIntervalsMotor
from .work_orders_motor import WorkOrdersMotor
from .work_orders_motor_request_api import WorkOrdersMotorRequestAPI
from .work_orders_others_costs_motor import WorkOrdersOthersCostsMotor
from .work_orders_others_costs_motor_request_api import (
    WorkOrdersOthersCostsMotorRequestAPI,
)
from .workorder_operation_procedure import WorkorderOperationProcedure
from .yes_no_custom import YesNoCustom
from .yes_or_no_custom import YesOrNoCustom

__all__ = (
    "ActivityAlternativeValueMotor",
    "ActivityProcedureFieldOption",
    "ActivityProcedureValue",
    "AddAssetMotor",
    "AddAssetMotorAttachment",
    "AddAssetMotorAttachmentFileConvertion",
    "ApiSupplyInventoryAdjustmentRequest",
    "ApiSupplyInventoryPatchRequest",
    "ApiSupplyItemCategory",
    "ApiSupplyItemCategoryRequest",
    "ApiSupplyItemStorageResponse",
    "Asset",
    "AssetAttachmentMotor",
    "AssetComponentsMotor",
    "AssetCriticalityMotor",
    "AssetImageMotor",
    "AssetInventoryItemMotor",
    "AssetLocationMotor",
    "AssetUserMotor",
    "AxisData",
    "Balance",
    "Batch",
    "BearingMotor",
    "BearingMotorFaultFrequenciesType0",
    "BooleanCustomField",
    "CategoryOtherCosts",
    "Checklist",
    "CheckListCustomField",
    "Code",
    "CodeType",
    "CommentsMotor",
    "ComponentsMotor",
    "ConsumptionSamplesWithoutTariffStation",
    "ConsumptionSamplesWithTariffStation",
    "CostSamplesWithoutTariffStation",
    "CostSamplesWithTariffStation",
    "CurrencyCustomField",
    "CurrentReviewCycleMotor",
    "DateCustomField",
    "Deleted",
    "DeletedInfo",
    "DemandSamplesWithoutTariffStation",
    "DemandSamplesWithTariffStation",
    "Disabled",
    "DisabledInfo",
    "EntityCustomField",
    "EntityCustomFieldValueType10",
    "EntityCustomFieldValueType5Item",
    "EntityCustomFieldValueType6",
    "EntityCustomFieldValueType7Item",
    "EntityCustomFieldValueType8",
    "EntityCustomFieldValueType9",
    "EventCerberus",
    "EventType",
    "FeedbackRequestsMotor",
    "FeedbackRequestUserMotor",
    "FieldsMotor",
    "FileMotor",
    "FixStatus",
    "GeneratedWorkorder",
    "GlobalUnitsSamples",
    "Heading",
    "HTTPValidationError",
    "IdentifiedAssetFailures",
    "InboundBatch",
    "InsightCerberus",
    "InsightStatus",
    "InspectionCustom",
    "InspectionList",
    "InspectionMotor",
    "InspectionStatus",
    "InventoryAdjustmentPositionSupplyRequest",
    "InventoryAdjustmentsInboundBatchSupplyRequest",
    "InventoryAdjustmentTypeEnum",
    "InventoryItemsCost",
    "InventoryMongoDB",
    "InventoryMongoDBAsset",
    "InventoryMongoDBAssetAssetType0",
    "InventoryMotorRequestAPI",
    "InventoryMotorRequestBatchAPI",
    "InventoryMotorRequestDisabledAPI",
    "InventoryMotorRestockBatchesRequestAPI",
    "InventoryMotorRestockRequestAPI",
    "InventoryRestockAPI",
    "InventoryRestockBatchesAPI",
    "ItemCategoryTypeEnum",
    "ItemReservationMotor",
    "ItemReservationMotorDelete",
    "ItemReservationMotorSelectedBatch",
    "ItemReservationRequestAPI",
    "ItemReservationRequestSelectedBatchesAPI",
    "ItemReservationUpdateAPI",
    "LevelMotor",
    "Location",
    "MaterialType",
    "MeasurementUnit",
    "Metrics",
    "MetricsFieldValues",
    "NewInboundBatchSupplyRequest",
    "NumberCustomField",
    "OtherCost",
    "PaginationApiSupplyItemCategoryResponse",
    "PaginationApiSupplyItemStorageResponse",
    "PaginationDTOAssetMotor",
    "PaginationEventCerberus",
    "PaginationInsightCerberus",
    "PaginationItemReservationMotor",
    "PaginationRequestsMotor",
    "PaginationWorkOrderOperationMotor",
    "PaginationWorkOrdersMotor",
    "PaginationWorkOrdersOthersCostsMotor",
    "ParentInfoRequestMotor",
    "ParentInfoRequestMotorOptionType0",
    "ParentWorkOrderOperationProcedureFields",
    "ParentWorkOrderOperationProcedureFieldsLevels",
    "ParentWorkOrderOperationProcedureRequestMotor",
    "PhaseValues",
    "ProcedureMotor",
    "PurchaseOrders",
    "Request",
    "RequestsMotor",
    "RequestsTemplate",
    "RequestsTemplateCategory",
    "RequestsTemplateIdentifiedAssetFailures",
    "RequestTemplateCategoriesMotor",
    "SelectionListCustomField",
    "SimplifiedRpmSampleData",
    "SimplifiedShockwaveSamplesData",
    "SimplifiedWaveData",
    "SpecificationMotor",
    "Specifications",
    "StockLevel",
    "StoragePosition",
    "Summary",
    "SupplyAbcClassification",
    "SupplyCategoryInventoryItem",
    "SupplyCodeRequest",
    "SupplyFileConversion",
    "SupplyFileRequest",
    "SupplyItemRelatedAssetRequest",
    "SupplyItemStorageInboundBatchRequest",
    "SupplyItemStoragePositionRequest",
    "SupplyItemStorageRequest",
    "SupplyStockValuationMethod",
    "SupplyXyzClassification",
    "TemplateRequestMotor",
    "TemplateRequestMotorAssetFailures",
    "TemplateRequestMotorAttachment",
    "TextCustomField",
    "TimeSpentCost",
    "TotalCost",
    "UpdateEventsTractianRequest",
    "UpdateInsightStatusTractianRequest",
    "UpdateInspectionProcedureTractianRequest",
    "UpdateInspectionStatusTractianRequest",
    "ValidationError",
    "WorkOrderAssetMotor",
    "WorkOrderCompletedByUser",
    "WorkOrderDeletedInfo",
    "WorkOrderFileValueMotor",
    "WorkOrderLocationMotor",
    "WorkOrderMotorAttachment",
    "WorkOrderOperationAssetMotor",
    "WorkOrderOperationInventory",
    "WorkOrderOperationInventoryInventory",
    "WorkOrderOperationInventorySelectedBatch",
    "WorkOrderOperationMotor",
    "WorkorderOperationProcedure",
    "WorkOrderOperations",
    "WorkOrderOperationsProcedure",
    "WorkOrderOperationsProcedureFields",
    "WorkOrderProcedureAlternativeValueMotor",
    "WorkOrderProcedureEmptyValueMotor",
    "WorkOrderProcedureFields",
    "WorkOrderProcedures",
    "WorkOrderProcedureValueMotor",
    "WorkOrdersElapsedIntervalsMotor",
    "WorkOrderSignatureValueMotor",
    "WorkOrdersMotor",
    "WorkOrdersMotorRequestAPI",
    "WorkOrdersOthersCostsMotor",
    "WorkOrdersOthersCostsMotorRequestAPI",
    "WorkOrderTimers",
    "YesNoCustom",
    "YesOrNoCustom",
)

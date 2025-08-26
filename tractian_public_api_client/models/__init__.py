"""Contains all the data models used in inputs/outputs"""

from .activity_alternative_value_motor import ActivityAlternativeValueMotor
from .add_asset_motor import AddAssetMotor
from .add_asset_motor_attachment import AddAssetMotorAttachment
from .add_asset_motor_attachment_file_convertion import (
    AddAssetMotorAttachmentFileConvertion,
)
from .add_purchase_requisition_supply_request import AddPurchaseRequisitionSupplyRequest
from .add_transfer_request_supply_request import AddTransferRequestSupplyRequest
from .api_category_motor_response import ApiCategoryMotorResponse
from .api_consumption_samples_with_tariff_station_response import (
    ApiConsumptionSamplesWithTariffStationResponse,
)
from .api_consumption_samples_without_tariff_station_response import (
    ApiConsumptionSamplesWithoutTariffStationResponse,
)
from .api_cost_samples_with_tariff_station_response import (
    ApiCostSamplesWithTariffStationResponse,
)
from .api_cost_samples_without_tariff_station_response import (
    ApiCostSamplesWithoutTariffStationResponse,
)
from .api_demand_samples_without_tariff_station_response import (
    ApiDemandSamplesWithoutTariffStationResponse,
)
from .api_disabled_location import ApiDisabledLocation
from .api_global_units_samples_response import ApiGlobalUnitsSamplesResponse
from .api_list_insights_response import ApiListInsightsResponse
from .api_list_inspections_fields import ApiListInspectionsFields
from .api_list_inspections_level import ApiListInspectionsLevel
from .api_list_inspections_option import ApiListInspectionsOption
from .api_list_inspections_procedure import ApiListInspectionsProcedure
from .api_list_inspections_response import ApiListInspectionsResponse
from .api_locations import ApiLocations
from .api_locations_put_request import ApiLocationsPutRequest
from .api_locations_request import ApiLocationsRequest
from .api_locations_request_deleted import ApiLocationsRequestDeleted
from .api_metric_value import ApiMetricValue
from .api_metric_value_motor import ApiMetricValueMotor
from .api_metric_value_request import ApiMetricValueRequest
from .api_metrics_motor_request import ApiMetricsMotorRequest
from .api_reliability_event_insight_response import ApiReliabilityEventInsightResponse
from .api_reliability_event_response import ApiReliabilityEventResponse
from .api_rpm_samples_response import ApiRpmSamplesResponse
from .api_supply_attachment import ApiSupplyAttachment
from .api_supply_deleted import ApiSupplyDeleted
from .api_supply_inventory_adjustment_request import ApiSupplyInventoryAdjustmentRequest
from .api_supply_inventory_patch_request import ApiSupplyInventoryPatchRequest
from .api_supply_item_category import ApiSupplyItemCategory
from .api_supply_item_category_request import ApiSupplyItemCategoryRequest
from .api_supply_item_reservation_request import ApiSupplyItemReservationRequest
from .api_supply_item_reservation_response import ApiSupplyItemReservationResponse
from .api_supply_item_storage_inbound_batch import ApiSupplyItemStorageInboundBatch
from .api_supply_measurement_unit_patch_request import (
    ApiSupplyMeasurementUnitPatchRequest,
)
from .api_supply_measurement_unit_put_request import ApiSupplyMeasurementUnitPutRequest
from .api_supply_measurement_unit_request import ApiSupplyMeasurementUnitRequest
from .api_supply_new_contract import ApiSupplyNewContract
from .api_supply_other_costs import ApiSupplyOtherCosts
from .api_supply_purchase_order import ApiSupplyPurchaseOrder
from .api_supply_purchase_order_item import ApiSupplyPurchaseOrderItem
from .api_supply_purchase_order_request import ApiSupplyPurchaseOrderRequest
from .api_supply_purchase_order_status import ApiSupplyPurchaseOrderStatus
from .api_supply_purchase_request_action import ApiSupplyPurchaseRequestAction
from .api_supply_purchase_requisition_item import ApiSupplyPurchaseRequisitionItem
from .api_supply_purchase_requisition_item_request import (
    ApiSupplyPurchaseRequisitionItemRequest,
)
from .api_supply_purchase_requisition_put_request import (
    ApiSupplyPurchaseRequisitionPutRequest,
)
from .api_supply_purchase_requisition_request import ApiSupplyPurchaseRequisitionRequest
from .api_supply_purchase_requisition_response import (
    ApiSupplyPurchaseRequisitionResponse,
)
from .api_supply_reject_purchase_request_action import (
    ApiSupplyRejectPurchaseRequestAction,
)
from .api_supply_reservation_patch_request import ApiSupplyReservationPatchRequest
from .api_supply_reservation_put_request import ApiSupplyReservationPutRequest
from .api_supply_reservation_request import ApiSupplyReservationRequest
from .api_supply_storage_location_code_response import (
    ApiSupplyStorageLocationCodeResponse,
)
from .api_supply_storage_location_deleted import ApiSupplyStorageLocationDeleted
from .api_supply_storage_location_disabled import ApiSupplyStorageLocationDisabled
from .api_supply_storage_location_response import ApiSupplyStorageLocationResponse
from .api_supply_supplier_address_coordinates import ApiSupplySupplierAddressCoordinates
from .api_supply_supplier_attachment import ApiSupplySupplierAttachment
from .api_supply_supplier_contract import ApiSupplySupplierContract
from .api_supply_supplier_deleted import ApiSupplySupplierDeleted
from .api_supply_supplier_image import ApiSupplySupplierImage
from .api_supply_transfer_request_item_status import ApiSupplyTransferRequestItemStatus
from .api_supply_transfer_requests_put_request import (
    ApiSupplyTransferRequestsPutRequest,
)
from .api_supply_transfer_requests_request import ApiSupplyTransferRequestsRequest
from .api_supply_work_order_item import ApiSupplyWorkOrderItem
from .api_user_deleted import ApiUserDeleted
from .api_user_request import ApiUserRequest
from .api_user_team import ApiUserTeam
from .api_vibration_samples_response import ApiVibrationSamplesResponse
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
from .bonsai_asset_tree import BonsaiAssetTree
from .bonsai_child import BonsaiChild
from .bonsai_parent import BonsaiParent
from .bonsai_value import BonsaiValue
from .boolean_custom_field import BooleanCustomField
from .category_other_costs import CategoryOtherCosts
from .check_list_custom_field import CheckListCustomField
from .code import Code
from .code_type import CodeType
from .comments_motor import CommentsMotor
from .components_motor import ComponentsMotor
from .cost_center import CostCenter
from .criticality_values_response import CriticalityValuesResponse
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
from .event_type import EventType
from .feedback_request_user_motor import FeedbackRequestUserMotor
from .feedback_requests_motor import FeedbackRequestsMotor
from .file_motor import FileMotor
from .fix_status import FixStatus
from .frequency_model import FrequencyModel
from .frequency_model_request import FrequencyModelRequest
from .frequency_type import FrequencyType
from .generated_workorder import GeneratedWorkorder
from .head_values_response import HeadValuesResponse
from .http_validation_error import HTTPValidationError
from .identified_asset_failures import IdentifiedAssetFailures
from .inbound_batch import InboundBatch
from .insight_event_response import InsightEventResponse
from .insight_status import InsightStatus
from .inspection_motor import InspectionMotor
from .inspection_procedure_empty_value_motor import InspectionProcedureEmptyValueMotor
from .inspection_procedure_field_alternative_value_motor import (
    InspectionProcedureFieldAlternativeValueMotor,
)
from .inspection_procedure_field_motor import InspectionProcedureFieldMotor
from .inspection_procedure_motor import InspectionProcedureMotor
from .inspection_procedure_option_value import InspectionProcedureOptionValue
from .inspection_procedure_value_motor import InspectionProcedureValueMotor
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
from .item_reservation_status_enum import ItemReservationStatusEnum
from .item_reservation_update_api import ItemReservationUpdateAPI
from .last_read_metric_motor import LastReadMetricMotor
from .level_motor import LevelMotor
from .load_insights_info_by_id_insights_insight_id_get_language import (
    LoadInsightsInfoByIdInsightsInsightIdGetLanguage,
)
from .load_insights_info_by_id_insights_insight_id_get_layout_type import (
    LoadInsightsInfoByIdInsightsInsightIdGetLayoutType,
)
from .load_requests_by_company_id_companies_company_id_requests_get_filter_type_0 import (
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0,
)
from .load_requests_by_company_id_companies_company_id_requests_get_load_custom_fields_type_0 import (
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
)
from .location import Location
from .material_type import MaterialType
from .measurement_unit import MeasurementUnit
from .metrics_field_values import MetricsFieldValues
from .metrics_field_values_motor import MetricsFieldValuesMotor
from .new_inbound_batch_supply_request import NewInboundBatchSupplyRequest
from .number_custom_field import NumberCustomField
from .offline_metric import OfflineMetric
from .online_metric import OnlineMetric
from .option import Option
from .other_cost import OtherCost
from .pagination_api_category_motor_response import PaginationApiCategoryMotorResponse
from .pagination_api_list_insights_response import PaginationApiListInsightsResponse
from .pagination_api_reliability_event_response import (
    PaginationApiReliabilityEventResponse,
)
from .pagination_api_supply_item_category_response import (
    PaginationApiSupplyItemCategoryResponse,
)
from .pagination_api_supply_purchase_order import PaginationApiSupplyPurchaseOrder
from .pagination_api_supply_purchase_requisition_response import (
    PaginationApiSupplyPurchaseRequisitionResponse,
)
from .pagination_api_supply_storage_location_response import (
    PaginationApiSupplyStorageLocationResponse,
)
from .pagination_dto_asset_motor import PaginationDTOAssetMotor
from .pagination_item_reservation_motor import PaginationItemReservationMotor
from .pagination_requests_motor import PaginationRequestsMotor
from .pagination_work_order_operation_motor import PaginationWorkOrderOperationMotor
from .pagination_work_order_priorities_motor_response_api import (
    PaginationWorkOrderPrioritiesMotorResponseAPI,
)
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
from .priority_motor import PriorityMotor
from .priority_motor_deleted import PriorityMotorDeleted
from .priority_motor_disabled import PriorityMotorDisabled
from .purchase_orders import PurchaseOrders
from .purchase_requisition_priority import PurchaseRequisitionPriority
from .purchase_requisition_supply_priority import PurchaseRequisitionSupplyPriority
from .purchase_requisition_supply_status import PurchaseRequisitionSupplyStatus
from .request import Request
from .request_template_categories_motor import RequestTemplateCategoriesMotor
from .requests_motor import RequestsMotor
from .requests_template import RequestsTemplate
from .requests_template_category import RequestsTemplateCategory
from .requests_template_identified_asset_failures import (
    RequestsTemplateIdentifiedAssetFailures,
)
from .selection_list_custom_field import SelectionListCustomField
from .sensor_metric import SensorMetric
from .simplified_prescription import SimplifiedPrescription
from .specification_motor import SpecificationMotor
from .specifications import Specifications
from .stock_level import StockLevel
from .storage_position import StoragePosition
from .summary import Summary
from .supplier import Supplier
from .supplier_address import SupplierAddress
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
from .transfer_request import TransferRequest
from .transfer_request_item import TransferRequestItem
from .update_events_tractian_request import UpdateEventsTractianRequest
from .update_insight_status_tractian_request import UpdateInsightStatusTractianRequest
from .update_inspection_procedure_tractian_request import (
    UpdateInspectionProcedureTractianRequest,
)
from .update_inspection_status_tractian_request import (
    UpdateInspectionStatusTractianRequest,
)
from .update_purchase_requisition_supply_request import (
    UpdatePurchaseRequisitionSupplyRequest,
)
from .user import User
from .validation_error import ValidationError
from .values_response import ValuesResponse
from .wave_data import WaveData
from .withdrawn_batch import WithdrawnBatch
from .withdrawn_position import WithdrawnPosition
from .work_order_asset_motor import WorkOrderAssetMotor
from .work_order_assigned_teams import WorkOrderAssignedTeams
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
from .work_order_operation_inventory_reservation import (
    WorkOrderOperationInventoryReservation,
)
from .work_order_operation_inventory_selected_batch import (
    WorkOrderOperationInventorySelectedBatch,
)
from .work_order_operation_motor import WorkOrderOperationMotor
from .work_order_operation_procedure_empty_value_motor import (
    WorkOrderOperationProcedureEmptyValueMotor,
)
from .work_order_operation_procedure_field_option import (
    WorkOrderOperationProcedureFieldOption,
)
from .work_order_operation_procedure_value import WorkOrderOperationProcedureValue
from .work_order_operations import WorkOrderOperations
from .work_order_operations_procedure import WorkOrderOperationsProcedure
from .work_order_operations_procedure_fields import WorkOrderOperationsProcedureFields
from .work_order_priorities_motor_response_api import (
    WorkOrderPrioritiesMotorResponseAPI,
)
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
from .workorder_operation_procedure_field import WorkorderOperationProcedureField

__all__ = (
    "ActivityAlternativeValueMotor",
    "AddAssetMotor",
    "AddAssetMotorAttachment",
    "AddAssetMotorAttachmentFileConvertion",
    "AddPurchaseRequisitionSupplyRequest",
    "AddTransferRequestSupplyRequest",
    "ApiCategoryMotorResponse",
    "ApiConsumptionSamplesWithoutTariffStationResponse",
    "ApiConsumptionSamplesWithTariffStationResponse",
    "ApiCostSamplesWithoutTariffStationResponse",
    "ApiCostSamplesWithTariffStationResponse",
    "ApiDemandSamplesWithoutTariffStationResponse",
    "ApiDisabledLocation",
    "ApiGlobalUnitsSamplesResponse",
    "ApiListInsightsResponse",
    "ApiListInspectionsFields",
    "ApiListInspectionsLevel",
    "ApiListInspectionsOption",
    "ApiListInspectionsProcedure",
    "ApiListInspectionsResponse",
    "ApiLocations",
    "ApiLocationsPutRequest",
    "ApiLocationsRequest",
    "ApiLocationsRequestDeleted",
    "ApiMetricsMotorRequest",
    "ApiMetricValue",
    "ApiMetricValueMotor",
    "ApiMetricValueRequest",
    "ApiReliabilityEventInsightResponse",
    "ApiReliabilityEventResponse",
    "ApiRpmSamplesResponse",
    "ApiSupplyAttachment",
    "ApiSupplyDeleted",
    "ApiSupplyInventoryAdjustmentRequest",
    "ApiSupplyInventoryPatchRequest",
    "ApiSupplyItemCategory",
    "ApiSupplyItemCategoryRequest",
    "ApiSupplyItemReservationRequest",
    "ApiSupplyItemReservationResponse",
    "ApiSupplyItemStorageInboundBatch",
    "ApiSupplyMeasurementUnitPatchRequest",
    "ApiSupplyMeasurementUnitPutRequest",
    "ApiSupplyMeasurementUnitRequest",
    "ApiSupplyNewContract",
    "ApiSupplyOtherCosts",
    "ApiSupplyPurchaseOrder",
    "ApiSupplyPurchaseOrderItem",
    "ApiSupplyPurchaseOrderRequest",
    "ApiSupplyPurchaseOrderStatus",
    "ApiSupplyPurchaseRequestAction",
    "ApiSupplyPurchaseRequisitionItem",
    "ApiSupplyPurchaseRequisitionItemRequest",
    "ApiSupplyPurchaseRequisitionPutRequest",
    "ApiSupplyPurchaseRequisitionRequest",
    "ApiSupplyPurchaseRequisitionResponse",
    "ApiSupplyRejectPurchaseRequestAction",
    "ApiSupplyReservationPatchRequest",
    "ApiSupplyReservationPutRequest",
    "ApiSupplyReservationRequest",
    "ApiSupplyStorageLocationCodeResponse",
    "ApiSupplyStorageLocationDeleted",
    "ApiSupplyStorageLocationDisabled",
    "ApiSupplyStorageLocationResponse",
    "ApiSupplySupplierAddressCoordinates",
    "ApiSupplySupplierAttachment",
    "ApiSupplySupplierContract",
    "ApiSupplySupplierDeleted",
    "ApiSupplySupplierImage",
    "ApiSupplyTransferRequestItemStatus",
    "ApiSupplyTransferRequestsPutRequest",
    "ApiSupplyTransferRequestsRequest",
    "ApiSupplyWorkOrderItem",
    "ApiUserDeleted",
    "ApiUserRequest",
    "ApiUserTeam",
    "ApiVibrationSamplesResponse",
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
    "BonsaiAssetTree",
    "BonsaiChild",
    "BonsaiParent",
    "BonsaiValue",
    "BooleanCustomField",
    "CategoryOtherCosts",
    "CheckListCustomField",
    "Code",
    "CodeType",
    "CommentsMotor",
    "ComponentsMotor",
    "CostCenter",
    "CriticalityValuesResponse",
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
    "EventType",
    "FeedbackRequestsMotor",
    "FeedbackRequestUserMotor",
    "FileMotor",
    "FixStatus",
    "FrequencyModel",
    "FrequencyModelRequest",
    "FrequencyType",
    "GeneratedWorkorder",
    "HeadValuesResponse",
    "HTTPValidationError",
    "IdentifiedAssetFailures",
    "InboundBatch",
    "InsightEventResponse",
    "InsightStatus",
    "InspectionMotor",
    "InspectionProcedureEmptyValueMotor",
    "InspectionProcedureFieldAlternativeValueMotor",
    "InspectionProcedureFieldMotor",
    "InspectionProcedureMotor",
    "InspectionProcedureOptionValue",
    "InspectionProcedureValueMotor",
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
    "ItemReservationStatusEnum",
    "ItemReservationUpdateAPI",
    "LastReadMetricMotor",
    "LevelMotor",
    "LoadInsightsInfoByIdInsightsInsightIdGetLanguage",
    "LoadInsightsInfoByIdInsightsInsightIdGetLayoutType",
    "LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0",
    "LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0",
    "Location",
    "MaterialType",
    "MeasurementUnit",
    "MetricsFieldValues",
    "MetricsFieldValuesMotor",
    "NewInboundBatchSupplyRequest",
    "NumberCustomField",
    "OfflineMetric",
    "OnlineMetric",
    "Option",
    "OtherCost",
    "PaginationApiCategoryMotorResponse",
    "PaginationApiListInsightsResponse",
    "PaginationApiReliabilityEventResponse",
    "PaginationApiSupplyItemCategoryResponse",
    "PaginationApiSupplyPurchaseOrder",
    "PaginationApiSupplyPurchaseRequisitionResponse",
    "PaginationApiSupplyStorageLocationResponse",
    "PaginationDTOAssetMotor",
    "PaginationItemReservationMotor",
    "PaginationRequestsMotor",
    "PaginationWorkOrderOperationMotor",
    "PaginationWorkOrderPrioritiesMotorResponseAPI",
    "PaginationWorkOrdersMotor",
    "PaginationWorkOrdersOthersCostsMotor",
    "ParentInfoRequestMotor",
    "ParentInfoRequestMotorOptionType0",
    "ParentWorkOrderOperationProcedureFields",
    "ParentWorkOrderOperationProcedureFieldsLevels",
    "ParentWorkOrderOperationProcedureRequestMotor",
    "PhaseValues",
    "PriorityMotor",
    "PriorityMotorDeleted",
    "PriorityMotorDisabled",
    "PurchaseOrders",
    "PurchaseRequisitionPriority",
    "PurchaseRequisitionSupplyPriority",
    "PurchaseRequisitionSupplyStatus",
    "Request",
    "RequestsMotor",
    "RequestsTemplate",
    "RequestsTemplateCategory",
    "RequestsTemplateIdentifiedAssetFailures",
    "RequestTemplateCategoriesMotor",
    "SelectionListCustomField",
    "SensorMetric",
    "SimplifiedPrescription",
    "SpecificationMotor",
    "Specifications",
    "StockLevel",
    "StoragePosition",
    "Summary",
    "Supplier",
    "SupplierAddress",
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
    "TransferRequest",
    "TransferRequestItem",
    "UpdateEventsTractianRequest",
    "UpdateInsightStatusTractianRequest",
    "UpdateInspectionProcedureTractianRequest",
    "UpdateInspectionStatusTractianRequest",
    "UpdatePurchaseRequisitionSupplyRequest",
    "User",
    "ValidationError",
    "ValuesResponse",
    "WaveData",
    "WithdrawnBatch",
    "WithdrawnPosition",
    "WorkOrderAssetMotor",
    "WorkOrderAssignedTeams",
    "WorkOrderCompletedByUser",
    "WorkOrderDeletedInfo",
    "WorkOrderFileValueMotor",
    "WorkOrderLocationMotor",
    "WorkOrderMotorAttachment",
    "WorkOrderOperationAssetMotor",
    "WorkOrderOperationInventory",
    "WorkOrderOperationInventoryInventory",
    "WorkOrderOperationInventoryReservation",
    "WorkOrderOperationInventorySelectedBatch",
    "WorkOrderOperationMotor",
    "WorkorderOperationProcedure",
    "WorkOrderOperationProcedureEmptyValueMotor",
    "WorkorderOperationProcedureField",
    "WorkOrderOperationProcedureFieldOption",
    "WorkOrderOperationProcedureValue",
    "WorkOrderOperations",
    "WorkOrderOperationsProcedure",
    "WorkOrderOperationsProcedureFields",
    "WorkOrderPrioritiesMotorResponseAPI",
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
)

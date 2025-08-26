from typing import Literal, cast

LoadInsightsInfoByIdInsightsInsightIdGetLayoutType = Literal["mobile", "web"]

LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LAYOUT_TYPE_VALUES: set[
    LoadInsightsInfoByIdInsightsInsightIdGetLayoutType
] = {
    "mobile",
    "web",
}


def check_load_insights_info_by_id_insights_insight_id_get_layout_type(
    value: str,
) -> LoadInsightsInfoByIdInsightsInsightIdGetLayoutType:
    if value in LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LAYOUT_TYPE_VALUES:
        return cast(LoadInsightsInfoByIdInsightsInsightIdGetLayoutType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LAYOUT_TYPE_VALUES!r}"
    )

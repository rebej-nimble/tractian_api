from typing import Literal, cast

LoadInsightsInfoByIdInsightsInsightIdGetLanguage = Literal["en", "es", "pt"]

LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LANGUAGE_VALUES: set[
    LoadInsightsInfoByIdInsightsInsightIdGetLanguage
] = {
    "en",
    "es",
    "pt",
}


def check_load_insights_info_by_id_insights_insight_id_get_language(
    value: str,
) -> LoadInsightsInfoByIdInsightsInsightIdGetLanguage:
    if value in LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LANGUAGE_VALUES:
        return cast(LoadInsightsInfoByIdInsightsInsightIdGetLanguage, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOAD_INSIGHTS_INFO_BY_ID_INSIGHTS_INSIGHT_ID_GET_LANGUAGE_VALUES!r}"
    )

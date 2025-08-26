from typing import Literal, cast

LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0 = Literal[
    "false", "true"
]

LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_LOAD_CUSTOM_FIELDS_TYPE_0_VALUES: set[
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0
] = {
    "false",
    "true",
}


def check_load_requests_by_company_id_companies_company_id_requests_get_load_custom_fields_type_0(
    value: str,
) -> LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0:
    if (
        value
        in LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_LOAD_CUSTOM_FIELDS_TYPE_0_VALUES
    ):
        return cast(
            LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetLoadCustomFieldsType0,
            value,
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_LOAD_CUSTOM_FIELDS_TYPE_0_VALUES!r}"
    )

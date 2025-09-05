from typing import Literal, cast

LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0 = Literal[
    "createdAt", "updatedAt"
]

LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_FILTER_TYPE_0_VALUES: set[
    LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0
] = {
    "createdAt",
    "updatedAt",
}


def check_load_requests_by_company_id_companies_company_id_requests_get_filter_type_0(
    value: str,
) -> LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0:
    if (
        value
        in LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_FILTER_TYPE_0_VALUES
    ):
        return cast(
            LoadRequestsByCompanyIdCompaniesCompanyIdRequestsGetFilterType0, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOAD_REQUESTS_BY_COMPANY_ID_COMPANIES_COMPANY_ID_REQUESTS_GET_FILTER_TYPE_0_VALUES!r}"
    )

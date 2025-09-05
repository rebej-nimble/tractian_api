from typing import Literal, cast

LoadWorkorderByCompanyIdCompaniesCompanyIdWorkordersGetFilterType0 = Literal[
    "createdAt", "updatedAt"
]

LOAD_WORKORDER_BY_COMPANY_ID_COMPANIES_COMPANY_ID_WORKORDERS_GET_FILTER_TYPE_0_VALUES: (
    set[LoadWorkorderByCompanyIdCompaniesCompanyIdWorkordersGetFilterType0]
) = {
    "createdAt",
    "updatedAt",
}


def check_load_workorder_by_company_id_companies_company_id_workorders_get_filter_type_0(
    value: str,
) -> LoadWorkorderByCompanyIdCompaniesCompanyIdWorkordersGetFilterType0:
    if (
        value
        in LOAD_WORKORDER_BY_COMPANY_ID_COMPANIES_COMPANY_ID_WORKORDERS_GET_FILTER_TYPE_0_VALUES
    ):
        return cast(
            LoadWorkorderByCompanyIdCompaniesCompanyIdWorkordersGetFilterType0, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOAD_WORKORDER_BY_COMPANY_ID_COMPANIES_COMPANY_ID_WORKORDERS_GET_FILTER_TYPE_0_VALUES!r}"
    )

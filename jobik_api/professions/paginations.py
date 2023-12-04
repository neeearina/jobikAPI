import rest_framework.pagination as pagination

__all__ = ["ProfessionsPagination"]


class ProfessionsPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
    max_page_size = 50

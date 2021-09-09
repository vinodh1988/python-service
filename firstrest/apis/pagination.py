from rest_framework.pagination import PageNumberPagination,CursorPagination

class ProductSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param='pageno'
    max_page_size = 10000

class CursorPagination(CursorPagination):
    page_size = 5
    ordering= 'productid'
from rest_framework.exceptions import APIException


class CategoryServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Category service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

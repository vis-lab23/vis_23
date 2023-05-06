from rest_framework.exceptions import APIException


class CategoryServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'category service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

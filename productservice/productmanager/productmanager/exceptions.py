from rest_framework import status
from rest_framework.exceptions import APIException


class CategoryServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "category service temporarily unavailable, try again later."
    default_code = "service_unavailable"


class CategoryIDMissing(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "category id is missing"

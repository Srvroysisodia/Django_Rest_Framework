from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffSetPagination(LimitOffsetPagination):
    
    default_limit = 15
    max_limit = 20
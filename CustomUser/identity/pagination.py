'''
This file contains the code to provide pagination to the entire API
'''
#importing the libraries
from rest_framework.pagination import LimitOffsetPagination

#Creating Pagination Class
class CustomLimitOffsetPagination(LimitOffsetPagination):
    '''
    Defining the page number for each of the pages
    
    '''
    default_limit = 15
    max_limit = 20
    

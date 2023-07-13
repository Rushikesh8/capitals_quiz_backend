from rest_framework import status as http_status
from rest_framework.response import Response

def api_success_response(response_data,status=http_status.HTTP_200_OK):
    return Response(({"success":True,"data":response_data}),status=status)


def api_error_response(error_message,status=http_status.HTTP_400_BAD_REQUEST):
    return Response(({"success":False,"data":error_message}),status=status)
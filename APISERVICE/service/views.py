"""
service/views.py
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_service_version(request):
    """
    return the api-service version

    :param request: argument.
    :type request: object

    :rtype: json
    :return: api-service version. "V1"
    """
    if request.method == "GET":
        return Response({"data": request.version})

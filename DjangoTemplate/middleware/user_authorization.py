from django.utils.deprecation import MiddlewareMixin
import logging
from ..utils import get_user_session
from django.http import HttpResponse, JsonResponse
import os
from ..settings import DEBUG

unauthorized_response = JsonResponse({"error": "Unauthorized", "details": "You do not have permission "
                                                                          "to access this resource"}, status=401)

class UserAuthorization:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        is_authorized = self.process_request(request)
        if not is_authorized:
            user_name = request.session.get('user_details', {}).get("username","")
            logging_message = f'{request.get_full_path()}: {user_name} do not have permission to access this resource'
            logging.warning(logging_message)
            return unauthorized_response
        # Call the next middleware or view
        return self.get_response(request)

    def process_request(self, request):
        try:
            user_details = request.session.get('user_details', None)

            if not user_details:
                get_user_session(request, is_debug=DEBUG)
                user_details = request.session.get('user_details', None)
                """
                add your authorization use case logic using user data
                """

        except Exception as e:
            logging.error(e, exc_info=True, stack_info=True)

        if user_details:
            return True

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        # This method is called when an exception occurs in the view
        logging.error(exception)
        return None

from devcycle_python_sdk.models.user import DevCycleUser
from .devcycle import get_devcycle_client

def devcycle_middleware(get_response):
    """
    This middleware adds the DevCycle client to the request object passed to
    all views as `request.devcycle`.
    """
    def middleware(request):
        # all client functions require user data to be an instance of the DevCycleUser class
        request.user = DevCycleUser(
            user_id='user123',
            email='jane.doe@example.ca',
            country='CA'
        )
        request.devcycle = get_devcycle_client()
        return get_response(request)

    return middleware

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from devcycle_python_sdk import (
    DevCycleLocalClient,
    DevCycleLocalOptions,
)

try:
    devcycle_sdk_key = settings.DEVCYCLE_SERVER_SDK_KEY
except AttributeError:
    raise ImproperlyConfigured("Please set DEVCYCLE_SERVER_SDK_KEY in .env")

# Create an options object to do custom configurations, or use the defaults
options = DevCycleLocalOptions()

# Initialize the SDK singleton once here - it will be captured in the closure below
devcycle_client = DevCycleLocalClient(devcycle_sdk_key, options)

def get_devcycle_client():
    return devcycle_client
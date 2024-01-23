import sys
import time
import threading
from devcycle_python_sdk.models.user import DevCycleUser
from .devcycle import get_devcycle_client

"""
Since this is used outside of a request context, we define a service user.
This can contian properties unique to this service, and allows you to target
services in the same way you would target app users.
"""
SERVICE_USER = DevCycleUser(
    user_id='api-service'
)

"""
Log the current DevCycle variation to the console.
"""
def log_variation():
    devcycle_client = get_devcycle_client()

    def render_frame(idx=0):
        timeout = 500

        if devcycle_client.is_initialized():
            features = devcycle_client.all_features(SERVICE_USER)
            variation_name = features['hello-togglebot'].variationName if 'hello-togglebot' in features else 'Default'

            wink = devcycle_client.variable_value(SERVICE_USER, 'togglebot-wink', False)
            speed = devcycle_client.variable_value(SERVICE_USER, 'togglebot-speed', 'off')

            spin_chars = "◟◜◝◞" if speed == 'slow' else "◜◠◝◞◡◟"
            spinner = '○' if speed == 'off' else spin_chars[idx]
            idx = (idx + 1) % len(spin_chars)

            face = '(- ‿ ○)' if wink else '(○ ‿ ○)'

            frame = '{} Serving variation: {} {}'.format(spinner, variation_name, face)
            color = 'rainbow' if speed == 'surprise' else 'blue'

            write_to_console(frame, color)

            timeout = 100 if speed in ['fast', 'surprise', 'off-axis'] else 500

        # Set timeout to render next frame
        threading.Timer(
            timeout / 1000,
            lambda: render_frame(idx)
        ).start()

    try:
        render_frame()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.exit(0)

COLORS = {}
COLORS['red'] = '\033[91m'
COLORS['green'] = '\033[92m'
COLORS['yellow'] = '\033[93m'
COLORS['blue'] = '\033[94m'
COLORS['magenta'] = '\033[95m'
END_CHAR = '\033[0m'

def add_color(text, color):
    colors = {}
    colors.update(COLORS)
    colors['rainbow'] = '\033[38;5;{}m'.format(int(time.time() * 1000) % 230)

    if color in colors:
        return colors[color] + text + END_CHAR
    else:
        return text

def write_to_console(frame, color):
    frame = add_color(frame, color)
    sys.stdout.write('\r\x1b[K' + frame)
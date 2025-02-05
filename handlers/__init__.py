from .common_handlers import register_common_handlers
from .echo_handlers import register_echo_handlers
from .weather_handlers import register_weather_handlers

def register_handlers(dp):
    register_common_handlers(dp)
    register_weather_handlers(dp)
    register_echo_handlers(dp)
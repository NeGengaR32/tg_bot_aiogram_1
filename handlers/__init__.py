from .common_handlers import register_common_handlers
from .echo_handlers import register_echo_handlers

def register_handlers(dp):
    register_common_handlers(dp)
    register_echo_handlers(dp)
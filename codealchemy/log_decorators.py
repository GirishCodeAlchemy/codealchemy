# girishcodealchemy/decorators.py

import logging
import time
from functools import wraps

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)

# Initialize a global indent level
indent_level = 0
indent_prefixes = ['']  # Root level has no prefix

class TreeFormatter(logging.Formatter):
    def format(self, record):
        global indent_level
        # Determine the appropriate prefix for the current log level
        prefix = indent_prefixes[indent_level] if indent_level < len(indent_prefixes) else ''
        # Format the log message with level, file name, line number, timestamp, and the message
        formatted_message = super().format(record)
        return f"{prefix}{formatted_message}"

# Add a custom formatter to the root logger
logger = logging.getLogger()
formatter = TreeFormatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def log_group(group_name):
    """
    Decorator to create log groups for a function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global indent_level
            # Update the indentation prefixes for the current level
            indent_prefixes.append('│   ' * indent_level + '├── ')
            logging.info(f"Entering log group: {group_name}")
            indent_level += 1  # Increase indentation level
            try:
                result = func(*args, **kwargs)
            finally:
                indent_level -= 1  # Decrease indentation level
                indent_prefixes.pop()  # Remove the current level prefix
                logging.info(f"Exiting log group: {group_name}")
            return result
        return wrapper
    return decorator

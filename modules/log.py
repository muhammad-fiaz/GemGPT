# Import Logly
import os

from logly import Logly

logly = Logly()

# Set the default file path and maximum file size
logly.set_default_max_file_size(50)
logger = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../log.txt")
logly.set_default_file_path(logger)


logly.start_logging()
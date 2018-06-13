from logging import getLogger, basicConfig, StreamHandler, FileHandler, INFO
from sys import stdout
LOG_FILE = 'bot.log'

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO)
log = getLogger(__name__)

# stdout_handler = StreamHandler(stream=stdout)
log_handler = FileHandler(LOG_FILE)

# log.addHandler(stdout_handler)
log.addHandler(log_handler)

# We're done! Import common logger from any other module

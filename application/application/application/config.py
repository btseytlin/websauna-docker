"""application config."""
from prettyconf import config  # noQA


# Example environment variable
DUMMY_ENV = config('DUMMY_ENV', default='')

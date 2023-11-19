from logging import getLogger, Formatter, StreamHandler

logger = getLogger(__name__)
__format = Formatter(
    "(%(asctime)s) %(levelname)s: %(pathname)s:%(lineno)d - %(message)s"
)

__handler = StreamHandler()
__handler.setFormatter(__format)
logger.addHandler(__handler)
logger.setLevel("INFO")

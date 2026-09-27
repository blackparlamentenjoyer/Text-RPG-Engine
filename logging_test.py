import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S", filename="game.log")
logging.debug("Debug info")
logging.info("Info info")
logging.warning("Warning info")
logging.error("Error info")
logging.critical("Critical error info")
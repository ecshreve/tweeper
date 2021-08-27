from helpers import get_random_quote
from config import create_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    api = create_api()

    qq = None
    while qq is None or len(qq[1]) > 140:
        qq = get_random_quote()

    try:
        api.update_status(qq[1])
    except Exception as e:
        logger.error("Error updating status", exc_info=True)
        raise e

    logger.info("status updated successfully")


if __name__ == "__main__":
    main()

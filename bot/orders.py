from .client import get_client
from .logging_config import logger
from binance.exceptions import BinanceAPIException


def place_market_order(symbol, side, quantity):

    client = get_client()

    request_data = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    }

    logger.info(f"REQUEST: {request_data}")

    try:

        response = client.futures_create_order(**request_data)

        logger.info(f"RESPONSE: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"BINANCE API ERROR: {str(e)}")
        raise

    except Exception as e:

        logger.error(f"NETWORK / UNKNOWN ERROR: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):

    client = get_client()

    request_data = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    }

    logger.info(f"REQUEST: {request_data}")

    try:

        response = client.futures_create_order(**request_data)

        logger.info(f"RESPONSE: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"BINANCE API ERROR: {str(e)}")
        raise

    except Exception as e:

        logger.error(f"NETWORK / UNKNOWN ERROR: {str(e)}")
        raise
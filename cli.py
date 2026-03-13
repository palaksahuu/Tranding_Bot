import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import *


def main():

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price)

        print("\n========== ORDER REQUEST ==========")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)
        print("Price:", args.price)

        if args.type == "MARKET":

            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            if args.price is None:
                raise ValueError("LIMIT order requires price")

            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\n========== ORDER RESPONSE ==========")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\nSUCCESS: Order placed successfully")

    except Exception as e:

        print("\nFAILED:", str(e))


if __name__ == "__main__":
    main()
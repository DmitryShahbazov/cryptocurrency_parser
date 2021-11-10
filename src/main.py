import asyncio

from src import engine
from src.helpers import get_currency, group_by_name, parse_json


def main():
    sources = parse_json()
    for source in sources:
        asyncio.run(engine.main(source))
    res = engine.result
    cryptocurrency_pairs_with_source = group_by_name(res)
    pairs = ['BTC_XRP', 'BTC_ETH', 'USDT_ETH', 'BTC_BCH', 'BTC_ZEC']
    group_by_pair_ask, group_by_pair_bid = dict(), dict()

    # Собираем новый словарь для удобства
    for k, v in cryptocurrency_pairs_with_source.items():
        group_by_pair_ask[k] = v['ask']
        group_by_pair_bid[k] = v['bid']

    get_currency(group_by_pair_ask, 'Ask', pairs)

    print('='*50)

    get_currency(group_by_pair_bid, 'Bid', pairs)


if __name__ == '__main__':
    main()

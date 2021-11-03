import asyncio


from src.exmo import Exmo
from src.helpers import get_currency, group_by_name
from src.kraken import Kraken
from src.poloniex import Poloniex


def main():
    pairs = ['BTC_XRP', 'BTC_ETH', 'USDT_ETH', 'BTC_BCH', 'BTC_ZEC']
    cryptocurrency_pairs_with_source, group_by_pair_ask, group_by_pair_bid = dict(), dict(), dict()
    poloniex = Poloniex()
    asyncio.run(poloniex.main())
    res = group_by_name(poloniex.result)
    cryptocurrency_pairs_with_source['poloniex'] = res

    exmo = Exmo()
    asyncio.run(exmo.main())
    res = group_by_name(exmo.result)
    cryptocurrency_pairs_with_source['exmo'] = res

    kraken = Kraken()
    asyncio.run(kraken.main())
    res = group_by_name(kraken.result)
    cryptocurrency_pairs_with_source['kraken'] = res

    # Собираем новый словарь для удобства
    for k, v in cryptocurrency_pairs_with_source.items():
        for k1, v1 in v.items():
            group_by_pair_ask[f'{k}/{k1}'] = v1['ask']
            group_by_pair_bid[f'{k}/{k1}'] = v1['bid']

    get_currency(group_by_pair_ask, 'Ask', pairs)

    print('='*50)

    get_currency(group_by_pair_bid, 'Bid', pairs)


if __name__ == '__main__':
    main()
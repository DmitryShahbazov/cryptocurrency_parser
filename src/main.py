import asyncio
import operator

from src.exmo import Exmo
from src.kraken import Kraken
from src.poloniex import Poloniex
from src.helpers import group_by_name


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

    # Проходимся по словарю и выводим значения Ask
    for pair in pairs:
        for k, v in sorted(group_by_pair_ask.items(), key=operator.itemgetter(1), reverse=True):
            if pair in k:
                source_pair = k.split('/')
                source = source_pair[0]
                pair = source_pair[1]
                print(f'Source: {source} Pair: {pair} Ask price: {v}')

    print('='*50)

    # Проходимся по словарю и выводим значения Bid
    for pair in pairs:
        for k, v in sorted(group_by_pair_bid.items(), key=operator.itemgetter(1), reverse=True):
            if pair in k:
                source_pair = k.split('/')
                source = source_pair[0]
                pair = source_pair[1]
                print(f'Source: {source} Pair: {pair} Bid price: {v}')


if __name__ == '__main__':
    main()
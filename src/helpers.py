import operator


def group_by_name(cryptocurrency: dict) -> dict:
    """
    Функция для приведения к одинаковым названиям пар
    :param cryptocurrency: Словарь с разными названиями пар
    :return:Словарь с одноименными парами
    """

    result = {}
    for k, v in cryptocurrency.items():
        if k in ('BTC_XRP', 'XRP_BTC', 'XXRPXXBT'):
            result['BTC_XRP'] = v
        elif k in ('BTC_ETH', 'ETH_BTC', 'XETHXXBT'):
            result['BTC_ETH'] = v
        elif k in ('USDT_ETH', 'ETH_USDT', 'ETHUSDT'):
            result['USDT_ETH'] = v
        elif k in ('BTC_BCH', 'BCH_BTC', 'BCHXBT'):
            result['BTC_BCH'] = v
        elif k in ('BTC_ZEC', 'ZEC_BTC', 'XZECXXBT'):
            result['BTC_ZEC'] = v

    return result


def get_currency(currency_group: dict, key: str, pairs: list):
    for pair in pairs:
        for k, v in sorted(currency_group.items(), key=operator.itemgetter(1), reverse=True):
            if pair in k:
                source_pair = k.split('/')
                source = source_pair[0]
                pair = source_pair[1]
                print(f'Source: {source} Pair: {pair} {key} price: {v}')

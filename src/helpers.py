import json
import operator


def group_by_name(cryptocurrency: dict) -> dict:
    """
    Функция для приведения к одинаковым названиям пар
    :param cryptocurrency: Словарь с разными названиями пар
    :return:Словарь с одноименными парами
    """
    result = {}
    for k, v in cryptocurrency.items():
        pair = k.split('/')[1]
        if pair in ('BTC_XRP', 'XRP_BTC', 'XXRPXXBT'):
            new_key = k.replace(pair, 'BTC_XRP')
            result[new_key] = v
        elif pair in ('BTC_ETH', 'ETH_BTC', 'XETHXXBT'):
            new_key = k.replace(pair, 'BTC_ETH')
            result[new_key] = v
        elif pair in ('USDT_ETH', 'ETH_USDT', 'ETHUSDT'):
            new_key = k.replace(pair, 'USDT_ETH')
            result[new_key] = v
        elif pair in ('BTC_BCH', 'BCH_BTC', 'BCHXBT'):
            new_key = k.replace(pair, 'BTC_BCH')
            result[new_key] = v
        elif pair in ('BTC_ZEC', 'ZEC_BTC', 'XZECXXBT'):
            new_key = k.replace(pair, 'BTC_ZEC')
            result[new_key] = v

    return result


def get_currency(currency_group: dict, key: str, pairs: list):
    for pair in pairs:
        for k, v in sorted(currency_group.items(), key=operator.itemgetter(1)):
            if pair in k:
                source_pair = k.split('/')
                source = source_pair[0]
                pair = source_pair[1]
                print(f'Source: {source} Pair: {pair} {key} price: {v}')


def parse_json() -> dict:
    path = 'sources.json'
    with open(path, 'r') as file:
        data = json.loads(file.read())

        return data

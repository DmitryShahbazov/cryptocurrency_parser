import asyncio

import aiohttp

result = {}


def parse_response(response: dict, source: dict):
    if source['many_urls']:
        for k, v in response['result'].items():
            result[f'{source["name"]}/{k}'] = {'ask': v[source['ask']][0], 'bid': v[source['bid']][0]}
    else:
        for k, v in response.items():
            if k in source['pairs']:
                result[f'{source["name"]}/{k}'] = {'ask': v[source['ask']], 'bid': v[source['bid']]}


async def fetch(client, pair: str, source: dict):
    url = source['url'].replace('PAIR_MACROS', pair)
    async with client.get(url) as resp:
        response = await resp.json()
        parse_response(response, source)


async def main(source: dict):
    async with aiohttp.ClientSession() as client:
        # Если нужно будет посылать несколько урлов, то делаем gather
        if source['many_urls']:
            await asyncio.gather(*[
                fetch(client, pair, source)
                for pair in source['pairs']
            ])
        else:
            async with client.get(source['url']) as resp:
                response = await resp.json()
                parse_response(response, source)

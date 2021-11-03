import aiohttp
import asyncio


class Kraken:
    def __init__(self):
        self.pairs = ['ETHBTC', 'ETHUSDT', 'XRPBTC', 'BCHBTC', 'ZECBTC']
        self.result = {}

    def parse_response(self, response: dict):
        for k, v in response['result'].items():
            self.result[k] = {'ask': v['a'][0], 'bid': v['b'][0]}

    async def fetch(self, client, item):
        url = f'https://api.kraken.com/0/public/Ticker?pair={item}'
        async with client.get(url) as resp:
            response = await resp.json()
            self.parse_response(response)

    async def main(self):
        async with aiohttp.ClientSession() as client:
            await asyncio.gather(*[
                self.fetch(client, item)
                for item in self.pairs
            ])

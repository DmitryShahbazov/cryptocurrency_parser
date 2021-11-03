import aiohttp


class Poloniex:
    def __init__(self):
        self.result = {}

    def parse_response(self, response: dict):
        for k, v in response.items():
            if k in ('BTC_ETH', 'USDT_ETH', 'BTC_XRP', 'BTC_BCH', 'BTC_ZEC'):
                self.result[k] = {'ask': v['lowestAsk'], 'bid': v['highestBid']}

    async def main(self):
        async with aiohttp.ClientSession() as session:
            poloniex_url = 'https://poloniex.com/public?command=returnTicker'
            async with session.get(poloniex_url) as resp:
                response = await resp.json()
                self.parse_response(response)

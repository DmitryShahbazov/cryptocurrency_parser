import aiohttp


class Exmo:
    def __init__(self):
        self.result = {}

    def parse_response(self, response: dict):
        for k, v in response.items():
            if k in ('ETH_BTC', 'ETH_USDT', 'XRP_BTC', 'BCH_BTC', 'ZEC_BTC'):
                self.result[k] = {'ask': v['buy_price'], 'bid': v['sell_price']}

    async def main(self):
        async with aiohttp.ClientSession() as session:
            exmo_url = 'https://api.exmo.com/v1.1/ticker'
            async with session.get(exmo_url) as resp:
                response = await resp.json()
                self.parse_response(response)

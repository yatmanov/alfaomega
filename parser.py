import asyncio
import argparse
import csv
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs

import aiohttp
import lxml.html

URL = 'https://alfaomega.tv/canal-tv/programul-tv'


async def main(file):

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            resp.raise_for_status()
            html = await resp.text()

    dom = lxml.html.fromstring(html)

    day_value = dom.xpath('.//option[@selected]/@value')[0]
    query = parse_qs(urlparse(day_value).query)
    current_day = datetime.strptime(query['zi'][0], '%Y-%m-%d')

    data = []
    for i, el in enumerate(dom.xpath('.//div[starts-with(@id, "dialog_")]')):

        _time = el.get('id').lstrip('dialog_')
        _date = current_day + timedelta(hours=int(_time[:2]), minutes=int(_time[2:]))
        datetime_start = _date.isoformat()

        if i > 0:
            data[i-1]['datetime_finish'] = datetime_start

        data.append({
            'datetime_start': datetime_start,
            'datetime_finish': None,
            'channel': el.xpath('./h2/span/text()')[0],
            'title': el.xpath('./h2/text()')[0],
            'channel_logo_url': el.xpath('./img/@src')[0],
            'description': el.xpath('./p/text()')[0],
        })

    with open(file, mode='w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=str)
    args = parser.parse_args()

    asyncio.run(main(args.output))

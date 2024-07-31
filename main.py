from src.controller.main_controller import process_data

import asyncio 

async def main():
    urls = [
        'https://www.visionofhumanity.org/maps/#/',
        'https://www.visionofhumanity.org/maps/global-terrorism-index/#/',
        'https://www.visionofhumanity.org/maps/ecological-threat-report/#/',
        'https://www.visionofhumanity.org/maps/mexico-peace-index/#/',
        'https://www.visionofhumanity.org/maps/positive-peace-index/#/',
        'https://www.visionofhumanity.org/maps/us-peace-index/#/',
        'https://www.visionofhumanity.org/maps/uk-peace-index/#/'
    ]
    # await asyncio.gather(*(process_data(url) for url in urls))
    for url in urls:
        await process_data(url)

asyncio.run(main())
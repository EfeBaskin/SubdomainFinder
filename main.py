import asyncio
import aiohttp
import time

target_input = "google.com"

async def get_data(session, url):
    async with session.get(url) as resp:
        return resp

async def faster_url(url):

    try:
        async with aiohttp.ClientSession() as session:
            response = await get_data(session, url)
            if response.status == 200:
                print(f"{url} exists")
    except aiohttp.client_exceptions.ClientConnectorError as e:
        print(f"Error connecting to {url}: {e}")


async def main():
    urls = []
    with open("Subdomainlist.txt.txt", "r") as subdomainList:
        for word in subdomainList:
            word = word.strip()
            url = "http://" + word + "." + target_input
            urls.append(url)

    tasks = [asyncio.create_task(faster_url(url)) for url in urls]
    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")  #runtime : 2 seconds
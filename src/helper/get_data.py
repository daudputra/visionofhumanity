import os
import requests
import asyncio
import time

from playwright.async_api import async_playwright
from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from src.exception.exception import PageRequestError


class GetData:

    @staticmethod
    async def detect_csv_requests(url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            csv_urls = []

            def handle_request(request):
                if request.url.endswith('.csv'):
                    # print(f"CSV request detected: {request.url}")
                    csv_urls.append(request.url)


            try:
                page.on("request", handle_request)
                await page.goto(url)
                await page.wait_for_timeout(6000)

            except PlaywrightTimeoutError:
                await page.reload()
                await page.wait_for_timeout(60000)
            except PageRequestError as e:
                await e.send_message()
            except Exception as e:
                raise PageRequestError(f"An unexpected error occurred: {e}")

            
                
            

            finally:
                await browser.close()

            return csv_urls

            # try:

            #     page.on("request", handle_request)
            #     await page.goto(url)
            #     await page.wait_for_timeout(6000)

            # except TimeoutError:
            #     await page.reload()
            #     page.on("request", handle_request)
            #     await page.wait_for_timeout(60000)
            # except Exception as e:
            #     raise PageRequestError(f"Error: {e}")

            # await browser.close()
            # return csv_urls

    @staticmethod   
    async def save_csv(url):
        category = url.split('/')[-1].split('_')[0]

        if 'GTI' in url and 'MPI' in url:
            tahun = url.split('/')[-1].split('_')[1]
        elif 'PPI' in url:
            tahun = url.split('/')[-1].split('_')[2]
        elif 'GPI' in url:
            tahun = url.split('/')[-1].split('_')[-1].split('.')[0].split('-')[0]
        else:
            tahun = url.split('/')[-1].split('_')[1].split('.')[0]

        if category == 'GPI':
            category = 'Global Peace Index'
        elif category == 'GTI':
            category = 'Global Terrorism Index'
        elif category == 'ETR':
            category = 'Ecological Threat Report'
        elif category == 'MPI':
            category = 'Mexico Peace Index'
        elif category == 'PPI':
            category = 'Positive Peace Index'
        elif category == 'USPI':
            category = 'US Peace Index'
        elif category == 'UKPI':
            category = 'UK Peace Index'

        category = category.replace(" ", "_").lower()

        csv_dir = f'csv/{category}/{tahun}'

        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        filename = url.split('/')[-1]
        file_path = os.path.join(csv_dir, filename)

        # response = requests.get(url)
        # with open(file_path, 'wb') as file:
        #     file.write(response.content)

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, GetData.download_csv, url, file_path)

        return tahun, category, filename
    

    @staticmethod
    def download_csv(url, file_path):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'application/csv'
        }

        max_retries = 10
        attempt = 0

        while attempt < max_retries:
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Memeriksa status kode respons
                
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                
                if os.path.getsize(file_path) == 0:
                    print("File kosong, mencoba lagi...")
                    attempt += 1
                    continue
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if '<html>' in content:
                        print("File berisi HTML, mencoba lagi...")
                        attempt += 1
                        continue
                
                print("File CSV berhasil diunduh.")
                break

            except requests.RequestException as e:
                print(f"Terjadi kesalahan saat mengunduh file: {e}")
                attempt += 1
                # Menunggu sejenak sebelum mencoba lagi
                time.sleep(5)
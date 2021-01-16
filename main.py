from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
app = FastAPI()


@app.post("/open-sessions")
async def root(web : str):
    reqs = requests.get(web)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = [];
    for link in soup.find_all('a'):
        urls.append(link.get('href'))

    return {"URLs": urls}
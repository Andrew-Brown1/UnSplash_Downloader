import requests 
from bs4 import BeautifulSoup
import lxml

def photo_download(url):
    requests = requests.get(url, allow_redirects=True)
	data = BeautifulSoup(request.content,'lxml')


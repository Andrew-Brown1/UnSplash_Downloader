import requests
from bs4 import BeautifulSoup
import os
import lxml
from tqdm import tqdm

output_path = '/Users/andrewbrown/images'

def photo_downloader(url, out_dir):
    request = requests.get(url,allow_redirects = True)
    data = BeautifulSoup(request.text,'lxml')
    all_image=data.find_all('figure',itemprop="image")
    count =0
    for i in tqdm(all_image):
        url=i.find('a',rel="nofollow")
        if url != None:
            i_url = url['href']
            photo_bytes = requests.get(i_url,allow_redirects=True)
            with open(os.path.join(out_dir,f'{count}3d.jpg'),'wb') as photo:
                photo.write(photo_bytes.content)
                count +=1

    print("Done")



if __name__ == "__main__":

    url_name = "https://unsplash.com/s/photos/3d"
    dir_name = url_name.split('/')[-1]
    if not os.path.isdir(os.path.join(output_path,dir_name)):
        os.mkdir(os.path.join(output_path,dir_name))

    photo_downloader(url_name, os.path.join(output_path,dir_name))
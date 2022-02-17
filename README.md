# UnSplash_Downloader
UnSplash is a website with lots of cool images, with a liscence meaning that anyone can use the images

This repo has some very simple code for downloading images from UnSplash using Python

This did not require as much code as I thought it would... But useful none the less

All credit to this medium post: https://medium.com/analytics-vidhya/%EF%B8%8F-do-some-automate-work-with-python-a4c5d50da79c


Further notes. For downloading from UnSplash, BeautifulSoup only gets the first page of images. The only way around I got (because UnSplash only has one continuous page where you "scroll down" to get new images - BeautifulSoup only gets the first ~60 images) was to use the "Save Page As" on FireFox which actually downloads every image on the page after you have scrolled down many times.

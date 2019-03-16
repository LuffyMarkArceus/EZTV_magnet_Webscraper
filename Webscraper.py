import requests
import os
import time
from pprint import pprint
def call_eztv():
        url_base = 'https://eztv.io/search/'
        search_str = input("Enter the show name to search : ")
        total_results = int(input("TOTAL NO. OF results"))
        timer_sleeper = int(input("Delay between every search"))
        uploader = 'x265-MiNX'
        print("---------------------------------------------------Torrent Web Scrapper Program---------------------------------------------------")

        url_base += search_str
        r = requests.get(url_base)


        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.content,'html.parser')
        torrent_url = []
        file_name = []

        for link in soup.find_all('a','magnet'):
                if len(torrent_url) < total_results:
                        torrent_url.append(link.get('href'))
                        file_name.append(link.get('title'))             #for now only need to be removed in future.

        torrent_zipper = zip(torrent_url,file_name)
        for t_url,t_name in torrent_zipper:
                if uploader in t_name:
                        os.startfile(t_url)
                        time.sleep(timer_sleeper)
        
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print(*torrent_url,sep='\n\n')
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print(*file_name,sep='\n')
        print("----------------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
        call_eztv()
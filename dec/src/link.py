from pytube import YouTube
from googlesearch import search
import sys

query = "het shah youtube"

for i in search(query, tld="co.in", num=1, stop=1, pause=2):
    print(i)
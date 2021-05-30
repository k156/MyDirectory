import requests
from bs4 import BeautifulSoup
import json
import re
from pprint import pprint
from time import sleep
from /home/file import header
headers = {'User-Agent': '{header}'}
def likes(self):
    url= "https://www.melon.com/commonlike/getSongLike.json?contsIds={}".format(self)
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, features="html.parser")
    res = soup.text
    plikes = re.findall('SUMMCNT":(.*)}]', res)[0]
    return plikes
singerdict = {}
la = re.compile(".*소속사.*")
# la = re.compile("<dt>소속사</dt>")
def get_info(self, title): #?title제거
    url= "https://www.melon.com/artist/timeline.htm?artistId={}".format(self)
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, features="html.parser")
    info = soup.select("div.wrap_atist_info")
    for i in info:
        singerdict["aid"] = self
        if soup.find(class_ = "gubun") != None:
            singerdict["debut"] = soup.find(class_ = "gubun").text
        else:
            singerdict["debut"] = 'N/A'
        etc = soup.find(class_ = "atist_info clfix")
        dts = etc.find_all("dt")
        for dt in dts:
            if len(la.findall(str(dt))) > 0:
                j = la.findall(str(dt))
                # print(j)
                singerdict["label"] = dt.next_sibling.next_sibling.text
                # print( singerdict)
                break
            else:
                singerdict["label"] = 'N/A'
                pass
        return singerdict
        # print(singerdict, title) #?title 제거
        # etc = soup.find_all("dd")
        # for e in etc:
        #     print(e.text)
# aid는 다음 aid 리스트의 숫자만큼 반복된다.
# 데뷔일, 타이틀은 정상 순서
# 소속사는 
#aid는 중복, label은 있는 경우만 반환
i = 1
url='https://www.melon.com/chart/index.htm'
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content, features="html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
# fnd = re.compile('goAlbumDetail\(\'(.*)\'\)')
fnd = re.compile("goAlbumDetail\(['](.*)[']\)")
# dic = {}
p = re.compile("goArtistDetail\([']([0-9]*)")
for i, tr in enumerate(trs):
    song_no = tr.attrs['data-song-no']
    rank = i
    i += 1
    title = tr.find(class_ = 'ellipsis rank01').text.strip('\n')
    artists = tr.find_all(class_ = 'ellipsis rank02')
    album = tr.find(class_ = 'ellipsis rank03').text.strip('\n')
    albumId = tr.find(class_ = 'ellipsis rank03').a.attrs['href']
    # AlbumId = str(albumId)
    albumID = fnd.findall(albumId)[0]
    likecnt = likes(song_no)
    alist = []
    lst = []
    idlist = []
    artistinfo = []
    for st in artists:
        iddouble = p.findall(str(st))
        idlist = iddouble[:len(iddouble)-len(iddouble)//2]
        # print(idlist)
        s = st.text.strip('\n')
        char = int(len(s)/2)
        alist.append(s[:char])
        for ids in idlist:
            info = get_info(ids, title = title) #?title제거
            artistinfo.append(info)
        # print(ids)
        # print(info)
        # print(artistinfo)C
    for name in alist:
        lst.append(name.split(','))
    # print(artistinfo)
        print([song_no, title, idlist, artistinfo, lst[0], album, albumID, likecnt])
        # return [song_no, title, idlist, lst[0], album, albumID, likecnt], artistinfo
    # print(dic)
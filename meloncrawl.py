import requests
from bs4 import BeautifulSoup
import json
import re
from pprint import pprint
from time import sleep


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}


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
        #####################
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
################################333
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
        aidlist = set(iddouble)
        # idlist = iddouble[:len(iddouble)-len(iddouble)//2]
        # # print(idlist)
        s = st.text.strip('\n')
        char = int(len(s)/2)
        alist.append(s[:char])
        # print(alist)
        for aid in aidlist:
            print(aid)
            info = get_info(aid, title = title) #?title제거
            artistinfo.append(info)
        
    # for ids in idlist:
    #     info = get_info(ids, title = title) #?title제거
    #     artistinfo.append(info)
        # print(ids)
        # print(info)
        # print(artistinfo)
    for name in alist:
        lst.append(name.split(','))
    # print(artistinfo)
        # print([song_no, title, artistinfo, lst[0], album, albumID, likecnt])
        # return [song_no, title, idlist, lst[0], album, albumID, likecnt], artistinfo
    # print(dic)

# [song_no, title, artistname, artistname, artid, artid, album, albumid, likecnt]
# [아이유, 261143], [브레이브걸스, 531700] [{name: 정은지, Id :510565}, {name: 양요섭, Id : 644871 } ] {정은지: 510565, 양요섭: 644871}
#  [[정은지, 510565], [양요섭, 644871 ] ]
 # dic[len(lst[0])] = m
# s= st.text.split(',') => [['양요섭', '정은지']]
# a.append(s[:char]) =>[['양요섭']]
# a.append(st.text.strip('\n').split(',')) => [['양요섭, '정은지양요섭', '정은지']]

        # etc = soup.find(class_ = "atist_info clfix")
        # birth = etc.dd.text
        # for e in etc:
        #     birth = e.dd.text
        # #     # label =
        #     print(birth)

# print(artists)

# print(soup.prettify)

# results1 = soup.find_all('div', class_ = 'ellipsis rank01')

# for result in results1:
#     print(result)

# results2 = soup.find_all('div', class_ = 'ellipsis rank02')

# for result in results2:
#     print(result)

# results3 = soup.find_all('div', class_ = 'ellipsis rank03')

# for result in results3:
#     print(result)

        # result = re.findall('\'goSongDetail(.*)\'', l)
       
    # print(lst2)

    # for l in lst:    
        # lst2.append(re.search("\'goSongDetail(.*)\'"),l)
        # print(re.search("\'goSongDetail(.*)\'"),l)

    # pprint(lst) 

# get_song_no()

# likeurl = "https://www.melon.com/commonlike/getSongLike.json?contsIds=33244575"
# req = requests.get(url=likeurl, headers =headers)
# soupl = BeautifulSoup(req.content, features="html.parser")
# resl = soupl.text
# # summcnt = plikes(resl)
# print(plikes)

# print(r.text)
########################################################33


# songlst = []

# lst = []
# lst2 = []

# def get_song_no():
#     url='https://www.melon.com/chart/index.htm'
#     r = requests.get(url=url, headers=headers)
#     soup = BeautifulSoup(r.content, features="html.parser")
#     res = soup.tbody
#     # for songDetail in res.find_all(href=re.compile("goSongDetail")):
#     #     print(songDetail.string)

#     # songDetail = res.find_all(href=re.compile("goSongDetail"))
#     # sd = str(songDetail)
#     # print(re.search("\'goSongDetail(.*)\'"),sd)
    

#     songDetail = res.find_all(href=re.compile("goSongDetail"))

#     for x in songDetail:
#         lst.append(str(x))
#     for l in lst:
#         lst2.append ( re.findall("goSongDetail\(\'(\d*)\'\)", l) )
#     return lst2
# lst3 = []

# def get_likes():
#     get_song_no()   
#     for m in lst2:    
#         lst3.append( m[0].strip("'"))
#     # print(lst3)
#     for n in lst3:
#         likes(n)    
# get_likes()
#########################################################




# def get_likes():
#     # i = 0
#     # ids = "33239419%2C33061995%2C32872978%2C33077590%2C33013877%2C32961718%2C32794652%2C33229299%2C32578498%2C32998018%2C3894276%2C33244575%2C32183386%2C33011180%2C3414749%2C33260801%2C33167063%2C33077234%2C32871975%2C33115807%2C32962258%2C32003395%2C33193809%2C32061975%2C32525311%2C33107649%2C33104090%2C30962526%2C32224272%2C32438894%2C32720013%2C32156286%2C32378104%2C32559782%2C32491274%2C32853712%2C31029291%2C31853557%2C32570501%2C31737197%2C32055419%2C33150997%2C32345931%2C32224166%2C32777869%2C32187544%2C33247490%2C30244931%2C32559781%2C32143487%2C33001672%2C31979846%2C31388145%2C33120545%2C32725013%2C33016659%2C32651098%2C31984204%2C33115804%2C32978341%2C33248758%2C30773554%2C33164083%2C32808616%2C33265859%2C33077591%2C33115806%2C31509376%2C33002813%2C33137384%2C32508053%2C32825454%2C32486613%2C33150993%2C33280399%2C32998020%2C32137576%2C33043504%2C31341518%2C32614125%2C33139117%2C32313543%2C33061829%2C32947184%2C32122539%2C33067476%2C33269643%2C32906021%2C33129712%2C32996210%2C33257245%2C33133804%2C32399830%2C32790516%2C30717645%2C33016550%2C33133799%2C33160574%2C33169122%2C33223396"
#     # lst = ids.split('%2C')
#     for n in lst3:
#         likes(n)
#         # i += 1

# get_likes
# json.loads( get_likes() )




# results4 = soup.find_all('button', class_ = 'button_etc like')

# # results4 = soup.select('tbody > tr')

# # results4 = soup.select('cnt')

# # results4 = soup.find_all('span')


# for rates in results4:
#     print(rates.text)


# //*[@id="frm"]/div/table/tbody/tr[2]/td[6]/div/button/span[2]/text()
# for rates in results4:
#     r = rates.select('none').text
#     print(r)


# tbody = soup.find_parents('#frm > div > table > tbody')
# for tr in tbody:
#     print(tr)


# data = json.loads(results4.text)      
# for rank in data['contsLike']:    
#     print(contsid["CONTSID"], likeyn["LIKEYN"], sumncnt["SUMMCNT"])



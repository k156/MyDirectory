

# i= 1
# sss= []
​
# while i < 2:
#     try:
#         url = "https://openapi.naver.com/v1/search/local.json"
​
#         title = "삼성동 노인정"
#         params = {
#             "query": title,
#             "display": 18,
#             "start": i,
#             "sort": "random"
#         }
​
#         headers = {
#         }
​
#         result = requests.get(url, params=params, headers=headers).text
​
#         jsonData = json.loads(result)
​
#         # print(json.dumps(jsonData, ensure_ascii=False, indent=2))
​
        
#         # p1 = re.compile('서울특별시 강남구 대치동 65-66.*')
#         # p2 = re.compile('서울특별시 강남구 대치동 73-75.*')
#         # p3 = re.compile('서울특별시 강남구 대치동 514.*')    
#         # p4 = re.compile('서울특별시 강남구 대치동 942-988.*')
#         # p5 = re.compile('서울특별시 강남구 대치동 995-1009.*')
​
#         for j in jsonData['items']:
#             category = j['category']
#             title = j["title"]
#             link = j["link"]
#             telephone = j["telephone"]
#             address = j["address"]
#             if '노인정' in category:
#                 # if p1.findall(address) or p2.findall(address) or p3.findall(address) or p4.findall(address) or p5.findall(address):
#                 #     continue
#                 # else:
#                     sss.append([title, category, link, telephone, address])
#     except KeyError:
#         break
​
#     i += 1
​
​
​
# print(jsonData['total'])
# pprint(sss)
​
​
​
​
# with open('realty_daechi.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow( ['상호명' ,'링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
# with open('realty_samsung.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow( ['상호명' ,'링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
# with open('realty_dogok.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow( ['상호명' ,'링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
​
​
# with open('hair_daechi.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow(  ['상호명' ,'분류', '링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
​
# with open('hair_samsung.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow(  ['상호명' ,'분류', '링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
​
# with open('hair_dogok.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow(  ['상호명' ,'분류', '링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
                                
            
​
# with open('senior_samsung.csv', 'w' , newline='', encoding = 'MS949') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
#     spamwriter.writerow(  ['상호명' ,'분류', '링크' ,'전화번호', '주소'] )
#     for i, row in enumerate (sss):
#         spamwriter.writerow(row)
​
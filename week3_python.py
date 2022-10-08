# import urllib.request as request
# import json
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# with request.urlopen(src) as response:
#    data=json.load(response)  #利用json模組處理json資料格式
# glist=data["result"]["results"]
# # with open("data.txt","w",""encoding="utf-8")as file:
# for place in glist:
#     # date1=int(["xpostDate"][0])
#     # print (date1)
#     #if [”xpostDate“]>2015
#     # print(type[xpostDate])

#     print(place["file"])
    # print(place["stitle"]+','+place["longitude"]+','+place["latitude"]+','+place["xpostDate"])
  
    # print(place["stitle"]+','+place["longitude"]+','+place["latitude"]+",",+place["file"]+"\n")
    
 
#  保留   
#    if int(place["xpostDate"][:4]) >= 2015:
#     # print(place['xpostDate'])
#     print(place["stitle"] + ',' + place["longitude"] + ',' +
#           place["latitude"] + ',' + place["xpostDate"])




import urllib.request as request
import json
import csv

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
  data = json.load(response)  #利用json模組處理json資料格式
glist = data["result"]["results"]

def get_first_url(place):

  text = place["file"]
  all_href = text.split('https://')

  return f"https://{all_href[1]}"
  
with open("data.csv","w",encoding="utf-8") as file:

  writer = csv.writer(file)
  # writer.writerow(['景點名稱', '區域', '經度', '緯度', '第一張圖檔網址'])

  for place in glist:
    if int(place["xpostDate"][:4]) >= 2015:
      # print('=================================')
      # print(f'{place["stitle"]}')
      # print(f'區域：{place["address"][5:8]}')
      # print(f'經度：{place["longitude"]}')
      # print(f'緯度：{place["latitude"]}')
      # print(f'第一張圖檔網址：{get_first_url(place)}')

      writer.writerow([f'{place["stitle"]}', 
                       f'{place["address"][5:8]}',
                       f'{place["longitude"]}',
                       f'{place["latitude"]}',
                       f'{get_first_url(place)}'])
  


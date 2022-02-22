
import requests
from bs4 import BeautifulSoup
import re
import json
from statistics import mean

def get_video_src(vid):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }
 
    api_url = 'http://vv.video.qq.com/getinfo?vids=' + vid + '&platform=101001&charge=0&otype=json&defn=shd'
 
    html = requests.get(api_url, headers=headers).text
 
    # 获取json数据
    p = re.compile(r'({.*})', re.S)
    jsonstr = re.findall(p, html)[0]
    json_data = json.loads(jsonstr)
    # print(jsonstr)
 
    # 解析json数据获取url
    baseurl = json_data['vl']['vi'][0]['ul']['ui'][0]['url']
    fn = json_data['vl']['vi'][0]['fn']
    fvkey = json_data['vl']['vi'][0]['fvkey']
 
    real_url = baseurl + fn + '?vkey=' + fvkey
    return real_url
   
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}
url = 'https://v.qq.com/x/search/?q=wwe&stag=0&smartbox_ab='



response=requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
wwe_list=[]
for strong in soup.html.find_all("strong"):
    if 'WWE' in strong.get_text():
        try:
#             print(strong.get_text())
#             print(json_data.keys())
            vid = strong.a['href'].strip('https://v.qq.com/x/page/').strip('.html')
#             print(vid)
            url = get_video_src(vid)
            if not url is None:
                wwe_list.append([strong.get_text(), url])
            
        except :
            pass
#             print(json_data.keys())



with open('mini_dict.json', 'r', encoding='utf-8') as f:
    mini_dict = json.loads(f.read())
import json
with open('all_links.json', 'r', encoding='utf-8') as f:
    all_links = json.loads(f.read())
name_list = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4','CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17', 'CCTV4K','CCTV8K', 'CCTV16', '湖南卫视', '浙江卫视', '江苏卫视', '北京卫视', '东方卫视', '安徽卫视', '广东卫视', '深圳卫视', '辽宁卫视',  '山东卫视', '天津卫视', '重庆卫视', '东南卫视', '甘肃卫视',  '贵州卫视', '河北卫视', '黑龙江卫视', '河南卫视', '湖北卫视', '江西卫视', '吉林卫视',   '四川卫视', '延边卫视' , '金鹰卡通', '风云足球', 'CHC高清电影',  'CHC动作电影',  '风云音乐', '第一剧场', '风云剧场', '世界地理', '怀旧剧场', '兵器科技', '女性时尚', 'CCTV-娱乐', 'CCTV-戏曲', 'CCTV-电影', '高尔夫网球']

txt = '○电视最终版○,#genre#\n'
for name in mini_dict:
    if len(mini_dict[name])==0 or name=='' or not name in name_list:
        mini_dict[name] = []
        continue
    txt = txt.strip('#')
    txt=txt+'\n'+name+','

    for link in mini_dict[name]:        
        txt=txt+link+'$'+str(mean(all_links[link])).split('.')[0]+'#'
print(txt)
with open('tv.txt', 'w') as f:
    f.write(txt)

txt = txt + '\n○WWE○,#genre#\n'
for a in wwe_list:
    name = a[0].replace(' ','-')
    link = a[1]
    txt += f'{name},{link}\n'
print(txt)

with open('tv.txt', 'w') as f:
    f.write(txt)   



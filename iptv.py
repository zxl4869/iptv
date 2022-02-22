import time,json
from statistics import mean

import cv2,time

def test_latensy(link):
    T1 = time.perf_counter()
    cap=cv2.VideoCapture(link)
    ret,frame = cap.read()
    T2 = time.perf_counter()
    latency = ((T2 - T1)*1000)
    cv2.destroyAllWindows()
    cap.release()
    if frame is None:
        return 1500000

    print(latency)
    
    return latency

with open('all_links.json', 'r', encoding='utf-8') as f:
    all_links = json.loads(f.read())
with open('mini_dict.json', 'r', encoding='utf-8') as f:
    mini_dict = json.loads(f.read())
i = 10
name_list = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4','CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17', 'CCTV4K','CCTV8K', 'CCTV16', '湖南卫视', '浙江卫视', '江苏卫视', '北京卫视', '东方卫视', '安徽卫视', '广东卫视', '深圳卫视', '辽宁卫视',  '山东卫视', '天津卫视', '重庆卫视', '东南卫视', '甘肃卫视',  '贵州卫视', '河北卫视', '黑龙江卫视', '河南卫视', '湖北卫视', '江西卫视', '吉林卫视',   '四川卫视', '延边卫视' , '金鹰卡通', '风云足球', 'CHC高清电影',  'CHC动作电影',  '风云音乐', '第一剧场', '风云剧场', '世界地理', '怀旧剧场', '兵器科技', '女性时尚', 'CCTV-娱乐', 'CCTV-戏曲', 'CCTV-电影', '高尔夫网球']

for name in mini_dict:
    for link in mini_dict[name]:
        print('check:'+link+"-"+name+'-',len(mini_dict[name]))
        lat = test_latensy(link)
        if int(lat)>9000:
            mini_dict[name].remove(link)
            all_links[link].append(int(lat))
            all_links[link] = all_links[link][-5:]
            i+=1
            if i > 5:
                with open('all_links.json', 'w') as f:
                    f.write(json.dumps(all_links))
                with open('mini_dict.json', 'w') as f:
                    f.write(json.dumps(mini_dict))
            i = 0
            print(lat)


for name in final_dict:
    for link in final_dict[name]:
        link = link.split('$')[0]
        if name not in mini_dict:
            mini_dict[name] = []
        if len(mini_dict[name])<10:
            if mean(all_links[link])>12000:
                continue
            else :
                i+=1
                if i > 5:
                    with open('all_links.json', 'w') as f:
                        f.write(json.dumps(all_links))
                    with open('mini_dict.json', 'w') as f:
                        f.write(json.dumps(mini_dict))
                    i = 0
                print('check:'+link+"-"+name+'-',len(mini_dict[name]))
               
                lat = test_latensy(link)

                all_links[link].append(int(lat))
                all_links[link] = all_links[link][-5:]
                if mean(all_links[link])<10000:
                    mini_dict[name].append(link)
                    print('添加')
                else:
                    print('失效')
                

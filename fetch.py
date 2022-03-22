# -*- coding: utf-8 -*-
import json
from statistics import mean
with open('all_links.json', 'r', encoding='utf-8') as f:
    all_links = json.loads(f.read())
def add_channel(dict_channels,source_txt):
    ts = source_txt.split('\n')
    for tt in ts:
        if 'genre' in tt:
            continue
        try:
            q = tt.split(',')   
            tittle = q[0]
            for link in q[1].split('#'):
                if not tittle in dict_channels:
                    dict_channels[tittle] = []
                dict_channels[tittle].append(link)
        except:
            continue
    return dict_channels

def m3u_add_channel(dict_channels,source_txt):
    ts = source_txt.split('#EXTINF:')
    for tt in ts:
        if 'genre' in tt:
            continue
        try:
            tittle = tt.split('\n')[0].split(',')[-1]
            link = tt.split('\n')[1]
            if not tittle in dict_channels:
                dict_channels[tittle] = []
            dict_channels[tittle].append(link)
        except:
            continue
    return dict_channels

def render_txt(dict_channels):
    str_txt = ''
    for name in dict_channels :
        str_txt= str_txt + name + ','
        for link in dict_channels[name] :
            str_txt= str_txt + link + '#'
        str_txt= str_txt +  '\n\n'
    return str_txt
import requests
channels = {}

txt_urls = ['https://raw.githubusercontent.com/LiuYi0526/IPTV/master/IPTV.txt',
        'https://raw.githubusercontent.com/zhjan33/zhjan33.github.io/ad8df9550002f79fa6aa465f90777b71915e9f07/tv.txt',
        'https://raw.githubusercontent.com/sun3020/it/b7436e1bbdecf6dc439c462935b6e05b86fab888/tv.txt',
         'https://raw.githubusercontent.com/vbskycn/iptv/8126a694d07ef81fc451aaa360cbb6fdd88fae9d/yyzb/hd.php',
            
        ]
m3u_urls = [
    'https://raw.githubusercontent.com/zfh424/iptv/main/All.m3u8',
        ]
for txt_url in txt_urls:
    result = requests.get(txt_url)
    channels = add_channel(channels,result.text)
          
for m3u_url in m3u_urls:
    result = requests.get(m3u_url)
    channels = m3u_add_channel(channels,result.text)
name_list = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4','CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17', 'CCTV4K','CCTV8K', 'CCTV16', '湖南卫视', '浙江卫视', '江苏卫视', '北京卫视', '东方卫视', '安徽卫视', '广东卫视', '深圳卫视', '辽宁卫视',  '山东卫视', '天津卫视', '重庆卫视', '东南卫视', '甘肃卫视',  '贵州卫视', '河北卫视', '黑龙江卫视', '河南卫视', '湖北卫视', '江西卫视', '吉林卫视',   '四川卫视', '延边卫视' , '金鹰卡通', '风云足球', 'CHC高清电影',  'CHC动作电影',  '风云音乐', '第一剧场', '风云剧场', '世界地理', '怀旧剧场', '兵器科技', '女性时尚', 'CCTV-娱乐', 'CCTV-戏曲', 'CCTV-电影', '高尔夫网球']
# name_list = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17', 'CGTN', 'CCTV4EUO', 'CCTV4AME', 'CCTV4K','CCTV8K', 'CCTV16', '湖南卫视', '浙江卫视', '江苏卫视', '北京卫视', '东方卫视', '安徽卫视', '广东卫视', '深圳卫视', '辽宁卫视', '旅游卫视', '山东卫视', '天津卫视', '重庆卫视', '东南卫视', '甘肃卫视', '广西卫视', '贵州卫视', '河北卫视', '黑龙江卫视', '河南卫视', '湖北卫视', '江西卫视', '吉林卫视', '内蒙古卫视', '宁夏卫视', '山西卫视', '陕西卫视', '四川卫视', '新疆卫视', '云南卫视', '青海卫视', '南方卫视', '兵团卫视', '延边卫视', '黄河卫视', '厦门卫视', '金鹰卡通', '康巴卫视', '西藏卫视', '三沙卫视', '中国教育1台', '中国教育2台', '中国教育3台', '3D电视试验频道', '外汇理财', '电竞天堂', 'IPTV5+', 'IPTV6+', 'IPTV经典电影', 'IPTV热播剧场', 'IPTV少儿动画', 'IPTV魅力时尚', '风云足球', '求索科学', 'CHC高清电影', '求索动物', '求索记录', 'CHC动作电影', 'CHC家庭电影', '梨园', '风云音乐', '第一剧场', '风云剧场', '世界地理', '怀旧剧场', '兵器科技', '女性时尚', 'CCTV-娱乐', 'CCTV-戏曲', 'CCTV-电影', '高尔夫网球', '央视精品', '彩民在线', '法律服务', '汽摩', '留学世界', '青年学苑', '摄影频道', '天元围棋', '现代女性', '早期教育', '证券资讯', '央视台球', '茶频道', '武术世界', '发现之旅', '环球奇观', '国学', '文物宝库', '新科动漫', '幼儿教育', '老故事', '快乐垂钓', '书画频道', 'DOXTV', '先锋乒羽', '车迷频道', '优优宝贝', '四海钓鱼', '动感音乐', '环球旅游', '新娱乐', '京视剧场', '弈坛春秋', '央广健康', '时代家居', '时代出行', '时代风尚', '财富天下', '百姓健康', '精品剧场', '少儿动漫', '欧美影院', '中国教育4台', '卡酷动画', '北京纪实', 'BTV文艺', 'BTV科教', 'BTV影视', 'BTV财经', 'BTV生活', 'BTV青年', 'BTV新闻', '哈哈炫动', 'DOX雅趣', '七彩戏剧', '新视觉', '劲爆体育', 'DOX英伦', 'DOX剧场', 'MAX极速汽车', '全纪实', '欢笑剧场', '幸福彩', '生活时尚', '游戏风云', '上视新闻频道', '第一财经', '东方影视', '五星体育频道', '上海纪实', '上海都市频道', '上视外语频道', '中国交通频道', '魅力足球', 'SCTV2', 'SCTV3', 'SCTV4', 'SCTV5', 'SCTV7', '峨嵋电影', 'SCTV9', 'SCTV8', 'CDTV1', 'CDTV2', 'CDTV3', 'CDTV4', 'CDTV5', 'CDTV6', 'wenjiang', '爱上4K', '山东齐鲁', '山东体育', '山东农科', '山东公共', '山东少儿', '山东影视', '山东综艺', '山东生活', '环宇电影', 'GTV游戏竞技', '网络棋牌', '新动漫', '辽宁都市', '辽宁影视剧', '辽宁青少', '辽宁生活', '辽宁公共', '辽宁北方', '辽宁体育', '辽宁经济', '沈阳新闻', '湖北综合频道', '湖北影视频道', '湖北教育频道', '湖北生活频道', '湖北公共·新闻', '湖北经济频道', '湖北垄上频道', '武汉新闻综合频道', '武汉电视剧频道', '武汉科技生活频道', '武汉经济频道', '武汉文体频道', '武汉外语频道', '武汉少儿频道', '武汉教育电视台', '优漫卡通', '嘉佳卡通', '广东体育', '广东公共', '珠江海外', '广东新闻', '广东国际', '珠江频道', '广东影视', '广东综艺', '广东经济', '广东少儿', '金鹰纪实', '翡翠台', '明珠台', 'TVB经典台', '无线新闻', '无线财经', '凤凰中文', '凤凰资讯', '凤凰香港', '阳光卫视', '美亚高清电影台', 'ViuTV', 'HKS', 'J2', '香港国际财经台', '香港开电视', '有线财经资讯台', '有线新闻台', '香港603', 'TVB星河频道', '星卫HD电影', '东森亚洲新闻台', '东森亚洲卫视', '公视2', 'GoodTV2', '壹电视综合台', '壹电视电影台', 'BabyTV', '公视三台', '民视无线台', '台视', '大爱一台', '中视', '人间卫视', '华视', '公视', 'GoodTV', '原住民频道', '客家电视台', 'MOMO亲子台', '东森幼幼台', '纬来综合台', '八大第一台', '八大综合台', '三立台湾台', '三立都会台', '卫视中文台', '东森综合台', '东森超视', '中天综合台', '东风卫视', '年代MUCH', '中天娱乐台', '东森戏剧台', '八大戏剧台', 'TVBS欢乐台', '纬来戏剧台', '高点综合台', 'JET综合台', '壹电视新闻台', '年代新闻台', '东森新闻台', '民视新闻台', '三立新闻台', 'TVBS新闻台', 'TVBS', '东森财经新闻台', '非凡新闻台', '卫视电影台', '东森电影台', '纬来电影台', 'LSTime电影台', '东森洋片台', '好莱坞电影台', '纬来育乐台', '纬来体育台', '纬来日本台', '国兴卫视', '靖天综合台', '靖天资讯台', '信吉电视台', '靖洋戏剧台', '冠军电视台', '台湾艺术台', '全大电视台', '非凡商业台', '三立财经新闻台', '运通财经', 'SBN全球财经台', '诚心电视台', 'MTV', '靖天映画', '海豚综合台', '霹雳台湾台', '十方法界', '信大频道', '华藏卫视', 'Z频道', '佛卫慈悲台', '生命频道', '天良综合台', '正德电视台', '高点育乐台', '冠军梦想台', '八大娱乐台', '大立电视台', '幸福空间居家台', '大爱二台', '台视新闻台', '台视财经台', '台视综合台', '靖天欢乐台', '靖天育乐台', '靖天日本台', 'FoodNetwork美食台', 'HGTV居家乐活', 'TravelChannel', '亚洲美食频道', '寰宇新闻', '亚洲旅游台', '博斯运动二台', '博斯网球台', '博斯无限台', '博斯高球1台', '博斯高球2台', '博斯魅力网', '博斯运动一台', '博斯无限二台', '达文西频道', '靖洋卡通台', '靖天卡通台', '三立综合台', '龙华偶像', '龙华戏剧', '龙华电影', '龙华经典', '龙华影剧', '龙华洋片', '民视第一台', '民视台湾台', '民视', '中视菁采台', 'TVBS精采台', 'BabyFirst', '民视综艺台', '华艺MBC', 'TRACEUrban', 'FashionOne', '龙华日韩台', '靖天戏剧台', '靖天电影台', 'wakuwaku', '中视经典', 'iFun1', 'iFun3', '中视新闻', 'CI', 'cnex', '采昌影剧', '智林体育', '影迷数位纪实', '影迷数位电影', 'ELTV', '靖天国际', '龙华动画', 'MTV综合', '爱尔达体育2', 'LUXETV', 'rollor', '亚洲综合', '寰宇HD综合', '纬来精采', 'Ettoday', '八大优', '台湾戏剧', '爱尔达影剧', 'MY101综合', '星卫娱乐', '寰宇财经', 'CatchPlay电影', 'MyCinemaEurope', 'TFC', 'MY-KIDS', '爱尔达体育1', '爱尔达体育3', '狼谷竞技', '美食星球', 'EYE旅游', '爱尔达综合', '天天电视', '三立戏剧', 'EYE戏剧', '曼迪日本', 'StarMoviesHD', '华艺影剧', '唯心电视', '澳亚卫视', 'NHKWorld', '国家地理野生频道', 'MEZZOLIVEHD', 'Lifetime', 'BBCWorldNews', 'CN卡通频道', 'CNBCHongKong', '国家地理频道', 'FashionTV', 'FXHD', 'DW', 'TV5Monde', 'france24', 'SkyNews', 'cinemaworld', 'CGTNDocumentary', 'TraceSports', 'Outdoor', 'HITS', 'CNN', '国家地理频道(台湾)', 'Discovery', 'TLC旅游生活频道', '动物星球', 'Disney', 'HBO', 'AXN', 'FOXMOVIES', 'CINEMAX', 'FOXSports', 'ELEVEN体育一台', 'FOX', 'NHK', 'ChannelNewsAsia', 'BloombergTV', 'ArirangTV', 'BBCLifestyle', 'DREAMWORKS', 'WarnerTV', 'HBOHD', 'HBOHits', 'HBOSignature', 'HBOFamily', 'BlueAntEntertainment', 'tvN', '韩国娱乐台KMTV', 'EVE', 'Discovery科学', 'DiscoveryAsia', 'DMAX', '梅迪奇艺术', 'BlueAntExtreme', 'Euronews', 'Nickelodeon', 'NickJr.', 'CBeebies', 'Boomerang', 'BBCEarth', 'ABCAustralia', 'CNNHeadlineNews', 'NHKWorldPremium', '爱尔达娱乐台', 'ELEVEN体育二台', 'History', 'SMART知识频道', 'AMC', 'aljazeera', 'EUROSPORT', 'Animax']
cctv1_17 = ['CCTV'+str(g) for g in range(1,18)]
cctv1_17_2 = ['CCTV-'+str(g) for g in range(1,18)]
cctvs = []
def get_name(name_txt):
    import re
    pattern = re.compile(r'-?\d+\.*\d*')  # 正则匹配数字(包括正负及浮点数)
    name = ''
#     name_list = ['CCTV1', 'CCTV2', 'CCTV3', 'CCTV4', 'CCTV5', 'CCTV5+', 'CCTV6', 'CCTV7', 'CCTV8', 'CCTV9', 'CCTV10', 'CCTV11', 'CCTV12', 'CCTV13', 'CCTV14', 'CCTV15', 'CCTV17', 'CGTN', 'CCTV4EUO', 'CCTV4AME', 'CCTV4K', 'CCTV16', '湖南卫视', '浙江卫视', '江苏卫视', '北京卫视', '东方卫视', '安徽卫视', '广东卫视', '深圳卫视', '辽宁卫视', '旅游卫视', '山东卫视', '天津卫视', '重庆卫视', '东南卫视', '甘肃卫视', '广西卫视', '贵州卫视', '河北卫视', '黑龙江卫视', '河南卫视', '湖北卫视', '江西卫视', '吉林卫视', '内蒙古卫视', '宁夏卫视', '山西卫视', '陕西卫视', '四川卫视', '新疆卫视', '云南卫视', '青海卫视', '南方卫视', '兵团卫视', '延边卫视', '黄河卫视', '厦门卫视', '金鹰卡通', '康巴卫视', '西藏卫视', '三沙卫视', '中国教育1台', '中国教育2台', '中国教育3台', '3D电视试验频道', '外汇理财', '电竞天堂', 'IPTV5+', 'IPTV6+', 'IPTV经典电影', 'IPTV热播剧场', 'IPTV少儿动画', 'IPTV魅力时尚', '风云足球', '求索科学', 'CHC高清电影', '求索动物', '求索记录', 'CHC动作电影', 'CHC家庭电影', '梨园', '风云音乐', '第一剧场', '风云剧场', '世界地理', '怀旧剧场', '兵器科技', '女性时尚', 'CCTV-娱乐', 'CCTV-戏曲', 'CCTV-电影', '高尔夫网球', '央视精品', '彩民在线', '法律服务', '汽摩', '留学世界', '青年学苑', '摄影频道', '天元围棋', '现代女性', '早期教育', '证券资讯', '央视台球', '茶频道', '武术世界', '发现之旅', '环球奇观', '国学', '文物宝库', '新科动漫', '幼儿教育', '老故事', '快乐垂钓', '书画频道', 'DOXTV', '先锋乒羽', '车迷频道', '优优宝贝', '四海钓鱼', '动感音乐', '环球旅游', '新娱乐', '京视剧场', '弈坛春秋', '央广健康', '时代家居', '时代出行', '时代风尚', '财富天下', '百姓健康', '精品剧场', '少儿动漫', '欧美影院', '中国教育4台', '卡酷动画', '北京纪实', 'BTV文艺', 'BTV科教', 'BTV影视', 'BTV财经', 'BTV生活', 'BTV青年', 'BTV新闻', '哈哈炫动', 'DOX雅趣', '七彩戏剧', '新视觉', '劲爆体育', 'DOX英伦', 'DOX剧场', 'MAX极速汽车', '全纪实', '欢笑剧场', '幸福彩', '生活时尚', '游戏风云', '上视新闻频道', '第一财经', '东方影视', '五星体育频道', '上海纪实', '上海都市频道', '上视外语频道', '中国交通频道', '魅力足球', 'SCTV2', 'SCTV3', 'SCTV4', 'SCTV5', 'SCTV7', '峨嵋电影', 'SCTV9', 'SCTV8', 'CDTV1', 'CDTV2', 'CDTV3', 'CDTV4', 'CDTV5', 'CDTV6', 'wenjiang', '爱上4K', '山东齐鲁', '山东体育', '山东农科', '山东公共', '山东少儿', '山东影视', '山东综艺', '山东生活', '环宇电影', 'GTV游戏竞技', '网络棋牌', '新动漫', '辽宁都市', '辽宁影视剧', '辽宁青少', '辽宁生活', '辽宁公共', '辽宁北方', '辽宁体育', '辽宁经济', '沈阳新闻', '湖北综合频道', '湖北影视频道', '湖北教育频道', '湖北生活频道', '湖北公共·新闻', '湖北经济频道', '湖北垄上频道', '武汉新闻综合频道', '武汉电视剧频道', '武汉科技生活频道', '武汉经济频道', '武汉文体频道', '武汉外语频道', '武汉少儿频道', '武汉教育电视台', '优漫卡通', '嘉佳卡通', '广东体育', '广东公共', '珠江海外', '广东新闻', '广东国际', '珠江频道', '广东影视', '广东综艺', '广东经济', '广东少儿', '金鹰纪实', '翡翠台', '明珠台', 'TVB经典台', '无线新闻', '无线财经', '凤凰中文', '凤凰资讯', '凤凰香港', '阳光卫视', '美亚高清电影台', 'ViuTV', 'HKS', 'J2', '香港国际财经台', '香港开电视', '有线财经资讯台', '有线新闻台', '香港603', 'TVB星河频道', '星卫HD电影', '东森亚洲新闻台', '东森亚洲卫视', '公视2', 'GoodTV2', '壹电视综合台', '壹电视电影台', 'BabyTV', '公视三台', '民视无线台', '台视', '大爱一台', '中视', '人间卫视', '华视', '公视', 'GoodTV', '原住民频道', '客家电视台', 'MOMO亲子台', '东森幼幼台', '纬来综合台', '八大第一台', '八大综合台', '三立台湾台', '三立都会台', '卫视中文台', '东森综合台', '东森超视', '中天综合台', '东风卫视', '年代MUCH', '中天娱乐台', '东森戏剧台', '八大戏剧台', 'TVBS欢乐台', '纬来戏剧台', '高点综合台', 'JET综合台', '壹电视新闻台', '年代新闻台', '东森新闻台', '民视新闻台', '三立新闻台', 'TVBS新闻台', 'TVBS', '东森财经新闻台', '非凡新闻台', '卫视电影台', '东森电影台', '纬来电影台', 'LSTime电影台', '东森洋片台', '好莱坞电影台', '纬来育乐台', '纬来体育台', '纬来日本台', '国兴卫视', '靖天综合台', '靖天资讯台', '信吉电视台', '靖洋戏剧台', '冠军电视台', '台湾艺术台', '全大电视台', '非凡商业台', '三立财经新闻台', '运通财经', 'SBN全球财经台', '诚心电视台', 'MTV', '靖天映画', '海豚综合台', '霹雳台湾台', '十方法界', '信大频道', '华藏卫视', 'Z频道', '佛卫慈悲台', '生命频道', '天良综合台', '正德电视台', '高点育乐台', '冠军梦想台', '八大娱乐台', '大立电视台', '幸福空间居家台', '大爱二台', '台视新闻台', '台视财经台', '台视综合台', '靖天欢乐台', '靖天育乐台', '靖天日本台', 'FoodNetwork美食台', 'HGTV居家乐活', 'TravelChannel', '亚洲美食频道', '寰宇新闻', '亚洲旅游台', '博斯运动二台', '博斯网球台', '博斯无限台', '博斯高球1台', '博斯高球2台', '博斯魅力网', '博斯运动一台', '博斯无限二台', '达文西频道', '靖洋卡通台', '靖天卡通台', '三立综合台', '龙华偶像', '龙华戏剧', '龙华电影', '龙华经典', '龙华影剧', '龙华洋片', '民视第一台', '民视台湾台', '民视', '中视菁采台', 'TVBS精采台', 'BabyFirst', '民视综艺台', '华艺MBC', 'TRACEUrban', 'FashionOne', '龙华日韩台', '靖天戏剧台', '靖天电影台', 'wakuwaku', '中视经典', 'iFun1', 'iFun3', '中视新闻', 'CI', 'cnex', '采昌影剧', '智林体育', '影迷数位纪实', '影迷数位电影', 'ELTV', '靖天国际', '龙华动画', 'MTV综合', '爱尔达体育2', 'LUXETV', 'rollor', '亚洲综合', '寰宇HD综合', '纬来精采', 'Ettoday', '八大优', '台湾戏剧', '爱尔达影剧', 'MY101综合', '星卫娱乐', '寰宇财经', 'CatchPlay电影', 'MyCinemaEurope', 'TFC', 'MY-KIDS', '爱尔达体育1', '爱尔达体育3', '狼谷竞技', '美食星球', 'EYE旅游', '爱尔达综合', '天天电视', '三立戏剧', 'EYE戏剧', '曼迪日本', 'StarMoviesHD', '华艺影剧', '唯心电视', '澳亚卫视', 'NHKWorld', '国家地理野生频道', 'MEZZOLIVEHD', 'Lifetime', 'BBCWorldNews', 'CN卡通频道', 'CNBCHongKong', '国家地理频道', 'FashionTV', 'FXHD', 'DW', 'TV5Monde', 'france24', 'SkyNews', 'cinemaworld', 'CGTNDocumentary', 'TraceSports', 'Outdoor', 'HITS', 'CNN', '国家地理频道(台湾)', 'Discovery', 'TLC旅游生活频道', '动物星球', 'Disney', 'HBO', 'AXN', 'FOXMOVIES', 'CINEMAX', 'FOXSports', 'ELEVEN体育一台', 'FOX', 'NHK', 'ChannelNewsAsia', 'BloombergTV', 'ArirangTV', 'BBCLifestyle', 'DREAMWORKS', 'WarnerTV', 'HBOHD', 'HBOHits', 'HBOSignature', 'HBOFamily', 'BlueAntEntertainment', 'tvN', '韩国娱乐台KMTV', 'EVE', 'Discovery科学', 'DiscoveryAsia', 'DMAX', '梅迪奇艺术', 'BlueAntExtreme', 'Euronews', 'Nickelodeon', 'NickJr.', 'CBeebies', 'Boomerang', 'BBCEarth', 'ABCAustralia', 'CNNHeadlineNews', 'NHKWorldPremium', '爱尔达娱乐台', 'ELEVEN体育二台', 'History', 'SMART知识频道', 'AMC', 'aljazeera', 'EUROSPORT', 'Animax']
    t=''
    for t in name_list:
        if t in name_txt or t.replace('CCTV','CCTV-') in name_txt :
            name = t
    if 'CCTV' in name_txt and "+" not in name_txt and name == '':
        numbers = re.findall(pattern, name_txt)       
        if 'CCTV'+numbers[0].strip("-") if len(numbers)>0 else 0 in cctv1_17:
            name = 'CCTV'+ numbers[0].strip("-") if len(numbers)>0 else ''
    return name
import re
final_dict = {}
try:
    with open('final_dict.json', 'r', encoding='utf-8') as f:
        final_dict = json.loads(f.read())
except:
    pass

def url_order_score(link):
    score = 0
    if 'PLTV' in link:
        score+=5
    if len(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", link)) >0:
        score+=3
    if 'cdn' in link:
        score+=4
    if 'http' in link:
        score+=1
    if 'rtsp' in link:
        score+=2
    if len(link.split('/'))>2 and ':' in link.split('/')[2]:
        score-=5
    if  link in all_links:
        score = score - mean(all_links[link])/10000.0
    return score

for name in name_list:
    if not name in final_dict:
        final_dict[name] = []                

for name_txt in channels:
    name = get_name(name_txt)
    if not name == '' and name in name_list:  
        for link in channels[name_txt]:
            link = link.strip('\r').split('$')[0]
            if link not in final_dict[name]:
                final_dict[name].append(link)
                all_links[link] = [10000,10000,10000,10000,10000]
for name in  final_dict  :
    final_dict[name].sort(key=url_order_score,reverse=True)
for name in final_dict:
    for link in final_dict[name]:
        l = int(mean(all_links[link]))    
        print(f'{name}->{l} {link} ')
        
        
with open('all_links.json', 'w') as f:
    f.write(json.dumps(all_links))
with open('final_dict.json', 'w') as f:
    f.write(json.dumps(final_dict))

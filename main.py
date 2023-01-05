import hashlib
import json
import requests
import time

# 配置cookie 支持多账号一行一个 放单引号里面 根据实际需求增删
cookie = [
    '__ckguid=jAgL936po9C2T62tWJFVU57; device_id=21307064331672890790738551ba267c42096d5ea85a0b78887bc469ac; '
    'homepage_sug=c; r_sort_type=score; _zdmA.uid=ZDMA.0GekqFQe6.1672892582.2419200; _zdmA.vid=*; '
    'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185800fb50adf-03c84c98c0ca7c-40262c3c-2073600'
    '-185800fb50b13a1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B'
    '%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7'
    '%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A'
    '%22185800fb50adf-03c84c98c0ca7c-40262c3c-2073600-185800fb50b13a1%22%7D; sajssdk_2015_cross_new_user=1; '
    'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672890791; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1672892582; '
    'footer_floating_layer=0; ad_date=5; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number'
    '%22%3A0%2C%22surplus%22%3A7%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus'
    '%22%3A1%7D%2C%7B%22number%22%3A2%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; '
    'ad_json_feed=%7B%7D; amvid=fbcc89e030537a6adaa6171fca22f68c; '
    '_zdmA.time=1672892841042.0.https%3A%2F%2Fwww.smzdm.com%2F; '
    'sess=BA-0vZVXvopIiJCGVEaIT0YxphK0yo9lUD5sSdTbmW5JslaDfIw2QCbYTqSCTA1Yb0mWuK3%2F1q88fYk1y4dVn9Fxq4OSYVsD'
    '%2F0ab3sBj%2BXpjTAA50Ri6HWbRCnR; user=user%3A8215148701%7C8215148701; smzdm_id=8215148701',
]

for i in range(len(cookie)):
    print(f'开始第{i + 1}个帐号签到')
    ts = int(round(time.time() * 1000))
    url = 'https://user-api.smzdm.com/robot/token'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    data = {
        "f": "android",
        "v": "10.4.1",
        "weixin": 1,
        "time": ts,
        "sign": hashlib.md5(bytes(f'f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',
                                  encoding='utf-8')).hexdigest().upper()
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = html.json()
    token = result['data']['token']

    Timestamp = int(round(time.time() * 1000))
    data = {
        "f": "android",
        "v": "10.4.1",
        "sk": "ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
        "weixin": 1,
        "time": Timestamp,
        "token": token,
        "sign": hashlib.md5(bytes(
            f'f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={Timestamp}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',
            encoding='utf-8')).hexdigest().upper()
    }
    url = 'https://user-api.smzdm.com/checkin'
    url2 = 'https://user-api.smzdm.com/checkin/all_reward'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    html = requests.post(url=url, headers=headers, data=data)
    html2 = requests.post(url=url2, headers=headers, data=data)
    result = json.loads(html.text)['error_msg']
    result2 = json.loads(html2.text)
    print(result)
    print(result2)

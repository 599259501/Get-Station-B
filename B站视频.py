import datetime  # 获取当前时间来命名获取时间
import json  # 格式化js数据
import os  # 系统模块创建文件夹
import pprint  # 输出格式
import re  # 正则表达式
import subprocess  # 音乐合成

import requests

now_time = datetime.date.today()
url = 'https://www.bilibili.com/video/BV1vj411A7FV/?spm_id_from=333.1073.high_energy.content.click&vd_source=97f9a774cab41cf9a663b028fd22ac8c'
head = {
    "cookie": "buvid3=2F862517-4AC7-8AEC-269E-E6C92A58C7D737791infoc; b_nut=1671788837; i-wanna-go-back=-1; _uuid=B7FDB1106-CE99-A713-B10F10-3AFBC1106DA8439244infoc; buvid4=7CAB9AFD-9CA7-2F0B-ED4A-9F98451E2C2140972-022122317-0f0VHGRE8w3drpfRP8hy+w%3D%3D; rpdid=|(J|)JulmkR~0J'uY~u)||uuu; buvid_fp_plain=undefined; DedeUserID=1099830934; DedeUserID__ckMd5=86b1ea358f344983; CURRENT_QUALITY=80; nostalgia_conf=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; fingerprint=5dcc7bd2785e3a5bf4cab7f6693e551a; buvid_fp=5dcc7bd2785e3a5bf4cab7f6693e551a; CURRENT_FNVAL=4048; bsource=search_bing; innersign=1; bp_video_offset_1099830934=757710296572756100; PVID=2; b_lsid=BBFE785C_18612048F78; SESSDATA=825b64a8%2C1690893410%2C59393%2A21; bili_jct=5b701fbbe738bd5ba62ed580289d622d; sid=62nx3599",
    "referer": "https://www.bilibili.com/",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
}
response = requests.get(url=url, headers=head)

data = response.text

title = re.findall(
    '"title":"(.*?),"pubdate"', response.text)[0]
html_data = re.findall(
    '<script>window.__playinfo__=(.*?)</script>', response.text)[0]
json_data = json.loads(html_data)
# pprint.pprint(json_data)
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_url = json_data['data']['dash']['video'][0]['baseUrl']
video_info = [title, audio_url, video_url]
title = re.sub('[\\/:*?,.\"<>|\\n\']', '', title)
# print(title)
# 音频的二进制数据       response.content 获取相应的二进制数据
audio_content = requests.get(url=video_url, headers=head).content
# print(audio_content)
# 视频的二进制数据
print(title)
video_content = requests.get(url=audio_url, headers=head).content
print("正在下载中....")
filename = f'H:/B站/{now_time}_{title}/'
if not os.path.exists(filename):
    os.mkdir(filename)
with open(filename+title+".mp4", mode='wb')as f:
    f.write(audio_content)
print(audio_url)
print("正在下载中....")
with open(filename+title+'.mp3', mode='wb')as f:
    f.write(video_content)
print(video_url)
print("视频内容保存完成...")
# a = f'ffmpeg -i  {filename} {title}.mp3 -i {title}.mp4 -c:v copy -c:a aac -strict experimental {filename}\\{title}+合成.mp4'
# subprocess.run(a, shell=True)
# print("视频合成成功！！！")

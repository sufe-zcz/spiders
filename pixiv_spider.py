import requests
from fake_useragent import UserAgent
import json
import time
requests.adapters.DEFAULT_RETRIES = 5


proxies = {
    "http": "47.92.234.75:80",
    "https": "47.92.234.75:80"
}

ID = "30798372"
UA = UserAgent()


def get_word_id(id):
    # url = f"https://www.pixiv.net/ajax/user/{id}/profile/top?lang=zh"
    url = "https://www.pixiv.net/ajax/user/30798372/profile/illusts?ids[]=96030798&ids[]=95937343&ids[]=95839883&ids[]=95640276&ids[]=95552176&ids[]=95226443&ids[]=95097468&ids[]=94993442&ids[]=94862458&ids[]=94764370&ids[]=94695449&ids[]=94675363&ids[]=94595786&ids[]=94416460&ids[]=94353435&ids[]=94240279&ids[]=94116154&ids[]=94051100&ids[]=93902328&ids[]=93793130&ids[]=93596716&ids[]=93491943&ids[]=93428367&ids[]=93271963&ids[]=93180775&ids[]=93110610&ids[]=92943203&ids[]=92843233&ids[]=92651899&ids[]=92563950&ids[]=92334153&ids[]=92162063&ids[]=92041912&ids[]=91985550&ids[]=91928798&ids[]=91904912&ids[]=91801332&ids[]=91710078&ids[]=91523952&ids[]=91450625&ids[]=91383673&ids[]=91268564&ids[]=91184024&ids[]=91108954&ids[]=91063873&ids[]=90993069&ids[]=90859865&ids[]=90807573&work_category=illustManga&is_first_page=1&lang=zh"    # headers = {
    #     "authority": "www.pixiv.net",
    #     "method": "GET",
    #     "path": f"/ajax/user/{id}/profile/all?lang=zh",
    #     "user-agent": UA.random
    # }
    headers = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
               'referer': 'https://www.pixiv.net/artworks/96030798',
               'sec-fetch-dest': 'image',
               'sec-fetch-mode': 'no-cors',
               'sec-fetch-site': 'cross-site',
               'user-agent': UA.random,
               "cookie": "first_visit_datetime_pc=2021-10-30+18:59:27; p_ab_id=1; p_ab_id_2=3; p_ab_d_id=1903733820; yuid_b=F5FpQoY; _ga=GA1.2.857176263.1635587969; c_type=20; privacy_policy_notification=0; a_type=0; b_type=1; privacy_policy_agreement=3; __utma=235335808.857176263.1635587969.1635587969.1635949138.2; __utmz=235335808.1635949138.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=66993514=1^9=p_ab_id=1=1^10=p_ab_id_2=3=1^11=lang=zh=1; ki_r=; ki_s=214908:0.0.0.0.2;214994:0.0.0.0.2;215190:0.0.0.0.2;220959:0.0.0.0.0; ki_t=1635588633465;1638080371463;1638080869736;5;29; PHPSESSID=66993514_b4PCaOU5fDdVV1gBKXezFzpWL2Vhb5xw; _gid=GA1.2.1631022672.1644494907; tag_view_ranking=Lt-oEicbBr~Ie2c51_4Sp~tgP8r-gOe_~RTJMXD26Ak~WVrsHleeCL~faHcYIP1U0~qtVr8SCFs5~Cc23GhmKNc~MC7yWU3YNW~9euyrr7oFl~FPCeANM2Bm~d9UpgqVAEz~pnCQRVigpy~DnmTE3Ec_I~RcahSSzeRf~0xsDLqCEW6~fg8EOt4owo~_EOd7bsGyl~X_1kwTzaXt~tzVOnrUz79~WDrRVlrKKs~7xMlE4CR3t~QaiOjmwQnI~UUZM6DRRvj~L36Q8o7i1e~txZ9z5ByU7~gpglyfLkWs~I-1xQGtn3G~ePN3h1AXKX~skx_-I2o4Y~ETjPkL0e6r~w7XDmF76rR~Ysf6p9hInm~YRDwjaiLZn~ziiAzr_h04~7-cdu1A0eA~bvp7fCUKNH~cFXtS-flQO~x_jB0UM4fe~BSlt10mdnm~IJkCuj9g6o~O2wfZxfonb~-oNVOx_K96~kZOrpQ0eOB~Wxk4MkYNNf~L7-FiupSjg~92z8RZmGQ6~kjfJ5uXq4m~RokSaRBUGr~jH0uD88V6F~BF2N4eoz_h~3Nx8WodkHF~5BQyNoZRWM~4N9NZ-TX3-~MSNRmMUDgC~ahO2xG1BUq~VMq-Vxsw8k~EUwzYuPRbU~JN2fNJ_Ue2~K8esoIs2eW~F-NKdmzAvA~CE4z81uaLD~OEIVtzPpB3~TEO656gSAo~Hn9qFX8COa~h_1FuDI5Nc~NJOmwtpQWD~-2AUmsDqzZ~0bNd1-hq-i~0YMUbkKItS~6QCMLTzs96~0oMmMHTqle~33kJYz6eWM~vYl0bVLhWW~I8DVKb4T8n~C7XTvPBYbD~PHQDP-ccQD~SGMAKY7jRo~YnvQJpeepV~IAswHyJ5H0~cofmB2mV_d~qnRhxi44Zq~ISKZqyBIeT~O64_t9evHE~awkRdldPOb~voBUJlwwSH~Q91GJOmVbQ~e2yEFDVXjZ~26-Sd3V3Py~nTjTRvH_ca~w54SU6Xx_L~gy4M_SbRJV~HrQjOxea1_~SzbEMY4eCb~pzzjRSV6ZO~CrFcrMFJzz~riCSPqp89S~LJo91uBPz4~I5npEODuUW~PGh9Qwfchx; __cf_bm=GBhkdm4MNqZ7265oxWw6xM_rM.0hFJJnxMJfew0LFjM-1644510939-0-AYVIN22gMi6WNzVQQt2MqB+fRgxad+7ERMepoaeXAA7a/YktCqksSv1PbhcquGaHPTEkhKDmDrrLx6eOZBa7uPZqhqjpOMAkZrvPZIO86mEyeXGWAFS70yBGZrHjbE0MoDsUMUXKOeKD06xdmPnQZDx2Va96UEynuwFRwPlsyByGjDgkFZAxbgqqQ3JVvruYkg==; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:21"
               }
    r = requests.get(url, headers=headers)
    k = list(r.json()["body"]["works"].keys())
    v = [r.json().get("body").get("works").get(key)["url"] for key in k]
    v = ["/".join(s.split("/")[7:13]) for s in v]

    return k, v


def get_pic(ids, urls, id):
    n = len(ids)
    for i in range(n):
        url = f"https://i.pximg.net/img-original/img/{urls[i]}/{ids[i]}_p0.jpg"
        print("正在爬取", url)
        headers = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
                   'referer': f'https://www.pixiv.net/artworks/{id}',
                   'sec-fetch-dest': 'image',
                   'sec-fetch-mode': 'no-cors',
                   'sec-fetch-site': 'cross-site',
                   'user-agent': UA.random
                   }
        try:
            r = requests.get(url, headers=headers)
            with open(f"./hhh/{ids[i]}.jpg", "wb") as f:
                f.write(r.content)
            print(f"{ids[i]}", "保存成功")
        except:
            print(f"{ids[i]}", "爬取失败")
        time.sleep(1)


IDS, URLS = get_word_id(id=ID)
print(IDS)
get_pic(IDS, URLS, ID)

# get_word_id(id=ID)

import requests
from fake_useragent import UserAgent
import json
import time
import os
requests.adapters.DEFAULT_RETRIES = 5

# file_path = "/hhh"
# if not os.path.exists(file_path):
#     os.mkdir(file_path)


proxies = {
    "http": "120.71.147.244:8901",
    "https": "120.71.147.244:8901"
}

ID = "2188232"
UA = UserAgent()


def get_word_id(id):
    # url = f"https://www.pixiv.net/ajax/user/{id}/profile/top?lang=zh"
    url = "https://www.pixiv.net/ajax/user/2188232/profile/illusts?ids%5B%5D=53758179&ids%5B%5D=53643448&ids%5B%5D=53551654&ids%5B%5D=53275453&ids%5B%5D=53186325&ids%5B%5D=53003270&ids%5B%5D=52870588&ids%5B%5D=52495727&ids%5B%5D=52452497&ids%5B%5D=52098226&ids%5B%5D=51806057&ids%5B%5D=51739709&ids%5B%5D=51664160&ids%5B%5D=51531779&ids%5B%5D=51420765&ids%5B%5D=51331207&ids%5B%5D=51237302&ids%5B%5D=51217728&ids%5B%5D=51214025&ids%5B%5D=51166367&ids%5B%5D=51068746&ids%5B%5D=51040304&ids%5B%5D=45981451&ids%5B%5D=44745753&ids%5B%5D=43393846&ids%5B%5D=42754259&ids%5B%5D=42714955&work_category=illustManga&is_first_page=0&lang=zh"
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
               "cookie": "first_visit_datetime_pc=2021-10-30+18%3A59%3A27; p_ab_id=1; p_ab_id_2=3; p_ab_d_id=1903733820; yuid_b=F5FpQoY; _ga=GA1.2.857176263.1635587969; c_type=20; privacy_policy_notification=0; a_type=0; b_type=1; privacy_policy_agreement=3; __utma=235335808.857176263.1635587969.1635587969.1635949138.2; __utmz=235335808.1635949138.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=66993514=1^9=p_ab_id=1=1^10=p_ab_id_2=3=1^11=lang=zh=1; ki_r=; ki_s=214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B220959%3A0.0.0.0.0; ki_t=1635588633465%3B1638080371463%3B1638080869736%3B5%3B29; PHPSESSID=66993514_b4PCaOU5fDdVV1gBKXezFzpWL2Vhb5xw; _gid=GA1.2.1980262300.1648703166; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:25; tag_view_ranking=Lt-oEicbBr~tgP8r-gOe_~Ie2c51_4Sp~faHcYIP1U0~RcahSSzeRf~WVrsHleeCL~_EOd7bsGyl~RTJMXD26Ak~QaiOjmwQnI~0xsDLqCEW6~pnCQRVigpy~MSNRmMUDgC~DnmTE3Ec_I~qtVr8SCFs5~X_1kwTzaXt~Cc23GhmKNc~MC7yWU3YNW~9euyrr7oFl~FPCeANM2Bm~d9UpgqVAEz~HY55MqmzzQ~JooW_Hne2Q~y3NlVImyly~pzzjRSV6ZO~jH0uD88V6F~ziiAzr_h04~azESOjmQSV~BSlt10mdnm~OYl5wlor4w~txZ9z5ByU7~qnGN-oHRQo~UnI8eZzpBM~KrMg4c4zFf~Ui7_qOnwP5~CrFcrMFJzz~ETjPkL0e6r~NgIJwXbXYc~SVCXbGp5Sf~fg8EOt4owo~tg4cf2wCF6~KN7uxuR89w~bfM8xJ-4gy~-StjcwdYwv~5oPIfUbtd6~yREQ8PVGHN~gpglyfLkWs~30YRghWWsb~28gdfFXlY7~y8GNntYHsi~BU9SQkS-zU~62FPd2uRc6~xha5FQn_XC~HpnacYZr6z~skx_-I2o4Y~wmxKAirQ_H~tzVOnrUz79~WDrRVlrKKs~7xMlE4CR3t~UUZM6DRRvj~_RfiUqtsxe~rqnJSF7cpq~9OgM5t9f0L~48UjH62K37~q303ip6Ui5~yv-MdmoUJ0~O2wfZxfonb~fIMPtFR8GH~-mS39rlV30~PzEXgc_S56~9Gbahmahac~LtW-gO6CmS~mzJgaDwBF5~ZTBAtZUDtQ~K8esoIs2eW~DpYZ-BAzxm~hW_oUTwHGx~eVxus64GZU~4TDL3X7bV9~L36Q8o7i1e~I-1xQGtn3G~ePN3h1AXKX~w7XDmF76rR~iFIin44D8E~H8dBmnNhw6~NsbQEogeyL~aSdrnGinfC~jpIZPQ502H~CiSfl_AE0h~gFv6cfMyax~cuImfsdRMn~OqJHdm3tOZ~zcgN5vmPI2~Bd2L9ZBE8q~t2K257LiKY~TqiZfKmSCg~aA2ODQ1ACf~rNs-bh_gk3~-NJZeKTYP8~xXhWS_7AGn~EUwzYuPRbU; __cf_bm=MMfsKkXVQfqKzZaLqX2KUgqmKxxe7qRrhDadHo0BLrU-1648736067-0-AQZ8kdbwC3Rjv9htJTk0d2drIYSdo9DGykrOcH/ZXCKp0nGRWNqrFxzKqZwxrqiUYMm8BZ2Ab/JuCLIJSFa3FlIgP50WgUZYvh+QOeLrFoaxUvR8c8uhWXrQJdiNi4nbizOy0HsRYjnoNRIW6ad09HIOzxPChRyOEd1BtGC1xS29X9l/pf0GR0mdyruKgVbsdQ=="
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

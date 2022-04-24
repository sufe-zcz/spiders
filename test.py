import requests
from fake_useragent import UserAgent
import json
import time
requests.adapters.DEFAULT_RETRIES = 5

ID = "6662895"
UA = UserAgent()


def get_word_id(id):
    # url = f"https://www.pixiv.net/ajax/user/{id}/profile/top?lang=zh"
    url = "https://www.pixiv.net/ajax/user/6662895/profile/illusts?ids[]=96032449&ids[]=95864662&ids[]=95707204&ids[]=95553489&ids[]=95396392&ids[]=95228461&ids[]=95076680&ids[]=94863669&ids[]=94719612&ids[]=94571370&ids[]=94418447&ids[]=94264568&ids[]=94117580&ids[]=93967018&ids[]=93794438&ids[]=93640529&ids[]=93493044&ids[]=93338703&ids[]=93183925&ids[]=93018819&ids[]=92846013&ids[]=92679832&ids[]=92513644&ids[]=92336851&ids[]=92165002&ids[]=91987029&ids[]=91637314&ids[]=91477750&ids[]=91315580&ids[]=91157789&ids[]=90994458&ids[]=90834125&ids[]=90673394&ids[]=90513531&ids[]=90352192&ids[]=90187096&ids[]=89866644&ids[]=89705973&ids[]=89371729&ids[]=89219826&ids[]=89071274&ids[]=88914271&ids[]=88750899&ids[]=88591054&ids[]=88429604&ids[]=88266187&ids[]=88099937&ids[]=87926814&work_category=illust&is_first_page=1&lang=zh"
    #     "authority": "www.pixiv.net",
    #     "method": "GET",
    #     "path": f"/ajax/user/{id}/profile/all?lang=zh",
    #     "user-agent": UA.random
    # }
    headers = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
               'referer': 'https://www.pixiv.net/artworks/6662895',
               'sec-fetch-dest': 'image',
               'sec-fetch-mode': 'no-cors',
               'sec-fetch-site': 'cross-site',
               'user-agent': UA.random,
               "cookie": "first_visit_datetime_pc=2021-10-30+18:59:27; p_ab_id=1; p_ab_id_2=3; p_ab_d_id=1903733820; yuid_b=F5FpQoY; _ga=GA1.2.857176263.1635587969; c_type=20; privacy_policy_notification=0; a_type=0; b_type=1; privacy_policy_agreement=3; __utma=235335808.857176263.1635587969.1635587969.1635949138.2; __utmz=235335808.1635949138.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=66993514=1^9=p_ab_id=1=1^10=p_ab_id_2=3=1^11=lang=zh=1; ki_r=; ki_s=214908:0.0.0.0.2;214994:0.0.0.0.2;215190:0.0.0.0.2;220959:0.0.0.0.0; ki_t=1635588633465;1638080371463;1638080869736;5;29; PHPSESSID=66993514_b4PCaOU5fDdVV1gBKXezFzpWL2Vhb5xw; _gid=GA1.2.425635493.1644636219; __cf_bm=vSJJZyTDHoItO3Kw5rKKuYeQMCSmhKU_s5Zvt_OgZ5s-1644655366-0-AeTlFUWlv6okgoXBvqh1mcGDIJzICBHsx3RuKdPc6W818/l2MlAXvJLnW/7ec3cpcLtOJIitZAmbsSDk7xqmpGpzCxbGHVi9cbSXwcZE6jJ1LdJ8AnKgc/rpywrQnlZi1jlwE+Mt4qq2+CkTzD5N+pwcMTVGdJChzo6I5Q3wNsAmrCcvrVDBUWGe0CYlPAdIAA==; tag_view_ranking=tgP8r-gOe_~Lt-oEicbBr~Ie2c51_4Sp~WVrsHleeCL~faHcYIP1U0~RTJMXD26Ak~pnCQRVigpy~DnmTE3Ec_I~qtVr8SCFs5~Cc23GhmKNc~MC7yWU3YNW~9euyrr7oFl~FPCeANM2Bm~d9UpgqVAEz~RcahSSzeRf~_EOd7bsGyl~X_1kwTzaXt~QaiOjmwQnI~pzzjRSV6ZO~0xsDLqCEW6~UnI8eZzpBM~KrMg4c4zFf~Ui7_qOnwP5~fg8EOt4owo~MSNRmMUDgC~wmxKAirQ_H~tzVOnrUz79~WDrRVlrKKs~7xMlE4CR3t~UUZM6DRRvj~BSlt10mdnm~DpYZ-BAzxm~hW_oUTwHGx~eVxus64GZU~4TDL3X7bV9~L36Q8o7i1e~txZ9z5ByU7~gpglyfLkWs~I-1xQGtn3G~ePN3h1AXKX~skx_-I2o4Y~ETjPkL0e6r~w7XDmF76rR~JooW_Hne2Q~y3NlVImyly~62FPd2uRc6~xha5FQn_XC~PwDMGzD6xn~HpnacYZr6z~Ysf6p9hInm~YRDwjaiLZn~ziiAzr_h04~7-cdu1A0eA~bvp7fCUKNH~cFXtS-flQO~x_jB0UM4fe~IJkCuj9g6o~O2wfZxfonb~-oNVOx_K96~kZOrpQ0eOB~Wxk4MkYNNf~L7-FiupSjg~92z8RZmGQ6~_pwIgrV8TB~fIMPtFR8GH~w8ffkPoJ_S~-mS39rlV30~LmbPyhfNiW~65aiw_5Y72~DriUjI1aUj~sr5scJlaNv~L-d833hYKU~lfjGxLc_aO~Cr3jSW1VoH~fSOqxxa1Xl~ptyAET71lu~GI4GuwP6yD~EhqvooMrEX~-lpXNPUEil~FE9s9RlCMY~HBlflqJjBZ~pzZvureUki~9Gbahmahac~bfM8xJ-4gy~Za2W2r7DSk~1yIPTg75Rl~opuscjyi1Z~kjfJ5uXq4m~RokSaRBUGr~jH0uD88V6F~BF2N4eoz_h~3Nx8WodkHF~5BQyNoZRWM~4N9NZ-TX3-~ahO2xG1BUq~VMq-Vxsw8k~EUwzYuPRbU~JN2fNJ_Ue2~K8esoIs2eW~F-NKdmzAvA; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:33"
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
        proxies = {
            "http": f"",
            "https": f""
        }
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

import urllib.request

url = "https://uta.pw/shodou/img/28/214.png"
savename = "test.png"

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urllib.request.urlretrieve(url, savename)
print("저장되었습니다!")
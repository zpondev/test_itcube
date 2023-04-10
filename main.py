import requests

s = requests.get("https://old.rsvpu.ru/sveden/education/?ftp=/UchebPlan/7920_2022_%D0%A3%D0%9F_%D0%BC%D0%98%D0%A0_%D0%BE%D1%84%D0%BE_2022_%D0%AD%D0%A6%D0%9F.pdf", verify=False)

f = open("f.pdf", 'wb')
f.write(s.content)
f.close()

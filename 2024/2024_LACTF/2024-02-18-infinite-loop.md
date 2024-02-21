---
title: 2024 LACTF - infinite loop
author: thanguyen165
date: 2024-02-18 00:00:00 +0700
categories: [Write-ups, 2024_LACTF]
tags: [Misc, write-ups]
---

* 545 solves / 153 points
* author: burturt

## Description

> I found this google form but I keep getting stuck in a loop! Can you leak to me the contents of form and the message at the end so I can get credit in my class for submitting? Thank you!
>
> [Click here](https://docs.google.com/forms/d/e/1FAIpQLSfgUDWRzgkSC2pppOx_SVdw1E9bpVVWUkvQssmWza11pufMUQ/viewform)

### Document

If the link is dead, I have its source code in [attached](attached/infinite-loop.html)

## Solution

Look around the source code via dev tools, search for ```lactf```.

The flag is
```
lactf{l34k1ng_4h3_f04mz_s3cr3tz}
```
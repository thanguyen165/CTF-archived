---
title: 2023 ImaginaryCTF - blurry
author: Gr33nM0nk3y
date: 2023-07-23 00:00:00 +0700
categories: [Write-ups, 2023imaginaryCTF]
tags: [Forensics, write-ups]
---

* Points: 100

## Description

> QR codes are error-correcting... whatever that means. How much error can it take though?

### Attached

[blurry.png](https://imaginaryctf.org/r/kaegq#chall.png)

## Solution

Use [pinetools](https://pinetools.com/sharpen-image) to sharpen the qr code, then scan the new qr code.

The flag is

```
ictf{blurR1ng_is_n0_m4tch_4_u_2ab140c2}
```
---
title: 2024 LACTF - terms-and-conditions
author: thanguyen165
date: 2024-02-18 00:00:00 +0700
categories: [Write-ups, 2024_LACTF]
tags: [Web Exploitation]
---

* 771 solves / 106 points
* author: aplet123

## Description

> Welcome to LA CTF 2024! All you have to do is accept the terms and conditions and you get a flag!
>
> [terms-and-conditions.chall.lac.tf](https://terms-and-conditions.chall.lac.tf/)

### Attached

[term-and-conditions.html](attached/terms-and-conditions.html)

## Analyzation

Let's visit the site

![visit site](img/terms-and-condition-1.png)

The button, for sure, cannot be clicked by mouse. It must be "clicked" by console.

But when the console is opened, the site becomes blank and...

![NO CONSOLE ALLOWED](img/terms-and-condition-2.png)

Look up in the source code, this is reason why

```js
let width = window.innerWidth;
let height = window.innerHeight;
setInterval(function() {
    if (window.innerHeight !== height || window.innerWidth !== width) {
        document.body.innerHTML = "<div><h1>NO CONSOLE ALLOWED</h1></div>";
        height = window.innerHeight;
        width = window.innerWidth;
    }
}, 10);
```

## Solution

It only does that if the dimensions of the window changes after it loads.

So let's just leave the console there and refresh, and the console is on.

![refresh the site](img/terms-and-condition-3.png)

Then run the js command

```js
document.getElementById("accept").click()
```

![flag](img/terms-and-condition-4.png)

The flag is
```
lactf{that_button_was_definitely_not_one_of_the_terms}
```
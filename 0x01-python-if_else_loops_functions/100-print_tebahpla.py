#!/usr/bin/python3
for x in range(0, 26):
    word = ord('z') - x
    if (x % 2 == 1):
        word = chr(word - ord('a') + ord('A'))
    else:
        word = chr(word)
    print("{}".format(word), end='')

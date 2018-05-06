import sys
digit_string = sys.argv[1]
res = 0
for s in digit_string:
    res += int(s)
print(res)

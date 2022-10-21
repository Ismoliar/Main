
cache = {}
cache["a"] = 12
cache["b"] = 17

print(cache["a"])
print(cache["b"])

m = {}
m[13] = 280
m[51] = 300

print(1 in m)
print(13 in m)

if 51 in m:
    print("OK")

list = []
list.append(5)
list.append(0)
list.append(1)
print(list[0], list[1], list[2])
print(list[3])

#convert str to list
slist = list(s)
return slist
#or
for i in range(0, len(s)):
    print(s[i])

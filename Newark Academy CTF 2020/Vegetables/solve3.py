from pwn import connect
from collections import deque


# big brain O(n) by M. Magnusson
def is_sorted(arr):
    prev = arr[0]
    for elem in arr:
        if elem < prev:
            return False
        prev = elem
    return True

def conveyor_bubble(arr, d):
    steps = []
    while not is_sorted(arr): # :brain:
        if (arr[0] > arr[1]) and (arr[1] not in d[arr[0]]): # big :brain:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            steps.append("s")
            d[arr[0]].add(arr[1])
            d[arr[1]].add(arr[0])
        else:
            arr.rotate(-1)
            steps.append("c")
    return steps


r = connect("challenges.ctfd.io", "30267")
r.recvuntil("Enter 1, 2, 3, 4, or 5.\n")
r.sendline("3")

r.recvuntil("Dr. J needs help sorting the following veggies into alphabetical order:\n\n")
veges = r.recvline().decode('utf-8').strip().split(", ")

r.recvuntil("will swap the vegetable in position 0 with the vegetable in position 1")

steps = conveyor_bubble(deque(veges), {i : set() for i in veges})
r.sendline(' '.join(steps))

r.recvuntil("\xf0\x9f\xa5\xac\xf0\x9f\xa5\x95\xf0\x9f\x8c\xbd\xf0\x9f\x8d\x86\xf0\x9f\xa5\xa6\xf0\x9f\xa5\x92\xf0\x9f\xa5\x91\xf0\x9f\x8d\x84 That's correct!! \xf0\x9f\xa5\xac\xf0\x9f\xa5\x95\xf0\x9f\x8c\xbd\xf0\x9f\x8d\x86\xf0\x9f\xa5\xa6\xf0\x9f\xa5\x92\xf0\x9f\xa5\x91\xf0\x9f\x8d\x84\n")
print(r.recvline().decode('utf-8').strip())

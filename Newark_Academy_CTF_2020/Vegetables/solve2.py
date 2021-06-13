from pwn import connect

steps = []
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                steps.append(j)

r = connect("challenges.ctfd.io", "30267")
r.recvuntil("Enter 1, 2, 3, 4, or 5.\n")

r.sendline("2")

r.recvuntil("Dr. J needs help sorting the following veggies into alphabetical order:\n")
test = r.recvline()

veges = r.recvline().decode('utf-8').strip().split(", ")
# print(veges)

r.recvuntil("ive instructions for Dr. J's Robot to execute. Enter numbers separated by spaces to sort Dr. J's vegetables. Entering x will swap the vegetable in position x with the vegetable in position x+1")

bubble(veges)
# print(steps)

r.sendline(' '.join(map(str, steps)))

print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())

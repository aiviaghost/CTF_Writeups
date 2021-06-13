nums = map(int, "111 98 100 117 103 124 98 116 100 50 50 96 89 67 53 83 68 83 54 126".split())

out = ''.join([chr(i - 1) for i in nums])

print(out)
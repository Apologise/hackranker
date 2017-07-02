a = 'xyzwd'
result = ''

for i in range(len(a)):
	if i % 2 == 1:
		continue
	else:
		result += a[i]
print(result)
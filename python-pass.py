print('Input s:')
s=input()

output = ''

for i in range(len(s)):

    for j in range(len(s),0,-1):
        if len(output) >= j-i:
            break
        elif s[i:j] == s[i:j][::-1]:
            output = s[i:j][::-1]

print('output:',output)

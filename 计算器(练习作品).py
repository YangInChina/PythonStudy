n = 1
ans = 0
while n == 1:
    key = ['a']
    key[0] = input()
    b = key[0]
    if b[0] == '+':
        CountStr = b.count('+')
        LOF = b.split('+')
        for i in range(CountStr):
            ans = ans + int(LOF[i + 1])
        print('=', ans)
        continue
    elif b[0] == '-':
        CountStr = b.count('-')
        LOF = b.split('-')
        for i in range(CountStr):
            ans = ans - int(LOF[i + 1])
        print('=', ans)
        continue
    elif b[0] == '*':
        CountStr = b.count('*')
        LOF = b.split('*')
        for i in range(CountStr):
            ans = ans * int(LOF[i + 1])
        print('=', ans)
        continue
    elif b[0] == '/':
        CountStr = b.count('/')
        LOF = b.split('/')
        for i in range(CountStr):
            ans = ans / int(LOF[i + 1])
        print('=', ans)
        continue

    if '+' in b:
        ans = 0
        CountStr = b.count('+')
        LOF = b.split('+')
        for i in range(CountStr + 1):
            ans = ans + int(LOF[i])
        print('=', ans)



    elif '-' in b:
        ans = 0
        CountStr = b.count('-')
        LOF = b.split('-')
        for i in range(CountStr + 1):
            ans = ans - int(LOF[i])
        print('=', ans)
    elif '*' in b:
        ans = 0
        CountStr = b.count('*')
        LOF = b.split('*')
        for i in range(CountStr + 1):
            ans = ans * int(LOF[i])
        print('=', ans)
    elif '/' in b:
        ans = 0
        CountStr = b.count('/')
        LOF = b.split('/')
        for i in range(CountStr + 1):
            ans = ans / int(LOF[i])
        print('=', ans)

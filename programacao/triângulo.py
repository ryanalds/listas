A, B, C, D = map(int, input().split())

formou = False

if A + B > C and A + C > B and B + C > A:
    formou = True

if A + B > D and A + D > B and B + D > A:
    formou = True

if A + C > D and A + D > C and C + D > A:
    formou = True

if B + C > D and B + D > C and C + D > B:
    formou = True

if formou:
    print('S')
else:
    print('N')
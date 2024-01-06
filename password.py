import re


def pw_validation(passwd):
    if len(passwd) < 8:
        print('Password must be at least 8 characters')
    elif not re.search('[A-Z]', passwd):
        print('Password must contain at least 1 uppercase letter')
    elif not re.search(r'\W', passwd):
        print('Password must contain at least 1 special character')
    elif not re.search('[0-9]', passwd):
        print('Password must contain at least 1 number')
    else:
        d = re.findall('[0-9]+', passwd)
        for i in range(len(d)+1):
            if len(d[i]) >= 3:
                for j in range(len(d[i])-1):
                    if (int(d[i][j]) == int(d[i][j+1]) - 1) and (int(d[i][j+1]) == int(d[i][j+2]) - 1):
                        print('Password must not contain 3 consecutive numbers')
                    else:
                        break
        print('Password is valid')


# re.search(r'^\d{3}$', passwd)


while True:
    pw = input('Your password: ')
    if not pw_validation(pw):
        pass
    else:
        break

# a = '33455@@F'
# pw_validation(a)

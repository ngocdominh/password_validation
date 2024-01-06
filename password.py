import re


def pw_validation(passwd):
    if len(passwd) < 8:
        print('Password must be at least 8 characters')
        return False
    elif not re.search(r'[A-Z]', passwd):
        print('Password must contain at least 1 uppercase letter')
        return False
    elif not re.search(r'\W', passwd):
        print('Password must contain at least 1 special character')
        return False
    elif not re.search('[0-9]', passwd):
        print('Password must contain at least 1 digit')
        return False
    elif re.search(r'\d{3,}', passwd):
        d = re.findall(r'\d{3,}', passwd)
        for i in range(len(d)):
            for j in range(len(d[i])-2):
                if (int(d[i][j]) == int(d[i][j+1]) - 1) and (int(d[i][j+1]) == int(d[i][j+2]) - 1):
                    print('Password must not contain 3 consecutive digits')
                    return False
                # else:
                #     print('Password is valid')
                #     return True


# pw = input('Your password: ')
#
# pw_validation(pw)


# still stuck at the last condition

# while True:
#     pw = input('Your password: ')
#     if pw_validation(pw):
#         # print('Password is valid')
#         break
#     else:
#         pw = input('Your password: ')

# a = '33355@@F6678'
# pw_validation(a)

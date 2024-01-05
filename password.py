import re


def pw_validation(passwd):
    if len(passwd) < 8:
        print('Password must be at least 8 characters')
    elif not re.search('[A-Z]', passwd):
        print('Password must contain at least 1 uppercase letter')
    elif not re.search('[0-9]', passwd):
        print('Password must contain at least 1 number')
    elif not re.search(r'\W', passwd):
        print('Password must contain at least 1 special character')
    elif re.search(r'^\d{3}$', passwd):
        print('Password must not contain 3 consecutive numbers')
    else:
        print('Password is valid')
        return False


while True:
    pw = input('Your password: ')
    if not pw_validation(pw) is False:
        continue
    else:
        break



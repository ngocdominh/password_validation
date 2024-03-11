# Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern

# Sample Input: 5
#
# Sample Output :
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# Sample Input  : 3
#
# Sample Output :
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string

n = 5
alp = string.ascii_lowercase

for i in range(n-1, 0, -1):
    st = alp[i:n]
    cct = "-".join(st[::-1] + st[1:n-i])
    ln = cct.center(4 * n - 3, "-")
    print(ln)

for i in range(n):
    st = alp[i:n]
    cct = "-".join(st[::-1] + st[1:n-i])
    ln = cct.center(4 * n - 3, "-")
    print(ln)

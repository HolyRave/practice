# https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    if len(list(str(n)))>1:
        cnt = 0
        for i in list(str(n)):
            cnt += int(i)
        n = cnt
        return digital_root(n)
    else:
        return n

memo = {}
def edit(s1, s2):
    if s1=="":
        return len(s2)
    if s2=="":
        return len(s1)
    if s1+s2 not in memo:
        if s1[0]==s2[0]:
            memo[s1+s2] = edit(s1[1:], s2[1:])
        else:
            memo[s1+s2] = 1 +  min(edit(s1[1:], s2[1:]), edit(s1, s2[1:]), edit(s1[1:], s2))

    return memo[s1+s2]

print(edit("sundaysatursunday", "saturdaysunsatur"))

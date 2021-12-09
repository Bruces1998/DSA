def permut(string):
    allpermutations = []
    if len(string)==0:
        allpermutations.append("")
        return allpermutations

    fc = string[0]
    remainder = string[1:]
    words= permut(remainder)
    for word in words:
        for i in range(len(word)+1):
            word = [l for l in word]
            word.insert(i, fc)
            word = ''.join(word)
            allpermutations.append(word)



    return allpermutations

a = permut('aniket')
print(a)

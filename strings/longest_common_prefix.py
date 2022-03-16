'''
Link: https://leetcode.com/problems/longest-common-prefix/discuss/172553/beat-100-python-submission-short-and-clean
'''

def lcs(m):
    if not m:
        return ""

    s1 = min(m)
    s2 = max(m)

    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]

    return s1
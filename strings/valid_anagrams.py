def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0]*26
        
        for i in s:
            arr[ord(i) - ord("a")]+=1
            
        for i in t:
            if arr[ord(i) - ord("a")] == 0:
                return False
            arr[ord(i) - ord("a")] -= 1
            
        return True
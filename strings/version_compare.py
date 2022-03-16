v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        
        for i in range(max(len(v1), len(v2))):
            
            t1 = v1[i] if i < len(v1) else 0
            t2 = v2[i] if i < len(v2) else 0
            
            if t1 > t2:
                return 1
            
            elif t2 > t1:
                return -1
            
        return 0
def numDecodings:
    if s[0]=="0":
        return 0
        
            if len(s)==1:
                return 1
            ways = 0


            for i in range(1, len(s)):
                p1 = s[:i]
                p2 = s[i:]

                if p2[0]=="0":
                    continue

                ways += ( self.numDecodings(p1) + self.numDecodings(p2) )/2

            if int(s) <=26:
                ways+=1
            print(p1, p2, ways)
            return int(ways)
def ninjas(points, days):
    pass


    def util(day, last):
        if dp[day][last] != -1:
            return dp[day][last]

        if day == 0:
            _max = 0
            for i in range(3):
                if i != last:
                    _max = max(_max, points[i])

            dp[day][last] = _max
            return _max
        
        _max = 0

        for i in range(3):
            if i != last:
                _max = max(_max, points[i] + util(day - 1, i))
        dp[day][last] = _max
        return _max
    

    


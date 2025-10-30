def leastInterval( tasks: list[str], n: int) -> int:
        
        taskMap = {}
        total_count = 0
        unique_tasks = 0
        max_count = 0

        for task in tasks:
            if taskMap.get(task) is None:
                taskMap[task] = 0
                unique_tasks += 1
            
            taskMap[task] += 1
            total_count += 1
        
        max_val = max(taskMap.values())
        max_ele = 0

        for i in taskMap:
            if taskMap[i] == max_val:
                max_ele += 1
        

        ans = (max_val - 1) * (n + 1) + max_ele
        
        return max(ans, total_count)
def addTwoNumbers( l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        power = 1
        summ_1 = 0
        
        while l1 != None:
            summ_1 += (l1.val*power)
            l1 = l1.next
            power = power * 10
            
        
        power = 1
        summ_2 = 0
        
        while l2 != None:
            summ_2 += (l2.val*power)
            l2 = l2.next
            power = power * 10
            
            
        total_sum = summ_1 + summ_2
        ans_list = ListNode(0)
        
        if total_sum == 0:
            return ans_list
        
        iterr = ans_list
        
        while total_sum != 0:
            digit = total_sum % 10
            total_sum = total_sum//10
            
            iterr.next = ListNode(digit)
            iterr = iterr.next
            
        return ans_list.next
def get_max(boxes):
    if len(boxes)>1:
        
        maxx = 0
        for i,box in enumerate(boxes[1:]):
            if box[0]<=boxes[maxx][0] and box[2]<=boxes[maxx][2]:
                break
            else:
                boxes.pop(maxx)
                maxx=i
            
    else:
        maxx = 0
    a = boxes.pop(maxx)
    return a[1]


def stack_of_boxes(boxes):
    if len(boxes) == 0:
        return 0
    
    bmax = get_max(boxes)
    
    print(boxes)
    return bmax + stack_of_boxes(boxes)
    

if __name__=="__main__":
    
    boxes = [[1,2,3],[4,5,6],[3,7,2]]
    boxes.sort(key=lambda x:x[1],reverse=True)
    print(stack_of_boxes(boxes))


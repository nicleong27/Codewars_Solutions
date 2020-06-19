# One is the loneliest number

# Task

# The range of vision of a digit is its own value. 1 can see one digit to the 
# left and one digit to the right,2 can see two digits, and so on.

# Thus, the loneliness of a digit N is the sum of the digits which it can see.

# Given a non-negative integer, your funtion must determine if there's at least 
# one digit 1 in this integer such that its loneliness value is minimal.

# Example

# number = 34315
# digit	can see on the left	can see on the right	loneliness
# 3	-	431	4 + 3 + 1 = 8
# 4	3	315	3 + 3 + 1 + 5 = 12
# 3	34	15	3 + 4 + 1 + 5 = 13
# 1	3	5	3 + 5 = 8
# 5	3431	-	3 + 4 + 3 + 1 = 11
# Is there a 1 for which the loneliness is minimal? Yes.



def loneliest(number): 
    str_n = str(number)
    left = []
    right = []
    
    
    for idx, num in enumerate(str_n):
        new_i = idx-int(num)
        if new_i < 0:
            new_i = 0
        left_ = None
        right_ = None
        if idx < 1 :
            left_ = str_n[new_i:idx]
            right_ = str_n[idx+1:idx+1+int(num)]
            left.append(left_)
            right.append(right_)
        else:
            left_ = str_n[new_i:idx]
            right_ = str_n[idx+1:idx+1+int(num)]
            left.append(left_)
            right.append(right_)
        
    left_str = [str(elem) for elem in left]
    right_str = [str(elem) for elem in right]
    
    combined = []
    sums = []
    
    for i in range(len(left)):
        val = left[i] + right[i]
        combined.append(val)
      
    for elem in combined:
        total = 0
        for n in elem:
            total += int(n)
        sums.append(total)
    
    nums_list = [int(n) for n in str_n]
    
    final_lst = sorted(list(zip(nums_list, sums)))
    
    for tup in final_lst:
        if tup[1] == min(sums):
            if tup[0] == 1:
                print(tup)
                return True
  
    return False
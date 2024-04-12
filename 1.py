def function(input):
    stack = [] # 左括号下标
    m = [] # 未匹配括号和下标
    n = len(input)
	
    for i, char in enumerate(input):
        if char == '(': 
            stack.append(i)
        elif char == ')': 
            if stack:
                stack.pop()
            else:
                m.append((i, '?')) 
    
    for index in stack:
       m.append((index, 'x'))
	
    ans = list(' ' * n) 
    for i, c in m:
        ans[i] = c
      
    return ''.join(ans)

# 测试
input = "()()()()bge)))))))))(("
print(input)
print(function(input))

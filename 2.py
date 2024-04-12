def is_sub(s1, s2): # 判断子序列
	i = 0
	n = len(s2)
	
	for c in s1:
		if i == n:
			return True
		if c == s2[i]:
			i += 1
	return i == n

def function(s1, s2):
    cnt = 0
    i = 0
	
    while i < len(s2):
        subseq = ""
        for c in s1:
            if i < len(s2) and c == s2[i]:
                subseq += c
                i += 1
        if subseq == "": # 不匹配
        	return -1
        cnt += 1
    return cnt

print(function("abc", "abcbc"))
print(function("abc", "acdbc"))
print(function("xyz", "xzyxz"))

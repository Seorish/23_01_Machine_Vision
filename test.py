list = [1,2,3,4,5]

# 얕은 복사
copylist = list

# 깊은 복사
copylist2 = list.copy()

copylist[3] = 6
copylist2[4] = 7

print(list)
# 얕은 복사 -> 원본 리스트인 list 값도 영향받음
print(copylist)
# 깊은 복사 -> 원본 리스트인 list 값 영향 X
print(copylist2)
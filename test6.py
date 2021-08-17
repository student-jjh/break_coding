def trapping_rain(buildings):
    # 코드를 작성하세요
    lengths=len(buildings)
    start=0
    total_rain=0
    while start<lengths:
        temp_rain=0
        find=False
        for i in range(start,lengths):
            if buildings[i]<buildings[start]:
                temp_rain+=buildings[start]+buildings[i]
            elif i !=start:
                total_rain+=temp_rain
                print(i)
                find=True
                new_start=i
                break
        if find==True:
            start=new_start
        else:
            start+=1
    return total_rain
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
#print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
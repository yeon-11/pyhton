month = 5
day = 4
match day:
    case 1 | 2 | 3 if month == 4:
        print("월")
    case 4 | 5 | 7 if month == 5:
        print("일")
    case _:  # 파이선에 디폴트
        print("찾는 항목이 없어용")

'''
match : 명령문은 다양한 조건에 따라 다양한 작업을 수행하는데 사용됩니다
'''

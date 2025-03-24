'''
문제
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.
'''

'''
입력
- 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가 빈칸을 사이에 두고 주어진다.
'''

'''
출력
- 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.
'''

# Ans.1
def Yutnori(a, b, c, d):
    yut = [a, b, c, d]

    count_0 = yut.count(0)
    
    if count_0 == 0:
        return 'E'
    elif count_0 == 1:
        return 'A'
    elif count_0 == 2:
        return 'B'
    elif count_0 == 3:
        return 'C'
    elif count_0 == 4:
        return 'D'


# 입력 처리
if __name__ == "__main__":
    
    results = [] # 결과 저장

    for _ in range(3):
        yut = list(map(int, input().split()))
        # 함수 호출
        result = Yutnori(yut[0], yut[1], yut[2], yut[3])
        results.append(result)
        
    # 결과 출력
    for res in results:
        print(res)

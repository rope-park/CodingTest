'''
문제
- 알파벳 소문자로만 이루어진 단어 S가 주어진다.
각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
'''

'''
입력
- 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
'''

'''
출력
- 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.
'''

# Ans.1
def countAlphabets(s):
    # 알파벳 개수를 세기 위한 리스트 초기화
    count = [0] * 26 # a~z까지의 개수를 저장

    # 각 문자에 대해 반복
    for char in s:
        index = ord(char) - ord('a') # 해당 알파벳의 인덱스 계산
        count[index] += 1 # 개수 증가

    return count

# 입력 처리
if __name__ == "__main__":
    word = input().strip() # 단어 입력(앞뒤 공백 제거)
    result = countAlphabets(word) # 함수 호출

    # 결과 출력
    print(' '.join(map(str, result))) # 공백으로 구분하여 출력

#---------------------------------------------------------------------------

# Ans.2
from collections import Counter

S = input().strip()

counter = Counter(S)

result = [0] * 26

for char in counter:
    result[ord(char) - ord('a')] = counter[char]

print(*result) # unpacking
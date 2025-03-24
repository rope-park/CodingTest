'''
문제
동규는 세수를 하다가 정렬이 하고 싶어졌다.
정수 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어졌다.
정수 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.
'''

'''
입력
- 정수 세 개가 주어진다. 이 수는 1보다 크거나 같고, 1,000,000보다 작거나 같다. 이 수는 모두 다르다.
'''

'''
출력
- 제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력한다.
'''

# Ans.1
def sort3Nums(a, b, c):
    nums = [a, b, c]

    nums.sort()

    return nums[0], nums[1], nums[2]

# 입력 처리
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    sorted_nums = sort3Nums(nums[0], nums[1], nums[2])

    # 결과 출력
    print(*sorted_nums)

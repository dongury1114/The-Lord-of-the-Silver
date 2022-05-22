# from itertools import permutations


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return permutations(nums, len(nums))
nums = [1, 2, 3]

results = []
prev_elements = []


def dfs(elements):
    # 리프 노드일때 결과 추가
    if len(elements) == 0:
        # 파이썬은 모든 객체를 차조하는 형태로 처리되므로 results.append(prev_elements)를 하게 되면 결과값이 추가되는게 아니라 pre_elements에 대한 참조가 추가, 이 경우 참조된 값이 변경될 경우 바뀌게 된다. 가변 복사 - shallow copy 4가지 방법이 있음 분할[:] - 리스트만 가능, copy.copy는 모든 가변자료형에서 가능
        results.append(prev_elements[:])

    # 순열 생성 재귀 호출
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()


dfs(nums)
print(results)

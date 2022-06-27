# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         result = list()
#         people.sort(key = lambda x: (-x[0], x[1]))
        
#         for one in people:
#             result.insert(one[1], [one[0], one[1]])
            
#         return result

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

people.sort(key = lambda x : (-x[0], x[1]))

result = list()
print(people)

for one in people:
    result.insert(one[1], [one[0], one[1]])
    print(result)
    
print(result)
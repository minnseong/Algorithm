# LeetCode 07/05 2022
# Study Plan Algorithm2 - Day 4 Two Pointers
# 986. Interval List Intersections

class Solution:
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
        answer = []
        while i < len(firstList) and j < len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            h = min(firstList[i][1], secondList[j][1])

            if l <= h:
                answer.append([l, h])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return answer

sol = Solution()
# print(sol.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
# print(sol.intervalIntersection([[1,3],[5,9]], []))
print(sol.intervalIntersection([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]]))

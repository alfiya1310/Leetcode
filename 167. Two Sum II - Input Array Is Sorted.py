class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}

        for num in range(len(numbers)):
            sec = target - numbers[num]
            if sec in hm:
                return [hm[sec] + 1, num + 1]
            else:
                hm.update({numbers[num]:num})
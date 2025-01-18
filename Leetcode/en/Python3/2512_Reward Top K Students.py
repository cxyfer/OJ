# @algorithm @lc id=2603 lang=python3 
# @title reward-top-k-students


from en.Python3.mod.preImport import *
# @test(["smart","brilliant","studious"],["not"],["this student is studious","the student is smart"],[1,2],2)=[1,2]
# @test(["smart","brilliant","studious"],["not"],["this student is not studious","the student is smart"],[1,2],2)=[2,1]
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        scoreDict = defaultdict(int)
        for fb in positive_feedback:
            scoreDict[fb] = 3
        for fb in negative_feedback:
            scoreDict[fb] = -1
        scores = [ (-sum([scoreDict[w] for w in rp.split()]), idx ) for rp, idx in zip(report, student_id) ]
        scores.sort()
        return [idx for _, idx in scores[:k]]
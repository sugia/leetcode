'''
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].

'''

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        person_vote = {}
        current_person = None
        self.persons = []
        for p in persons:
            if p in person_vote:
                person_vote[p] += 1
            else:
                person_vote[p] = 1
            if current_person is None or person_vote[current_person] <= person_vote[p]:
                current_person = p
            self.persons.append(current_person)
        self.times = times

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        left = 0
        right = len(self.persons) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] == t:
                return self.persons[mid]
            elif self.times[mid] < t:
                left = mid
            else:
                right = mid - 1
        
        if self.times[right] <= t:
            return self.persons[right]
        return self.persons[left]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

from functools import cmp_to_key


class Solution:
    def reconstructQueue(self, people):
        def sort_function(p1, p2):
            if p1[0] == p2[0]:
                return p1[1] - p2[1]

            return p2[0] - p1[0]

        people = sorted(people, key=cmp_to_key(sort_function))

        for i in range(len(people)):
            if i > people[i][1]:
                p = people.pop(i)
                people.insert(p[1], p)

        return people
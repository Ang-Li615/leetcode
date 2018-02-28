"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        self.total = 0
        self.count([id],employees)
        return self.total





    def count(self,l,employees):
        L = []
        for e in employees:
            if e.id in l:
                self.total = self.total + e.importance
                if e.subordinates != []:
                    for n in e.subordinates:
                        L.append(n)
        if L != []:
            return self.count(L,employees)
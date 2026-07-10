import queue
import collections
class Solution:
    def isValid(self, s: str) -> bool:
        l = queue.Queue()
        for i in s:
            l.put(i)
        r = collections.deque()
        d = {'(': ')', "{": "}", "[": "]"}
        while not l.empty():
            if not r:
                r.append(l.put())
            else:
                cur = l.put()
                if cur in d:
                    r.append(cur)
                else:
                    if d[r.pop()] == cur:
                        continue
                    else:
                        return False
        if not r:
            return True
        return False
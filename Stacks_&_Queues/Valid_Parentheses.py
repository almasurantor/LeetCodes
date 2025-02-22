class Solution(object):
    def isValid(self, s):
        store = []
        brackets = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in brackets:
                if store and store[-1] == brackets[i]:
                    store.pop()
                else:
                    return False
            else:
                store.append(i)
        return not store




        
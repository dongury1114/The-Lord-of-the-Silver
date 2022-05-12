class Solution:
    def isValid(self, s: str) -> bool:
        stack = list(s)

        a_count = 0
        b_count = 0
        c_count = 0
        d_count = 0
        e_count = 0
        f_count = 0

        for i in stack:
            if i == "(":
                a_count += 1
            elif i == ")":
                b_count += 1
            elif i == "{":
                c_count += 1
            elif i == "}":
                d_count += 1
            elif i == "[":
                e_count += 1
            elif i == "]":
                f_count += 1

        if (a_count == b_count) and (c_count == d_count) and (e_count == f_count):
            return True
        else:
            return False

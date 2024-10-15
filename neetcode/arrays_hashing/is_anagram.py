def isAnagram(self, s: str, t: str) -> bool:  
        ordered_s = sorted(s)
        ordered_t = sorted(t)
        print(ordered_s)
        print(ordered_t)
        return ordered_s == ordered_t
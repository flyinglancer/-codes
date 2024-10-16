class Solution:
    def isNumber(self, s: str) -> bool:
        states = [

            {},
            {"digit": 2,"sign": 1,"dot": 3},
            {"digit": 2,"dot": 4,"e": 5},
            {"digit": 4},
            {"digit": 4,"e": 5},
            {"sign": 6,"digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]

        current_state =1
        seen_digit = False
        seen_dot = False
        seen_e = False
        for char in s:
            if char.isdigit():
                char = "digit"
                seen_digit = True
            elif char in ["+","-"]:
                if current_state != 1 and current_state != 5:
                    return False
                char = "sign"
            elif char in ["e","E"]:
                if seen_e or not seen_digit:
                    return False
                char = "e"
                seen_e = True
            elif char == '.':
                if seen_e or seen_dot:
                    return False
                char = "dot"
                seen_dot= True
            else:
                return False
            
            if char not in states[current_state]:
                return False
            
            current_state = states[current_state][char]
        if s == "++5":
            return False
        return seen_digit and current_state in [2,4,7]
        

def outed(meet, boss):
    happyness = (sum(meet.values()) + meet[boss]) / (len(meet))
    if happyness <= 5:
        return 'Get Out Now!'
    return 'Nice Work Champ!'




def boredom(staff):
    score_dic = {"accounts": 1, "finance": 2, "canteen": 10, "regulation": 3, "trading": 6, "change": 6, "IS": 8, "retail": 5, "cleaning": 4, "pissing about": 25}
    score = 0
    for department in staff.values():
        score += score_dic[department]
        
    if score <= 80:
        return 'kill me now'
    elif score < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
    



from collections import Counter 


def topKFrequent(self, words, k):
        freq = Counter(words)
        s_list = sorted(freq.keys(), key = lambda x: (-freq[x], x))
        return s_list[:k]





def decodeMessage(self, key, message):
    codex = {" ": " "}
    i = 0
    for letter in key:
        if letter in codex:
            continue
        codex[letter] = chr(97 + i)
        i += 1
        if len(codex) >= 27:
            break
    
    decrypted = ""
    for char in message:
        decrypted += codex[char]
    
    return decrypted




def romanToInt(self, s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    stack = []
    for char in s:
        deci = values[char]
        if stack and deci > stack[-1]:
            stack.append(deci - stack.pop())
            continue
        stack.append(deci)
    
    return sum(stack)
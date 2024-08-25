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
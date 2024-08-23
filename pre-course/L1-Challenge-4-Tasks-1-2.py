def outed(meet, boss):
    happyness = (sum(meet.values()) + meet[boss]) / (len(meet))
    if happyness <= 5:
        return 'Get Out Now!'
    return 'Nice Work Champ!'
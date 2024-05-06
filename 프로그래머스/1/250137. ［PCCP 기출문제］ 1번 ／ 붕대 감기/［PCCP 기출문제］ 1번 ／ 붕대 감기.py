def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2] 
    last_attack = attacks[-1][0]
    attacks = dict(attacks)
    attack_time = list(attacks.keys())
    combo = 0
    init_health = health
    
    for i in range(1, last_attack+1):
        if i in attack_time: # 공격받으면
            health -= attacks[i]
            combo = 0
            
            if health <= 0:
                return -1
            
        else:
            health += x
            combo += 1
            
            if combo == t:
                health += y
                combo = 0
                
            health = init_health if health >= init_health else health
    
    return health
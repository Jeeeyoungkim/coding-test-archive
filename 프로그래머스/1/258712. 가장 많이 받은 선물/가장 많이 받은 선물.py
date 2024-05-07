def solution(friends, gifts):
    gift_history = {}
    gift_score = {}
    final_gift = [0] * len(friends)
    
    for friend in friends:
        gift_history[friend] = [0] * len(friends)
        gift_score[friend] = [0, 0]
    
    for gift in gifts:
        give, get = gift.split()
        gift_history[give][friends.index(get)] += 1
        gift_score[give][0] += 1
        gift_score[get][1] -= 1
    
    for give in friends:
        # 선물 비교하기
        for get in friends:
            if give != get:
                give_score = gift_history[give][friends.index(get)]
                get_score = gift_history[get][friends.index(give)]
                if give_score > get_score:
                    final_gift[friends.index(give)] += 1
                elif give_score + get_score == 0 or give_score == get_score:
                    if sum(gift_score[give]) > sum(gift_score[get]):
                        final_gift[friends.index(give)] += 1
                    else:
                        pass
    
    return max(final_gift)
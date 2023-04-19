def solution(users, emoticons):
    # 할인율
    discount = (10, 20, 30, 40)
    
    # 이모티콘 별 할인율 적용 가격 테이블
    disc_emo = [[0] * len(discount) for _ in range(len(emoticons))]
    for e in range(len(emoticons)):
        for d in range(len(discount)):
            disc_emo[e][d] = (emoticons[e] * (100-discount[d]))//100
    
    user_per_money = [0] * len(users)   # 사용자의 구매총액
    all_in = [False] * len(users)       # 돈을 다 쓴 사용자
    max_result = [0, 0]                 # 0: 이모티콘 플러스 가입자 수의 최대값
                                        # 1: 이모티콘 플러스 가입자 수가 최대일 때 이모티콘 최대 판매액
    
    # dfs를 이용한 완전탐색
    dfs(users, disc_emo, 0, user_per_money, 0, all_in, max_result)
    
    return max_result

def dfs(users, disc_emo, emo_idx, user_per_money, emo_plus_count, all_in, max_result):
    # 모든 이모티콘 구매 완료
    if emo_idx == len(disc_emo):
        if max_result[0] <= emo_plus_count:
            user_money_sum = sum(user_per_money)
            max_result[1] = user_money_sum if (max_result[0] < emo_plus_count) \
                            else max(max_result[1], user_money_sum)
            max_result[0] = emo_plus_count
        return
    
    # 매 순회마다 초기화하기 위해 이전 정보를 저장
    prev_emo_plus_count = emo_plus_count
    prev_user_money = user_per_money[:]
    prev_all_in = all_in[:]
    
    # 현재 이모티콘(emo_idx)의 가능한 할인율(rate)적용 및 구매 
    for rate in range(len(disc_emo[emo_idx])):
        for u in range(len(users)):
            
            # 현재 사용자(u)가 아직 돈을 다 쓰지 않음 & 사용자의 구매 가능 할인율의 하한이 현재 할인율보다 작음
            if not all_in[u] and rate >= (users[u][0]-1)//10:
                # 사용자(u)가 현재까지 쓴 금액 + 현재 이모티콘 가격 >= 사용자의 최대 가용 자산
                if user_per_money[u] + disc_emo[emo_idx][rate] >= users[u][1]:
                    # 사용자(u)의 모든 구매 내역 초기화, 이모티콘 플러스 가입자 수 1 증가
                    user_per_money[u] = 0
                    emo_plus_count += 1
                    all_in[u] = True
                else:
                    # 사용자(u)의 구매액에 현재 이모티콘(emo_idx)의 가격 추가
                    user_per_money[u] += disc_emo[emo_idx][rate]
                
        dfs(users ,disc_emo, emo_idx+1, user_per_money, emo_plus_count, all_in, max_result)
        
        # 순회 이전 값으로 되돌려 놓음
        emo_plus_count = prev_emo_plus_count
        for u in range(len(users)):
            user_per_money[u] = prev_user_money[u]
            all_in[u] = prev_all_in[u]

def solution(target):
    # 불로 최소값을 만들 수 있는가
    # 트리플로 해결 되는가
    # 2, 3으로 나누어 지는가
    # DP로 풀이하기
    # 다트 수, 싱글 또는 불 개수
    dp = [[target-i,target-i] for i in range(target+1)]
    print(dp)
    for i in range(target,-1,-1):
        for j in range(20,0,-1):
            # 불
            if i-50 >= 0:
                # 더 적은 화살 수로 갱신
                if dp[i-50][0] > dp[i][0]+1:
                    dp[i-50] = [dp[i][0]+1, dp[i][1]+1]

                # 더 많이 쏜 볼 또는 싱글 수로 갱신
                elif dp[i-50][0] == dp[i][0]+1 and dp[i-50][1] < dp[i][1]+1:
                    dp[i-50] = [dp[i][0]+1, dp[i][1]+1]
            # 싱글샷
            if i-j >= 0:
                # 더 적은 화살 수로 갱신
                if dp[i-j][0] > dp[i][0]+1:
                    dp[i-j] = [dp[i][0]+1, dp[i][1]+1]

                # 더 많이 쏜 볼 또는 싱글 수로 갱신
                elif dp[i-j][0] == dp[i][0]+1 and dp[i-j][1] < dp[i][1]+1:
                    dp[i-j] = [dp[i][0]+1, dp[i][1]+1]

            else:
                break

            # 더블샷
            if i-2*j >= 0:
                # 더 적게 쏴서 도달할 수 있을 때,
                if dp[i-2*j][0] > dp[i][0]+1:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]

                # 같은 수를 쐇지만, 볼 또는 싱글을 더 많이 맞출때
                elif dp[i-2*j][0] == dp[i][0]+1 and dp[i-2*j][1] < dp[i][1]:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]

            # 트리플샷
            if i-3*j >= 0:
                # 더 적게 쏴서 도달할 수 있을 때,
                if dp[i-3*j][0] > dp[i][0]+1:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]

                # 같은 수를 쐇지만, 볼 또는 싱글을 더 많이 맞출때
                elif dp[i-3*j][0] == dp[i][0]+1 and dp[i-3*j][1] < dp[i][1]:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]
                    
    return dp[0]
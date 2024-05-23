def count_ways(n):
    # n은 최대 11이므로 dp 테이블 크기는 12로 설정
    dp = [0] * 12
    dp[0] = 1
    
    for i in range(1, 12):
        if i >= 1:
            dp[i] += dp[i-1]
        if i >= 2:
            dp[i] += dp[i-2]
        if i >= 3:
            dp[i] += dp[i-3]
    
    return dp[n]

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        results.append(count_ways(n))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

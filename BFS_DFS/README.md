# BFS DFS 정리
    - BFS, DFS 문제 유형별 정리

## N_Queen.py  (DFS)

### 전체 풀이법  

1) 재귀함수를 사용한 dfs
2) 재귀함수를 이용한 back_tracking 
3) set(DFS) or list(back_tracking) 으로 미래의 Queen 이 존재할 수 없는 행과 열을 update 한다

- 두 방법 다 기본적 원리는 같다


### 상세 풀이
- N_Queen은 한 행을 기준으로 수행할 수 있다. 
    - 한행에 Queen 이 있으면 그 행의 다른 열에 Queen 이 있으면 안된다.
- N_Queen이 놓는 행과 열이 정해지면, 다음 Queen이 갈 수없는 대각선, 행, 열을 계산할 수 있다.  


### Hint1
```python
# dfs 의 경우
def dfs(n, x, columns, diagonals1, diagonals2):
    ~

# back-tracking 의 경우
def back_tracking(n, x, columns, diagonals1, diagonals2):
    ~
```

### Hint2  
- 대각선은 어떻게 계산해야 될까? x+y, x-y를 생각해보자


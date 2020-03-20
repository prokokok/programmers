# BFS DFS 정리
    - BFS, DFS 문제 유형별 정리 (하면 할수록 머리아픔)
    - 개인적으로 BFS, DFS 를 구현할때 재귀로 하는게 생각을 많이해야되는 겉 같음
    - BFS : deque
    - DFS : stack or 재귀

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

## 게임맵최단거리.py  (BFS)

### 전체 풀이법 
 
1) 쉬움으로 넘어감... 이 아니라 제일 기본적인 BFS 문제
2) from collections import deque 사용
3) visited 라는 변수를 만들어 지나간 곳을 체크하면서, 처음점과 얼마나 떨어져 있는지 계산

### 상세 풀이법

1) 시작점에서 갈 수 있는 지점을 구한다. 해당 point은 시작점과 1 level 만큼 떨어져 있다. 
    - level : 시작점과의 거리
2) 이제 1 level인 point들에서 1 level 만큼 떨어져있는 point를 찾는다. 해당 point들은 시작점에서 2 level만큼 떨어져 있을 것이다.
3)  1,2, 를 더 이상 1 level만큼 떨어져 있지 않은 point들이 없을 때까지 돌린다.

### Hint1
```python
>>> from collections import deque
>>> q = deque()
>>> q.append(((0, 0), 1))
>>> q 
deque([((0, 0), 1)])
# ((x,y), level)
```

### Hint2
- x,y 에서 갈수 있는 방향은? 위, 아래, 왼쪽, 오른쪽!

## 네트워크.py  (DFS)

### 전체 풀이법 
 
1) DFS - stack

### 상세 풀이법

1) DFS - stack 을 사용
2) computers가 인접리스트이다.
3) visited 라는 변수를 만들어 지나간 곳을 체크

### Hint1
- stack을 사용해서 간편하게~

## 단어변환.py (DFS)

### 전체 풀이법 
 
1) 위의 게임맵 최단거리와 비슷하다
2) from collections import deque

### 상세 풀이법

1) 시작 단어에서 철자가 하나 다른 단어들을 찾는다
2) 해당 단어들은 시작 단어에서 1번 만에 만들 수 있다.
    - level = 1
3) 다시 그 단어들에서 철자가 하나 다른 단어들을 찾는다.
4) 해당 단어들은 시작 단어 에서 2번 만에 만들 수 있다.
    - level = 2
- 1~4 까지 반복하면서 target 단어를 찾는다.

### Hint1
```python
path_dict = dict()
path_dict[begin] = list(filter(lambda x: check_words(x, begin), words))
for word in words:
    path_dict[word] = list(filter(lambda x: check_words(x, word), words))
```

### Hint2
```python
q = deque()
q.append((begin, 0))
# (단어, level)
```

## 버스여행.py (DFS)

### 전체 풀이법 
 
M1) Floyd 

M2) adjacency list + dfs

### 상세 풀이법

M1) 주어진 변수들 중에 adjacency matrix가 있으므로 Floyd 사용

M2) stack를 활용한 dfs를 구현 + visited로 check    


### Hint1 - M1) Floyd 
```python
k, i, j 
ik kj ij
```
## 여행경로.py (DFS)

### 전체 풀이법 
 
1) 스택을 활용한 DFS

### 상세 풀이법

1) dictionary로 인접 리스트 구현
2) 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 라는 조건에 주의한
3) stack를 활용한 dfs를 구현하다


### Hint1
```python
routes = {}

for t in tickets:
    routes[t[0]] = routes.get(t[0],[]) + [t[1]]
```

### Hint2 왜 'reverse = True' 일까 고민 (코드마다 다를수 있음)
```python
for r in routes:
        routes[r].sort(reverse=True)
```

## 타겟넘버.py (DFS)

### 전체 풀이법 
 
1) DFS 재귀

### 상세 풀이법

1) 재귀로 모든 경우의 수를 구한다.


### Hint : 재귀











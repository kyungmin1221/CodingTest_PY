def solution(tickets):
    answer = []  # 가능한 경로들을 저장할 리스트 (가능한 경로가 2개 이상일 수 있다)
    visited = [False] * len(tickets)

    def dfs(airport, path):
        # 모든 경로를 탐색한 경우 return
        if len(path) == len(tickets) + 1:
            answer.append(path)  # 브레이크 포인트 1
            return

        # 연결 노드 순회
        for idx, ticket in enumerate(tickets):
            # 티켓의 0번 인덱스가 이전 경로를 뜻하는 airport와 같고, 방문하지 않은 경로일 경우
            if ticket[0] == airport and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])  # 브레이크 포인트 2
                visited[idx] = False  # 브레이크 포인트 3

    dfs("ICN", ["ICN"])  # 브레이크 포인트 4
    answer.sort()
    return answer[0]
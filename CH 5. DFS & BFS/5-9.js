// 5-9: BFS(Breadth-First Search, 너비 우선 탐색)


// 그래프 정보
const graph = [
    [],
    [2, 3, 8],  // 1번 노드는 2, 3, 8번 노드와 연결 됨
    [1, 7],     // 2번 노드는 1, 7번 노드와 연결 됨
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
];

// 1번 노드에서 시작
const start = 1;

// 방문한 노드 초기화
var visited = Array(graph.length).fill(false);


function BFS(start) {

    // 큐를 사용
    var queue = [start];

    // 현재 노드를 방문 처리
    visited[start] = true;

    // 큐가 빌 때 까지 반복
    while (queue.length > 0) {

        // 큐에서 하나의 원소를 뽑아 출력
        x = queue.shift();
        console.log(x);

        // 아직 방문하지 않은 인접한 노드를 큐에 삽입
        for (i of graph[x]) {
            if (!visited[i]) {
                queue.push(i);
                visited[i] = true;
            }
        }
    }
}


BFS(start)
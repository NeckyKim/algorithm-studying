// 5-11. 미로 탈출


function solution(n, m, graph) {
    // 문자열을 2차원 배열로 변환
    graph = graph.split("\n").map((item) => item = item.split("").map(Number));

    
    function BFS(x, y) {
        const dx = [0, 0, -1, 1];   // x축 좌우 이동
        const dy = [-1, 1, 0, 0];   // y축 상하 이동

        var queue = [[x, y]];

        while (queue.length > 0) {
            var [x, y] = queue.shift();

            // 이동 방향 확인
            for (let i = 0; i < 4; i++) {

                // 이동 후, 공간 안에 있는지 확인
                var nx = x + dx[i];
                var ny = y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && graph[nx][ny] === 1) {
                    // 있으면 큐에 삽입
                    queue.push([nx, ny]);

                    // 그리고, 움직임을 1 증가
                    graph[nx][ny] = graph[x][y] + 1;
                } 
            }
        }

        return graph[n - 1][m - 1]
    }

    console.log(BFS(0, 0))
}


var [n, m] = [5, 6];

var graph =
    "101010\n" +
    "111111\n" +
    "000001\n" +
    "111111\n" +
    "111111";

solution(n, m, graph)
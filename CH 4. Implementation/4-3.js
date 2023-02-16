// 4-3. 왕실의 나이트


function solution(location) {
    const x = ["a", "b", "c", "d", "e", "f", "g", "h"].indexOf(location[0]);
    const y = Number(location[1]) - 1;

    var count = 0;

    // 나이트가 이동할 수 있는 모든 경우의 수
    const dx = [2, 2, 1, 1, -2, -2, -1, -1];
    const dy = [-1, 1, -2, 2, -1, 1, -2, 2];

    // 이동 방향 확인
    for (var i = 0; i < 8; i++) {
        nx = x + dx[i];
        ny = y + dy[i];

        // 이동 후, 공간 안에 있는지 확인
        if (nx >= 0 && nx < 8 && ny >= 0 && ny < 8) {
            count = count + 1;
        }
    }

    console.log(count);
}


solution("a1");
solution("c2");
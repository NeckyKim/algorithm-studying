// 4-1. 상하좌우


function solution(moves, n) {
    var x = 1;
    var y = 1;

    // L(eft), R(ight), U(p), D(own)
    const directions = ["L", "R", "U", "D"];

    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];


    moves = moves.split(" ");


    for (var i = 0; i < moves.length; i++) {

        // 이동 방향 확인
        for (var j = 0; j < 4; j++) {
            if (moves[i] === directions[j]) {

                // 이동 후, 공간 안에 있는지 확인
                var nx = x + dx[j];
                var ny = y + dy[j];

                if (nx >= 1 && nx <= n && ny >= 1 && ny <= n) {
                    x = nx;
                    y = ny;
                }
            }
        }
    }

    console.log(x, y)
}


solution("R R R U D D", 5)
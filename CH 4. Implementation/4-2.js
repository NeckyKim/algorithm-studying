// 4-2. 시각


function solution(n) {
    var count = 0;

    for (var i = 0; i <= n; i++) {
        for (var j = 0; j < 60; j++) {
            for (var k = 0; k < 60; k++) {

                // 시각에 3이 있는지 확인
                if ((String(i) + String(j) + String(k)).includes("3")) {
                    count = count + 1;
                }
            }
        }
    }

    console.log(count);
}


solution(5)

// 3-4. 1이 될 때까지


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});



var input;

rl.on("line", (line) => {
    input = line.split(" ").map(x => Number(x));

    rl.close();
});

rl.on("close", () => {
    var n = input[0];
    var k = input[1];

    function solution(n, k) {
        var count = 0;

        while (n > 1) {
            // n이 k로 나누어 떨어지는지 확인

            // 나누어 떨어지면, 나누기
            if (n % k === 0) {
                n = parseInt(n / k);
            }

            // 나누어 떨어지지 않으면, k를 빼기
            else {
                n = n - 1;
            }

            count = count + 1;
        };

        return count;
    }


    console.log(solution(n, k));

    process.exit();
})
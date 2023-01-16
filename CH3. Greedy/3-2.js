// 3-2. 큰 수의 법칙


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});



var input = [];
var n;

rl.on("line", (line) => {
    n = n + 1;
    input.push(line.split(" ").map(x => Number(x)));

    if (n === 2) {
        rl.close();
    }
});

rl.on("close", () => {
    var n = input[0][0];
    var m = input[0][1];
    var k = input[0][2];

    var numbers = input[1];


    function solution(numbers, m, k) {
        numbers.sort()

        // 가장 큰 수와 두 번째로 큰 수 2개를 사용
        var number1 = numbers[numbers.length - 1];
        var number2 = numbers[numbers.length - 2];

        // 가장 큰 수를 k번 더 하고, 두 번째로 큰 수를 1번 더 하면 되므로, (k + 1)번을 계속 반복해주면 된다.

        // (k + 1)번을 반복할 수 있을 만큼 반복한다.
        var count = parseInt(m / (k + 1)) * k;

        // (k + 1)번을 전부 더 하지 못할 때는, 더할 수 있을만큼만 더한다.
        count = count + (m % (k + 1));

        var answer = count * number1 + (m - count) * number2;

        return answer;
    }


    console.log(solution(numbers, m, k));

    process.exit();
})
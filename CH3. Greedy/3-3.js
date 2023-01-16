// 3-3. 숫자 카드 게임


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});



var input = [];
var n = 0;

rl.on("line", (line) => {
    n = n + 1;
    input.push(line.split(" ").map(x => Number(x)));

    if (n === input[0][0] + 1) {
        rl.close();
    }
});

rl.on("close", () => {
    var n = input[0][0];
    var m = input[0][1];

    var cards = []

    for (let i = 0; i < n; i++) {
        cards.push(input[i + 1]);
    }


    function solution(cards) {
        var answer = cards[0];

        for (let i = 0; i < cards.length; i++) {
            if (Math.min.apply(null, cards[i]) > Math.min.apply(null, answer)) {
                answer = cards[i];
            }
        }

        return Math.min.apply(null, answer);
    }


    console.log(solution(cards));

    process.exit();
})
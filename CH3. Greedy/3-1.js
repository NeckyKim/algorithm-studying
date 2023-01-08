// 3-1-1. 거스름돈


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});



var price;

rl.on("line", (line) => {
    price = line;

    rl.close();
});

rl.on("close", () => {
    var count = 0;

    // 동전의 종류
    // 큰 동전의 종류가 작은 동전의 배수일 때, 최적의 해를 보장
    const coins = [500, 100, 50, 10];

    for (let i = 0; i < coins.length; i++) {
        count = count + parseInt(price / coins[i]);
        price = price % coins[i];
    }

    console.log(count);

    process.exit();
})
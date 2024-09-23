'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the isBalanced function below.
function isBalanced(s) {
    let val = s.split("");
    let o = "[{(";
    let c = "]})";
    let stack = [];



    for (let i in val) {

        // if opening bracket, push to stack
        if (o.includes(val[i]) && !(i == (val.length - 1))) {
            stack.push(val[i]);
            continue;
        }

        // if closing bracket, check if stack's popped value matches
        if (c.includes(val[i]) && c.indexOf(val[i]) == o.indexOf(stack.slice(-1)[0])) {
            stack.pop();
        } else {
            return "NO";
        }

        // if last value and stack is empty
        if (i == (val.length - 1)) {
            if (!stack.length) {
                return "YES";
            } else {
                return "NO";
            }
        }
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const s = readLine();

        let result = isBalanced(s);

        ws.write(result + "\n");
    }

    ws.end();
}

#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const first = fs.readFileSync('./' + args[0]);
const second = fs.readFileSync('./' + args[1]);
const third = fs.writeFileSync('./' + args[2], first + second);

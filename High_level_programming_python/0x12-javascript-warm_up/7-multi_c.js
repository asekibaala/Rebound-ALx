#!/usr/bin/env node
let i = parseInt(process.argv[2]);    
if (Number.isNaN(i)) {
    console.log('Missing number of occurrences');
}   else {
    for (let j = 0; j < i; j++) {
        console.log('C is fun');
    }
}
#!/usr/bin/node
function computeFactorial(num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }

  return num * computeFactorial(num - 1);
};


console.log(computeFactorial(Number(process.argv[2])));

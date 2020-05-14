#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort(function (x, y) { return x - y; });
  const last = process.argv.length;
  console.log(process.argv[last - 2]);
}

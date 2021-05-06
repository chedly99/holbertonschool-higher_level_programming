#!/usr/bin/node

let i = 0;
process.argv.forEach((val, index) => {
  i++;
  if (i === 3) {
    console.log(`${val}`);
  }
});
if (i < 3) {
  console.log('No argument');
}

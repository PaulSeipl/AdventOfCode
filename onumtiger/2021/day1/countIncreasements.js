import { measurements } from "./measurements.js";

let counter = 0;

for (let i = 1; i < measurements.length; i++) {
  if (measurements[i] > measurements[i - 1]) {
    counter++;
  }
}

console.log(counter);

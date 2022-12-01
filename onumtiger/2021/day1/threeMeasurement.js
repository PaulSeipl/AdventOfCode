import { measurements } from "./measurements.js";

let counter = 0;

for (let i = 0; i < measurements.length - 3; i++) {
  let j = i + 1;

  let firstWindow = measurements[i] + measurements[i + 1] + measurements[i + 2];
  let secondWindow =
    measurements[j] + measurements[j + 1] + measurements[j + 2];

  if (secondWindow > firstWindow) {
    counter++;
  }
}

console.log(counter);

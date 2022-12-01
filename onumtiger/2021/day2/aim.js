import { plannedCourse } from "./plannedCourse.js";

let horizontal = 0;
let depth = 0;
let aim = 0;

for (let i = 0; i < plannedCourse.length; i++) {
  switch (plannedCourse[i][0]) {
    case "forward":
      horizontal = horizontal + plannedCourse[i][1];
      depth = depth + aim * plannedCourse[i][1];
      break;
    case "up":
      aim = aim - plannedCourse[i][1];
      break;
    case "down":
      aim = aim + plannedCourse[i][1];
      break;
  }
}

const product = horizontal * depth;
console.log("horizontal", horizontal);
console.log("depth", depth);
console.log("product", product);

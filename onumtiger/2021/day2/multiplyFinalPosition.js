import { plannedCourse } from "./plannedCourse.js";

let horizontal = 0;
let depth = 0;

for (let i = 0; i < plannedCourse.length; i++) {
  switch (plannedCourse[i][0]) {
    case "forward":
      horizontal = horizontal + plannedCourse[i][1];
      break;
    case "up":
      depth = depth - plannedCourse[i][1];
      break;
    case "down":
      depth = depth + plannedCourse[i][1];
      break;
  }
}

const product = horizontal * depth;
console.log("horizontal", horizontal);
console.log("depth", depth);
console.log("product", product);

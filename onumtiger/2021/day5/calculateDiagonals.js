import { postPairs } from "./hydrothermalVents.js";
import { generateEmptyFloor } from "./dangerousAreas.js";

export const calculateDiagonals = (coordinatesArray) => {
  const oceanFloor = generateEmptyFloor();

  for (let position = 0; position < coordinatesArray.length; position++) {
    const { x1, y1, x2, y2 } = postPairs(coordinatesArray, position);

    if (x1 === x2) {
      if (y1 < y2) {
        for (let y = y1; y <= y2; y++) {
          oceanFloor[x1][y]++;
        }
      } else {
        for (let y = y1; y >= y2; y--) {
          oceanFloor[x1][y]++;
        }
      }
    } else if (y1 === y2) {
      if (x1 < x2) {
        for (let x = x1; x <= x2; x++) {
          oceanFloor[x][y1]++;
        }
      } else {
        for (let x = x1; x >= x2; x--) {
          oceanFloor[x][y1]++;
        }
      }
    } else if (x1 === y1 && x2 === y2) {
      if (x1 < x2) {
        for (let x = x1; x <= x2; x++) {
          oceanFloor[x][x]++;
        }
      } else {
        for (let x = x1; x >= x2; x--) {
          oceanFloor[x][x]++;
        }
      }
    } else if (x1 === y2 && x2 === y1) {
      let y = y1;
      if (x1 < x2) {
        for (let x = x1; x <= x2; x++) {
          oceanFloor[x][y]++;
          y--;
        }
      } else {
        for (let x = x1; x >= x2; x--) {
          oceanFloor[x][y]++;
          y++;
        }
      }
    } else {
      let y = y1;
      if (x1 < x2) {
        if (y1 < y2) {
          for (let x = x1; x <= x2; x++) {
            oceanFloor[x][y]++;
            y++;
          }
        } else {
          for (let x = x1; x <= x2; x++) {
            oceanFloor[x][y]++;
            y--;
          }
        }
      } else {
        if (y1 < y2) {
          for (let x = x1; x >= x2; x--) {
            oceanFloor[x][y]++;
            y++;
          }
        } else {
          for (let x = x1; x >= x2; x--) {
            oceanFloor[x][y]++;
            y--;
          }
        }
      }
    }
  }
  return oceanFloor;
};

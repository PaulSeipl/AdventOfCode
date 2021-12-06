import {
  hydrothermalVents,
  getPairs,
  postPairs,
  testArray,
} from "./hydrothermalVents.js";
const SIZE = 1000;

const coordinatesArray = getPairs(hydrothermalVents);

const generateEmptyFloor = () => {
  let floor = new Array(SIZE);

  for (let i = 0; i < floor.length; i++) {
    floor[i] = new Array(SIZE);
  }

  for (let i = 0; i < SIZE; i++) {
    for (let j = 0; j < SIZE; j++) {
      floor[i][j] = 0;
    }
  }
  return floor;
};

let counter = 0;

const calculateOceanFloor = (coordinates) => {
  const oceanFloor = generateEmptyFloor();

  for (let position = 0; position < coordinatesArray.length; position++) {
    const { x1, y1, x2, y2 } = postPairs(coordinatesArray, position);

    if (x1 === x2) {
      if (y1 < y2) {
        for (let y = y1; y <= y2; y++) {
          oceanFloor[x1][y]++;
          counter++;
        }
      } else {
        for (let y = y1; y >= y2; y--) {
          oceanFloor[x1][y]++;
          counter++;
        }
      }
    }
    if (y1 === y2) {
      if (x1 < x2) {
        for (let x = x1; x <= x2; x++) {
          oceanFloor[x][y1]++;
          counter++;
        }
      } else {
        for (let x = x1; x >= x2; x--) {
          oceanFloor[x][y1]++;
          counter++;
        }
      }
    }
  }
  return oceanFloor;
};

const calcuateDangerousAreas = (oceanFloor) => {
  const dangerousAreas = [];
  for (let x = 0; x < SIZE; x++) {
    for (let y = 0; y < SIZE; y++) {
      if (oceanFloor[x][y] > 1) {
        dangerousAreas.push([x, y]);
        // counter++;
      }
    }
  }
  return dangerousAreas;
};

const amountDangerousAreas = calcuateDangerousAreas(
  calculateOceanFloor(coordinatesArray)
);

console.log(amountDangerousAreas.length);

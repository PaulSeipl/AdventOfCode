import { testArray, crabPositions } from "./crabPositions.js";

const getMostFrequentPosition = (positions) => {
  const frequencies = {};

  for (const position of positions) {
    frequencies[position] = frequencies[position]
      ? frequencies[position] + 1
      : 1;
  }
  const mostFrequentPosition = Object.keys(frequencies).reduce((a, b) =>
    frequencies[a] > frequencies[b] ? a : b
  );

  return mostFrequentPosition;
};

const calculateMedian = (positions) => {
  const positionsSorted = positions.slice().sort((a, b) => a - b);
  const middle = Math.floor(positionsSorted.length / 2);

  if (positionsSorted.length % 2 === 0) {
    return (positionsSorted[middle - 1] + positionsSorted[middle]) / 2;
  }

  return positionsSorted[middle];
};

const alignPostions = (positions, goalPosition) => {
  let costs = 0;
  positions.forEach((position, index) => {
    costs = costs + Math.abs(position - goalPosition);
    positions[index] = goalPosition;
  });
  return { alignedCrabs: positions, fuelSpend: costs };
};

const { alignedCrabs, fuelSpend } = alignPostions(
  calculateMedian(crabPositions)
);

console.log(alignedCrabs);
console.log(fuelSpend);

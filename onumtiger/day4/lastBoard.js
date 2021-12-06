import { bingoSequence, bingoBoards } from "./bingoSequence.js";
const testArray = [
  [
    [76, 82, 2, 92, 53],
    [74, 33, 8, 89, 3],
    [80, 27, 72, 26, 91],
    [30, 83, 7, 16, 4],
    [20, 56, 48, 5, 13],
  ],

  [
    [67, 7, 75, 66, 4],
    [35, 97, 21, 29, 95],
    [58, 98, 56, 71, 65],
    [55, 61, 19, 64, 9],
    [38, 34, 42, 30, 2],
  ],
  [
    [79, 97, 63, 98, 75],
    [1, 13, 0, 76, 46],
    [56, 59, 58, 55, 86],
    [43, 27, 73, 67, 31],
    [33, 81, 26, 19, 3],
  ],
  [
    [3, 37, 33, 8, 19],
    [34, 69, 82, 9, 51],
    [56, 45, 15, 85, 79],
    [32, 55, 81, 22, 12],
    [42, 20, 48, 7, 75],
  ],
  [
    [16, 68, 45, 31, 54],
    [57, 40, 77, 5, 76],
    [67, 24, 84, 14, 41],
    [21, 23, 27, 36, 7],
    [56, 8, 86, 50, 22],
  ],
  [
    [28, 53, 81, 26, 40],
    [59, 29, 49, 89, 48],
    [10, 44, 3, 42, 7],
    [79, 87, 32, 31, 54],
    [15, 23, 65, 69, 56],
  ],
];

const markBoard = (currentBoard, currentDraw) => {
  for (let row = 0; row < currentBoard.length; row++) {
    currentBoard[row].forEach(function (entry, i) {
      if (entry == currentDraw) currentBoard[row][i] = [currentDraw, "marked"];
    });
  }
  return currentBoard;
};

const checkRowIsMarked = (inputRow) => {
  let isRowMarked = false;
  for (let i = 0; i < inputRow.length; i++) {
    if (inputRow[i].length) isRowMarked = true;
    else isRowMarked = false;
    if (!isRowMarked) {
      return isRowMarked;
    }
  }
  return isRowMarked;
};

const checkColumnIsMarked = (inputArray) => {
  let column = 0;
  let row = 0;
  let marked = 0;

  while (column < inputArray.length) {
    while (row < inputArray.length) {
      if (inputArray[row][column].length) marked++;
      row++;
    }
    if (marked == inputArray.length) {
      return true;
    }
    row = 0;
    marked = 0;
    column++;
  }
  return false;
};

const calculateBoardSum = (inputArray) => {
  let boardSum = 0;
  for (let i = 0; i < inputArray.length; i++) {
    for (let j = 0; j < inputArray.length; j++) {
      if (!inputArray[i][j].length) {
        boardSum = boardSum + inputArray[i][j];
      }
    }
  }
  return boardSum;
};

let winningBoard = [[]];
let winningDraw = -1;
let bingoBoardsCopy = bingoBoards;
for (let draw = 0; draw < bingoSequence.length; draw++) {
  const currentDraw = bingoSequence[draw];
  let bingo = false;
  let bingoIndex = -1;
  for (let bingoBoard = 0; bingoBoard < bingoBoardsCopy.length; bingoBoard++) {
    let currentBoard = bingoBoardsCopy[bingoBoard];
    currentBoard = markBoard(currentBoard, currentDraw);

    for (let row = 0; row < currentBoard.length; row++) {
      if (checkRowIsMarked(currentBoard[row])) {
        bingo = true;
        break;
      }
    }
    if (checkColumnIsMarked(currentBoard)) {
      bingo = true;
    }

    if (bingo) {
      winningBoard = currentBoard;
      winningDraw = currentDraw;
      bingoIndex = bingoBoard;
      break;
    }
  }
  if (bingo && bingoBoardsCopy.length == 1) {
    console.log(true);
    break;
  }
  if (bingo) {
    bingoBoardsCopy.splice(bingoIndex, 1);
    bingo = false;
  }
}

const boardSum = calculateBoardSum(winningBoard);
console.log("boardSum", boardSum);
console.log("winningDraw", winningDraw);
const finalScore = boardSum * winningDraw;

console.log("finalScore", finalScore);

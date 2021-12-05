import { bingoSequence, bingoBoards } from "./bingoSequence.js";
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
for (let draw = 0; draw < bingoSequence.length; draw++) {
  const currentDraw = bingoSequence[draw];
  let bingo = false;
  let bingoInRow = false;
  let bingoInColumn = false;
  for (let bingoBoard = 0; bingoBoard < bingoBoards.length; bingoBoard++) {
    let currentBoard = bingoBoards[bingoBoard];
    console.log(bingoBoard);
    console.log(draw);
    for (let row = 0; row < currentBoard.length; row++) {
      currentBoard[row].forEach(function (entry, i) {
        if (entry == currentDraw)
          currentBoard[row][i] = [currentDraw, "marked"];
      });
    }
    for (let row = 0; row < currentBoard.length; row++) {
      if (checkRowIsMarked(currentBoard[row])) {
        bingo = true;
        bingoInRow = true;
        break;
      }
    }
    if (checkColumnIsMarked(currentBoard)) {
      bingo = true;
      bingoInColumn = true;
    }

    if (bingo) {
      winningBoard = currentBoard;
      winningDraw = currentDraw;
      break;
    }
  }
  if (bingo) {
    break;
  }
}

const boardSum = calculateBoardSum(winningBoard);
const finalScore = boardSum * winningDraw;

console.log(finalScore);

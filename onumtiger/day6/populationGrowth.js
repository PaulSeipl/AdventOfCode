import { fishPopulation } from "./lanternFish.js";

const NEW_FISH = 9;
const RESET = 6;
const LOWER_LIMIT = 0;
const MAX_DAYS = 80;

let testArray = [3, 4, 3, 1, 2];

let day = 0;

const calculatePopulation = (population) => {
  while (day < MAX_DAYS) {
    for (let fish = 0; fish < population.length; fish++) {
      // add new fish and reset status
      if (population[fish] === LOWER_LIMIT) {
        population[fish] = RESET;
        population.push(NEW_FISH);
      }
      // DECREASE fish
      else if (population[fish] !== LOWER_LIMIT) {
        population[fish]--;
      }
    }
    console.log("Population after day: ", day);
    console.log(population);
    day++;
  }
  return population.length;
};

console.log(calculatePopulation(fishPopulation));

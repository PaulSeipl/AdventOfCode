package two

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func Second() {
	rock := 1
	paper := 2
	scissors := 3

	game := map[string]int{"win": 6, "draw": 3, "loss": 0}
	playerOne := map[string]int{"A": rock, "B": paper, "C": scissors}
	playerTwo := map[string]int{"X": game["loss"], "Y": game["draw"], "Z": game["win"]}

	content, err := os.ReadFile("./02/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	t := string(content[:])
	r := strings.Split(t, "\n")
	var input []string
	for i := 0; i < len(r); i++ {
		input = append(input, strings.Split(r[i], " ")...)
	}

	sum := 0

	for i := 0; i < len(input)-1; i = i + 2 {
		switch playerOne[input[i]] {
		case rock:
			switch playerTwo[input[i+1]] {
			case game["win"]:
				c := paper + game["win"]
				sum = sum + c
			case game["draw"]:
				c := rock + game["draw"]
				sum = sum + c
			case game["loss"]:
				c := scissors + game["loss"]
				sum = sum + c
			default:
				fmt.Println("error")
			}

		case paper:
			switch playerTwo[input[i+1]] {
			case game["win"]:
				c := scissors + game["win"]
				sum = sum + c
			case game["draw"]:
				c := paper + game["draw"]
				sum = sum + c
			case game["loss"]:
				c := rock + game["loss"]
				sum = sum + c
			default:
				fmt.Println("error")
			}

		case scissors:
			switch playerTwo[input[i+1]] {
			case game["win"]:
				c := rock + game["win"]
				sum = sum + c
			case game["draw"]:
				c := scissors + game["draw"]
				sum = sum + c
			case game["loss"]:
				c := paper + game["loss"]
				sum = sum + c
			default:
				fmt.Println("error")
			}
		default:
			fmt.Println("error")
		}

	}
	fmt.Println(sum)
}

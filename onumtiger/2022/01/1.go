package one

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func First() {
	content, err := os.ReadFile("./01/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	t := string(content[:])
	input := strings.Split(t, "\n")

	var acc int = 0
	var caloriesPerElves = []int{}
	for _, calories := range input {
		if calories > "0" {

			converted, _ := strconv.Atoi(calories)
			acc += converted
		} else {
			caloriesPerElves = append(caloriesPerElves, acc)
			acc = 0
		}
	}

	max := map[string]int{"elve": -1, "calories": 0}
	for elve, calories := range caloriesPerElves {
		if calories > max["calories"] {
			max = map[string]int{"elve": elve + 1, "calories": calories}
		}
	}

	fmt.Println(max)
}

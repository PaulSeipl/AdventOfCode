package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func second() {
	content, _ := ioutil.ReadFile("1.txt")
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

	maxThree := [3]map[string]int{{"elve": -1, "calories": 0}, {"elve": -1, "calories": 0}, {"elve": -1, "calories": 0}}

	for elve, calories := range caloriesPerElves {
		if calories > maxThree[0]["calories"] {
			maxThree[2] = maxThree[1]
			maxThree[1] = maxThree[0]
			maxThree[0] = map[string]int{"elve": elve + 1, "calories": calories}
		} else if calories > maxThree[1]["calories"] {
			maxThree[2] = maxThree[1]
			maxThree[1] = map[string]int{"elve": elve + 1, "calories": calories}
		} else if calories > maxThree[2]["calories"] {
			maxThree[2] = map[string]int{"elve": elve + 1, "calories": calories}
		}
	}

	max := maxThree[0]["calories"] + maxThree[1]["calories"] + maxThree[2]["calories"]
	fmt.Println(max)
}

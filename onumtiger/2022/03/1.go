package three

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func First() {
	convertMap := map[string]int{"A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

	content, err := os.ReadFile("./03/input.txt")
	if err != nil {
		log.Fatal(err)
	}
	t := string(content[:])
	r := strings.Split(t, "\n")

	doubles := []string{}

	for j := 0; j < len(r); j++ {
		firstHalf := r[j][0 : len(r[j])/2]
		secondHalf := r[j][len(r[j])/2 : len(r[j])]

		for i := 0; i < len(firstHalf); i++ {
			if strings.Contains(firstHalf, (string(secondHalf[i]))) {
				doubles = append(doubles, string(secondHalf[i]))
				break
			}
		}
	}

	sum := 0

	for i := 0; i < len(doubles); i++ {
		sum = sum + convertMap[doubles[i]]
	}

	fmt.Println(sum)
}

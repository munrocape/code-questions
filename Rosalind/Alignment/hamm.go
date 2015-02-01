package main

import "fmt"

func main() {
	sequenceA := "GAGCCTACTAACGGGAT"
	sequenceB := "CATCGTAATGACGGCCT"
	
	length := len(sequenceA)
	distance := 0
	for i := 0; i < length; i++ {
		if sequenceA[i] != sequenceB[i] {
			distance += 1
		}
	}
	fmt.Printf("%d\n", distance)
}
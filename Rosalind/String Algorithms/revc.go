package main

import "fmt"

func main() {
	sequence := "AAAACCCGGT"

	reversed_sequence := []rune(sequence)
	for i, j := 0, len(reversed_sequence)-1; i < len(reversed_sequence)/2; i, j = i+1, j-1 {
		reversed_sequence[i], reversed_sequence[j] = reversed_sequence[j], reversed_sequence[i]
	}
	
	// max input of size 1000
	var complement [1000]byte
	length := len(reversed_sequence)
	for i := 0; i < length; i++ {
		if reversed_sequence[i] == 'A' {
			complement[i] = 'T'
		} else if reversed_sequence[i] == 'C' {
			complement[i] = 'G'
		} else if reversed_sequence[i] == 'T' {
			complement[i] = 'A'
		} else if reversed_sequence[i] == 'G' {
			complement[i] = 'C'
		}
	}
	fmt.Printf("%s\n", complement)
}
package main

import ("fmt"
        "strings"
        "time"
)

type dnaCount struct {
	A, C, G, T int
}

func iterate_occurances(dna string) dnaCount {
	length := len(dna)
	count := dnaCount{A: 0, C: 0, G: 0, T: 0}
	for i := 0; i < length; i++ {
		if dna[i] == 'A' {
			count.A += 1
		} else if dna[i] == 'C' {
			count.C += 1
		} else if dna[i] == 'G' {
			count.G += 1
		} else if dna[i] == 'T' {
			count.T += 1
		}
	}
	return count
}

func count_occurances(dna string) dnaCount {
	count := dnaCount{A: 0, C: 0, G: 0, T: 0}
	count.A = strings.Count(dna, "A")
	count.C = strings.Count(dna, "C")
	count.G = strings.Count(dna, "G")
	count.T = strings.Count(dna, "T")
	return count
}

func main() {
	sequence := "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	count_start_time := time.Now()
	dna_count := count_occurances(sequence)
	count_elapsed_time := time.Since(count_start_time)
	fmt.Printf("count run time: %s\n", count_elapsed_time)

	iterate_start_time := time.Now()
	dna_iterate := iterate_occurances(sequence)
	iterate_elapsed_time := time.Since(iterate_start_time)
	fmt.Printf("iterate run time: %s\n", iterate_elapsed_time)

	fmt.Printf("Result of strings.Count: %d %d %d %d\n", dna_count.A, dna_count.C, dna_count.G, dna_count.T)
	fmt.Printf("Result of iteration: %d %d %d %d\n", dna_iterate.A, dna_iterate.C, dna_iterate.G, dna_iterate.T)

}
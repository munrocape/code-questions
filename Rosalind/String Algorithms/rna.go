package main

import ("fmt" 
       "strings"
       "time"
)

func main() {
	sequence := "GATGGAACTTGACTACGTAAATT"
	
	replace_start_time := time.Now()
	fmt.Printf(strings.Replace(sequence, "T", "U" , -1))
	replace_elapsed_time := time.Since(replace_start_time)
	
	// max input of size 1000
	iterate_start_time := time.Now()
	var derp [1000]byte
	length := len(sequence)
	for i := 0; i < length; i++ {
		if sequence[i] == 'T' {
			derp[i] = 'U'
		} else {
			derp[i] = sequence[i]
		}
	}
	fmt.Printf("\n\n%s\n", derp)
	iterate_elapsed_time := time.Since(iterate_start_time)
	
	fmt.Printf("replace run time: %s\n", replace_elapsed_time)
	fmt.Printf("iterate run time: %s\n", iterate_elapsed_time)
}
package main

import "fmt"

func convertToProtein(rna string, rnaDict map[string]string) string{
	return ""
}

func main() {

	rnaToProtein := make(map[string]string)
    rnaToProtein["UUU"] = "F"
    rnaToProtein["UUC"] = "F"
    rnaToProtein["UUA"] = "L"
    rnaToProtein["UUG"] = "L"

    rnaToProtein["UCU"] = "S"
    rnaToProtein["UCC"] = "S"
    rnaToProtein["UCA"] = "S"
    rnaToProtein["UCG"] = "S"

    rnaToProtein["UAU"] = "Y"
    rnaToProtein["UAC"] = "Y"
    rnaToProtein["UAA"] = "STOP"
    rnaToProtein["UAG"] = "STOP"

    rnaToProtein["UGU"] = "C"
    rnaToProtein["UGC"] = "C"
    rnaToProtein["UGA"] = "STOP"
    rnaToProtein["UGG"] = "W"

    rnaToProtein["CUU"] = "L"
    rnaToProtein["CUC"] = "L"
    rnaToProtein["CUA"] = "L"
    rnaToProtein["CUG"] = "L"

    rnaToProtein["CCU"] = "P"
    rnaToProtein["CCC"] = "P"
    rnaToProtein["CCA"] = "P"
    rnaToProtein["CCG"] = "P"

    rnaToProtein["CAU"] = "H"
    rnaToProtein["CAC"] = "H"
    rnaToProtein["CAA"] = "Q"
    rnaToProtein["CAG"] = "Q"

    rnaToProtein["CGU"] = "R"
    rnaToProtein["CGC"] = "R"
    rnaToProtein["CGA"] = "R"
    rnaToProtein["CGG"] = "R"

    rnaToProtein["AUU"] = "I"
    rnaToProtein["AUC"] = "I"
    rnaToProtein["AUA"] = "I"
    rnaToProtein["AUG"] = "M"

    rnaToProtein["ACU"] = "T"
    rnaToProtein["ACC"] = "T"
    rnaToProtein["ACA"] = "T"
    rnaToProtein["ACG"] = "T"

    rnaToProtein["AAU"] = "N"
    rnaToProtein["AAC"] = "N"
    rnaToProtein["AAA"] = "K"
    rnaToProtein["AAG"] = "K"

    rnaToProtein["AGU"] = "S"
    rnaToProtein["AGC"] = "S"
    rnaToProtein["AGA"] = "R"
    rnaToProtein["AGG"] = "R"

    rnaToProtein["GUU"] = "V"
    rnaToProtein["GUC"] = "V"
    rnaToProtein["GUA"] = "V"
    rnaToProtein["GUG"] = "V"

    rnaToProtein["GCU"] = "A"
    rnaToProtein["GCC"] = "A"
    rnaToProtein["GCA"] = "A"
    rnaToProtein["GCG"] = "A"

    rnaToProtein["GAU"] = "D"
    rnaToProtein["GAC"] = "D"
    rnaToProtein["GAA"] = "E"
    rnaToProtein["GAG"] = "E"

    rnaToProtein["GGU"] = "G"
    rnaToProtein["GGC"] = "G"
    rnaToProtein["GGA"] = "G"
    rnaToProtein["GGG"] = "G"

    rna := ""
    
    fmt.Printf(convertToProtein(rna, rnaToProtein))

}
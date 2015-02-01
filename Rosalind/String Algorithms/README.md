For these problems, I was interested in the speed comparisions between the strings library and bespoke implementations of what I was trying to acomplish (count characters or replace them, for example). Other languages had better performance using the provided libraries and I couldn't grep anything conclusive on the series of tubes. Below is what I found. 

##dna.go time comparison (988 characters)
```
$ go run dna.go
count run time: 24.355µs
iterate run time: 16.971µs
Result of strings.Count: 251 247 266 223
Result of iteration: 251 247 266 223
```

This makes sense. Count is called four times, one for each character. However, because it is not 4 times the time taken to iterate once, count for one substring is faster than iterating for one substring.

###rna.go time comparison (989 characters)
```
$ go run rna.go
...
[output removed]
...
replace run time: 61.823µs
iterate run time: 97.197µs

```

Replace must have some magic in creating the array and replacing it than just iterating, checking, and replacing.
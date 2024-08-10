package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	return lim
}

type Vertex struct {
	X int
	Y int
}

func main() {

	names := [4]string{
		"John",
		"Paul",
		"Ringo",
		"George",
	}

	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]

	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}

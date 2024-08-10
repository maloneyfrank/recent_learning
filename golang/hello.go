package main

import (
	"fmt"
)

var name = "Franklin"

type Set struct {
	Data map[string]bool
}

func main() {

	mySet := Set{
		Data: map[string]bool{
			"hello": false,
		},
	}

	fmt.Println(mySet)

}

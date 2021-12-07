package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
	"sort"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var adapters []int
	ones := 1
	threes := 1
	for scanner.Scan(){
		number,_:= strconv.Atoi(scanner.Text())
		adapters = append(adapters, number)
	}
	sort.Ints(adapters)
	for i:=1; i< len(adapters); i++{
		switch adapters[i] - adapters[i-1] {
			case 1:
				ones++
			case 3:
				threes++
			default:
				fmt.Println("WTF")
		}
		fmt.Println(adapters[i], ones, threes)
	}
	fmt.Println(ones, threes, ones * threes)
}

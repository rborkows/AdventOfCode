package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
	"sort"
	"math"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var adapters []int
	adapters = append(adapters, 0)
	for scanner.Scan(){
		number,_:= strconv.Atoi(scanner.Text())
		adapters = append(adapters, number)
	}
	sort.Ints(adapters)
	
	skippable := []int{0}
	skippable_1 := 0
	skippable_3 := 0
	for i:=2; i< len(adapters); i++{
		if(adapters[i] - adapters[i-2]) <= 3{
			skippable = append(skippable, adapters[i-1])
			if(len(skippable) > 3 && skippable[len(skippable)-1] - 2 == skippable[len(skippable)-3] && skippable[len(skippable)-1] - 1 == skippable[len(skippable)-2]){
				skippable_3++
				skippable_1 -= 2
			} else {
				skippable_1++
			}
			fmt.Println(adapters[i-1], " is skippable", skippable_1, skippable_3)
		}
	}
	fmt.Println(skippable_1, skippable_3, int(math.Pow(7.0, float64(skippable_3)) * math.Pow(2.0, float64(skippable_1))))
}

package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var numbers []int
	preamble := 25
	for scanner.Scan(){
		number,_:= strconv.Atoi(scanner.Text())
		numbers = append(numbers, number)
	}
	fmt.Println(numbers)
	var target int
	var matched bool
	for i := preamble; i<len(numbers); i++ {
		matched = false
		out:
		for j := i - preamble; j<i; j++ {
			target = numbers[i] - numbers[j]
			for k := i - preamble; k<i; k++ {
				if(i == k){
					continue
				}
				if(numbers[k] == target){
					fmt.Println("Found match: ", numbers[j], "+", numbers[k], "=", numbers[i])
					matched = true
					break out
				}
			}
		}
		if(!matched){
			fmt.Println("Failed to find a match for ", numbers[i])
			break
		}
	}
}

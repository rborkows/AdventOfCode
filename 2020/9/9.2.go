package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
)

// 572 138879426
func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var numbers []int
	for scanner.Scan(){
		number,_:= strconv.Atoi(scanner.Text())
		numbers = append(numbers, number)
	}

	var sum int
	var i int
	var j int
	out:
	for i = 0; i<=570; i++ {
		sum = numbers[i]
		for j = i + 1; j<=571; j++ {
			sum += numbers[j]
			if(sum == 138879426){
				break out
			}
		}
	}
	fmt.Println(i,j)
	min := 138879426
	max := 0
	for k := i; k<=j; k++ {
		if(numbers[k] < min){
			min = numbers[k]
		} else if(numbers[k] > max){
			max = numbers[k]
		}
	}
	fmt.Println(min, max, min + max)
		
}

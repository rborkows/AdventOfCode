package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

func countbits(n int32) int32{
	var sum int32 = 0

	for p := 0; p<32; p++ {
		sum += (n & 1)
		n = n >> 1
	}
	return sum
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 


	var answers int32 = ^0
	var answer int32 = 0
	var sum int32 = 0
	for scanner.Scan(){
		line := scanner.Text()
		if(len(line) > 0){
			answer = 0
			for _,c := range(line){
				answer |= 1<< (c-'a')
				fmt.Println("c: ", c-'a')
			}
			fmt.Println(line, answer)
			answers &= answer
		} else {
			fmt.Println("***", answers, countbits(answers))
			sum += countbits(answers)
			answers = ^0
		}
	}
	fmt.Println(sum + countbits(answers))
}

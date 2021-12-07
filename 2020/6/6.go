package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 


	answers := make(map[rune]bool)
	sum := 0
	for scanner.Scan(){
		line := scanner.Text()
		if(len(line) > 0){
			for _,c := range(line){
				answers[c] = true
			}
//			fmt.Println(line, answers, len(answers))
		} else {
			sum += len(answers)
			fmt.Println("**** ", answers, len(answers), sum)
			answers = make(map[rune]bool)
		}
	}
	fmt.Println("Final sum: ", sum + len(answers))
}

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
	var expenses []int

	for scanner.Scan(){
		expense, _ := strconv.Atoi(scanner.Text())
		expenses= append(expenses, expense)
	}
	sort.Ints(expenses)

	found:
	for i := 0; i < len(expenses); i++ {
		for j := len(expenses)-1; j>i; j-- {
			for k := i+1; k<j; k++ {
				sum := expenses[i] + expenses[j] + expenses[k]
				if(sum == 2020){
					fmt.Println(expenses[i], "+", expenses[j], "+", expenses[k], "=", sum, expenses[i] * expenses[j] * expenses[k])
					break found
				}
			}
		}
	}
}

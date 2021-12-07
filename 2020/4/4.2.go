package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 


	for scanner.Scan(){
		line := strings.Fields(scanner.Text())
	}
}

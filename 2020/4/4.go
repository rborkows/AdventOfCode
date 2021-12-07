package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strings"
)

func isValid(passport map[string]string) bool{
	required := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _,rk := range(required){
		if _,ok := passport[rk]; !ok {
			return(false)
		}
	}
	return(true)
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 


	attribute := map[string]string{}
	valid := 0
	for scanner.Scan(){
		line := strings.Fields(scanner.Text())
		if(len(line) > 0){
			fmt.Println("line: ", line)
			for _,e := range line {
				kv := strings.Split(e, ":")
//				fmt.Println("kv: ", kv)
				attribute[kv[0]] = kv[1]
			}
		} else {
			fmt.Println("attributes: ", attribute)
			if(isValid(attribute)){
				valid++
			}

			attribute = make(map[string]string)

		}
	}
	fmt.Println("valid: ", valid)
}

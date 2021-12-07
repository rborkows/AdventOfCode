package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	vp := 0
	for scanner.Scan(){
		line := strings.Fields(scanner.Text())
		minmax := strings.Split(line[0], "-")
		min,_ := strconv.Atoi(minmax[0])
		max,_ := strconv.Atoi(minmax[1])
		char := rune(line[1][0])

		cc := 0
		for _, c := range line[2]{
			if(c==char){
				cc++
			}
		}
		if(cc >= min && cc <= max){
			vp++
		}
		
		
		
		fmt.Println(min, max, char, cc, line)
	}

	fmt.Println("vp =", vp)
}

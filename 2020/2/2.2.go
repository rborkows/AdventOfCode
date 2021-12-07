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
		mc := 0
		line := strings.Fields(scanner.Text())
		minmax := strings.Split(line[0], "-")
		min,_ := strconv.Atoi(minmax[0]) 
		max,_ := strconv.Atoi(minmax[1]) 
		min--
		max--

		char := rune(line[1][0])
		pwd := []rune(line[2])
		if(pwd[min] == char){
			mc++
		}
		if(pwd[max] == char){
			mc++
		}
		if(mc == 1){
			vp++
		}

		fmt.Println(min, max, char, mc, line)
		
	}

	fmt.Println("vp =", vp)
}

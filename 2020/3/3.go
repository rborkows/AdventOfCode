package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

func ride(slope []string, xdelta int, ydelta int) int {
	x := 0
	y := 0

	width := len(slope[0]) 
	height := len(slope)

	trees := 0
	for(y < height){
		if(slope[y][x%width] == "#"[0]){
			trees++
		}
		x += xdelta
		y += ydelta
	}
	return(trees)
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var slope []string

	result := 1

	for scanner.Scan(){
		slope = append(slope, scanner.Text())
	}

	testset := [][]int{{1,1},{3,1},{5,1},{7,1},{1,2}}

	for _,t := range testset{
		result *= ride(slope, t[0], t[1])
		fmt.Println("testset: ", t, result)
	}

	


}

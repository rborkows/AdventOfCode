package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

func bsp(id string) int {
	l := len(id)
	u := (1 << l) - 1
	l = 0
	for _,c := range id {
		m := (l + u) / 2
		if(c == 70 || c == 76){  // Lower
			u = m
		} else { // Upper
			l = m + 1
		}
//		fmt.Println("after: ", l, u)
			
	}
	if(l == u){
		return(l)
	} else {
		fmt.Println("****** WTF")
		return(l)
	}
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 


	maxId := 0
	for scanner.Scan(){
		line := scanner.Text()
		row_bsp := line[:7]
		col_bsp := line[7:]
		row := bsp(row_bsp)
		col := bsp(col_bsp)
		id := row*8 + col
		if(id > maxId){
			maxId = id
		}
	}
	fmt.Println(maxId)
}

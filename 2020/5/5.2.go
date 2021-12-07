package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"sort"
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
	var ids []int

	for scanner.Scan(){
		line := scanner.Text()
		row_bsp := line[:7]
		col_bsp := line[7:]
		row := bsp(row_bsp)
		col := bsp(col_bsp)
		id := row*8 + col
		ids = append(ids, id)
	}
	sort.Ints(ids)

	for i := 0; i < len(ids) - 1; i++ {
		if(ids[i+1] != ids[i] + 1){
			fmt.Println(ids[i], ids[i+1])
		}
	}
}

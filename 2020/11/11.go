package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
)

type Coordinate struct {
	row int
	column int
}

func printboard(floor [][]int8){
	for _,r := range floor{
		for _,e := range r {
			switch e {
				case -1:
					fmt.Print("L")
				case 0:
					fmt.Print(".")
				case 1:
					fmt.Print("#")
			}
		}
	fmt.Println("")
	}
}

func neighbour_count(floor [][]int8, row int, col int) int {
	ret := 0
	directions := [][]int{{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}}
	for _,n := range directions {
		n_row := n[0] + row
		n_col := n[1] + col
		if(n_row >= 0 && n_row < len(floor) && n_col >= 0 && n_col < len(floor[0]) && floor[n_row][n_col] == 1){
			ret++
		}
	}
	return ret
}

func occupied(floor [][]int8) int {
	ret := 0
	for _,r := range floor {
		for _,e := range r {
			if(e == 1){
				ret++
			}
		}
	}
	return ret
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

//	var floor = make([][]int8,91)
	var floor = make([][]int8,10)
	row := 0
	// -1 empty
	// 0 no seat
	// 1 occupied
	for scanner.Scan(){
		line := scanner.Text()
		floor[row] = make([]int8, len(line))
		for col,c := range line{
			if(c == 76){
				floor[row][col] = -1
			}
		}
		row++
	}
	rows := len(floor)
	columns := len(floor[0])

	changes := 1
	cycle := 0
	neighbours := 0
	var changelist []Coordinate

	printboard(floor)
	fmt.Println("------")
	fmt.Println(floor[1][1], neighbour_count(floor,1,1))
	for changes > 0 {
		changes = 0
		for r := 0; r< rows; r++{
			for c:= 0; c< columns; c++{
				neighbours = neighbour_count(floor, r, c)
				if((neighbours == 0 && floor[r][c] == -1 )  || (neighbours >= 4 && floor[r][c] == 1)){
					changes++
					changelist = append(changelist, Coordinate{r, c})
				}
				
			}
		}
		for _,c := range changelist {
			floor[c.row][c.column] *= -1
		}
		printboard(floor)
		changelist = make([]Coordinate, 0)
		cycle++
		fmt.Println("Cycle ", cycle, ", changes: ", changes, ", occupied: ", occupied(floor), floor[1][1], neighbour_count(floor,1,1))
	}
}

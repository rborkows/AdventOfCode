package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
	"regexp"
)

func abs(n int) int{
	if(n < 0){
		return -n
	} else {
		return n
	}
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var line string
	var operator string
	var operand int
	x := 0
	y := 0
	dir := 90
	re := regexp.MustCompile(`^([NSEWLRF])(\d+)$`)
	for scanner.Scan(){
		line = scanner.Text()
		ma := re.FindStringSubmatch(line)
		operator = ma[1]
		operand,_ = strconv.Atoi(ma[2])
		switch operator {
			case "R":
				dir = (dir + operand) % 360
			case "L":
				dir = ((dir + 360) - operand) % 360
			case "F":
				switch dir {
					case 0:
						y += operand
					case 90:
						x += operand
					case 180:
						y -= operand
					case 270:
						x-= operand
				}
			case "N":
				y += operand
			case "S":
				y -= operand
			case "E":
				x += operand
			case "W":
				x -= operand
			default:
				fmt.Println("******* Unhandled operator")
		}

		fmt.Println(operator, operand, x, y, dir)
	}
	fmt.Println("Manhattan: ", abs(x) + abs(y))
}

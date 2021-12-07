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

type Coord struct {
	x int
	y int
}

func sin(angle int) int {
	switch angle {
		case 0:
			return 0
		case 90:
			return 1
		case 180:
			return 0
		case 270:
			return -1
	}
	return 0
}

func cos(angle int) int {
	switch angle {
		case 0:
			return 1
		case 90:
			return 0
		case 180:
			return -1
		case 270:
			return 0
	}
	return 0
}

func rotate(p Coord, angle int) Coord {
	x1 := p.x * cos(angle) - p.y * sin(angle)
	y1 := p.x * sin(angle) + p.y * cos(angle)
	p.x = x1
	p.y = y1
	return p
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

	wp := Coord{10,1}
	pos := Coord{0,0}
	re := regexp.MustCompile(`^([NSEWLRF])(\d+)$`)
	for scanner.Scan(){
		line = scanner.Text()
		ma := re.FindStringSubmatch(line)
		operator = ma[1]
		operand,_ = strconv.Atoi(ma[2])
		switch operator {
			case "R":
				wp = rotate(wp, 360 - operand)
			case "L":
				wp = rotate(wp, operand)
			case "F":
				pos.x += wp.x * operand
				pos.y += wp.y * operand
			case "N":
				wp.y += operand
			case "S":
				wp.y -= operand
			case "E":
				wp.x += operand
			case "W":
				wp.x -= operand
			default:
				fmt.Println("******* Unhandled operator")
		}

		fmt.Println(operator, operand, pos, wp)
	}
	fmt.Println("Manhattan: ", abs(pos.x) + abs(pos.y))
}

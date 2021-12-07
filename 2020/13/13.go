package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func min(a []int) (int, int){
	m := a[0]
	mi := 0
	for i,n := range a{
		if n < m {
			m = n
			mi = i
		}
	}
	return mi, m
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 

	scanner.Scan()
	arrived,_:= strconv.Atoi(scanner.Text())
	scanner.Scan()
	line := strings.Split(scanner.Text(),",")
	file.Close()

	var schedule []int
	var bus_departures []int
	var bus_arrivals []int
	var delta []int

	for _,n := range line {
		if n != "x"{
			id,_ := strconv.Atoi(n)
			schedule = append(schedule, id)
			bus_departure := ((arrived / id) * id) + id
			bus_departures = append(bus_departures, bus_departure)
			delta = append(delta, bus_departure - arrived)
			bus_arrivals = append(bus_arrivals, bus_departure + id)
		}
	}

	fmt.Println(arrived)
	fmt.Println(schedule)
	fmt.Println(bus_departures)
	fmt.Println(bus_arrivals)
	fmt.Println(delta)
	mi,m := min(delta)
	fmt.Println(m * schedule[mi])

}

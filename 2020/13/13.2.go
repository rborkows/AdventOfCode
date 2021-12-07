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

func max(a []int) (int, int){
	m := a[0]
	mi := 0
	for i,n := range a{
		if n > m {
			m = n
			mi = i
		}
	}
	return mi, m
}

func drop(a []int, i int) []int {
	if (i == 0){
		return a[1:]
	} else if(i == len(a) - 1){
		return a[:len(a)-2]
	} else {
		for x := i; x<len(a)-1; x++{
			a[i] = a[i+1]
		}
		return a[:len(a)-2]
	}

	return a
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 

	scanner.Scan()
	arrived,_:= strconv.Atoi(scanner.Text())
	arrived++
	scanner.Scan()
	line := strings.Split(scanner.Text(),",")
	file.Close()

	var schedule,schedule_done []int
	var offset,offset_done []int

	period := 1
	for i,n := range line {
		if n != "x"{
			id,_ := strconv.Atoi(n)
			period *= id
			schedule = append(schedule, id)
			offset = append(offset, i)
		}
	}

	step := schedule[0]
	schedule_done = schedule
	offset_done = offset
	schedule = schedule[1:]
	offset = offset[1:]
//	fmt.Println(schedule)
//	fmt.Println(offset)

	ts := 0

	delta := 1
//	for delta != 0 {

	for delta > 0 {
		ts += step
		delta = 0
//		fmt.Println("testing: ", ts)
		for i := range schedule {
			if  (ts + offset[i]) % schedule[i] == 0{
//				fmt.Println("Partial: ", schedule[i], ts + offset[i])
				step *= schedule[i]
				schedule = drop(schedule,i)
				offset = drop(offset,i)
				break
			}

		}

		delta = 0
		for i:= range schedule_done {
			delta += (ts + offset_done[i]) % schedule_done[i]
		}

		if(delta == 0){ 
			fmt.Println("Solution: ",ts)
		}
	}
}

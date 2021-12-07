package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"regexp"
	"strings"
	"strconv"
)

type Baggage struct {
	size int
	name string
}

type stack []Baggage

func(s stack) Push (v Baggage) stack {
	return append(s, v)
}

func(s stack) Pop() (stack, Baggage) {
	l := len(s)
	return s[:l-1], s[l-1]
}

func(s stack) Isempty() bool {
	if(len(s)) == 0{
		return true
	} else {
		return false
	}
}

func str2Baggage(str string) Baggage {
	var ret = Baggage{}
	re := regexp.MustCompile(`^(\d+) (\w+ \w+)$`)
	ma := re.FindStringSubmatch(str)
	size,_ := strconv.Atoi(ma[1])
	ret.size = size
	ret.name = ma[2]
	return(ret)
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	re := regexp.MustCompile(`^(\w+ \w+) bags contain (.*)$`)
	re_contents := regexp.MustCompile(`(\d \w+ \w+) bag`)
	
	parents := make(map[string][]Baggage)

	for scanner.Scan(){
		line := scanner.Text()
		ma := re.FindStringSubmatch(line)
		if(!strings.Contains(ma[2], "no other")){
			parents[ma[1]] = make([]Baggage,  0)
			ma_contents := re_contents.FindAllStringSubmatch(line, -1)
			for _,child := range ma_contents {
				parents[ma[1]] = append(parents[ma[1]], str2Baggage(child[1]))
			}
		}
	}

//	fmt.Println("Leaves: ", leaves)
//	fmt.Println("Parents: ", parents)

	s := make(stack,0)
	s = s.Push(Baggage{1, "shiny gold"})
	var e Baggage
	var result []Baggage
	for !s.Isempty() {
		fmt.Println("stack: ", s)
		s,e = s.Pop()
		if children,ok := parents[e.name]; ok {
			result = append(result, e)
			for _,child := range children {
				fmt.Println("Child: ", child)
				child.size *= e.size
				s = s.Push(child)
			}
		} else {
			result = append(result, e)
		}
		fmt.Println(e.size, e.name)
	}
	fmt.Println("*****")
	fmt.Println(result)
	sum := 0
	for _,e := range result {
		sum += e.size
	}
	fmt.Println("sum: ", sum)

}

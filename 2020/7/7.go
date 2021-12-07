package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"regexp"
	"strings"
)

type stack []string

func(s stack) Push (v string) stack {
	return append(s, v)
}

func(s stack) Pop() (stack, string) {
	l := len(s)
	if(l == 0){
		return s, ""
	} else {
		return s[:l-1], s[l-1]
	}
}

func(s stack) Isempty() bool {
	if(len(s)) == 0{
		return true
	} else {
		return false
	}
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	re := regexp.MustCompile(`^(\w+ \w+) bags contain (.*)$`)
//	re_contents := regexp.MustCompile(`(\d \w+ \w+) bag`)
	
	bagtypes := make(map[string]string)
	s := make(stack,0)
	s = s.Push("shiny gold")
//	fmt.Println("stack: ", s)
	for scanner.Scan(){
		line := scanner.Text()
		ma := re.FindStringSubmatch(line)
		bagtypes[ma[1]] = ma[2]
//		ma_contents := re_contents.FindAllStringSubmatch(line, -1)
//		fmt.Println(line)
//		fmt.Println("bagname: ", ma[1])
//		fmt.Println("contents: ", ma[2])
//		if(len(ma_contents) == 0) {
//			fmt.Println("***** LEAF")
//		}
	}
	var target string
	results := make(map[string]bool)
	for !s.Isempty() {
		s,target = s.Pop()
		for k:= range bagtypes {
			if(strings.Contains(bagtypes[k], target)){
				if _,ok := results[k]; !ok {
					s = s.Push(k)
					results[k] = true
				}
				
			}
		}
	}
	for k:= range results {
		fmt.Println(k)
	}
}

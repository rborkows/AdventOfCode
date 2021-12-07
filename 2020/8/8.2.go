package main

import (
	"fmt"
	"bufio"
	"log"
	"os"
	"strings"
	"strconv"
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

type Instruction struct {
	operator string
	operand int
}

func mutate(instructions []Instruction, pc int){
	switch instructions[pc].operator {
	case "jmp":
		instructions[pc].operator = "nop"
	case "nop":
		instructions[pc].operator = "jmp"
	}
}

func main() {
	file, err := os.Open("input") 
  
	if err != nil { 
		log.Fatalf("failed to open input file") 
	}

	scanner := bufio.NewScanner(file) 
	scanner.Split(bufio.ScanLines) 

	var instructions []Instruction
	for scanner.Scan(){
		line := strings.Fields(scanner.Text())
		operator := line[0]
		operand,_ := strconv.Atoi(line[1])
		instructions = append(instructions, Instruction{operator, operand})
//		execution_count = append(execution_count, 0)
	}
	var ax int
	var pc int
	var execution_count = make([]int, len(instructions))
	for mutator := range instructions {
		ax = 0
		pc = 0
		if(instructions[mutator].operator == "acc"){
			fmt.Println("Skipping mutating instruction ", mutator)
			continue
		}
		mutate(instructions, mutator)
		for i := range execution_count {
			execution_count[i] = 0
		}
		for true {
			fmt.Println(pc, ax, instructions[pc])
			execution_count[pc]++
			switch instructions[pc].operator {
				case "acc":
					ax += instructions[pc].operand
					pc++
				case "nop":
					pc++
				case "jmp":
					pc += instructions[pc].operand
				}
			if(pc >= len(instructions) || execution_count[pc] > 0 ){
				break
			}
		}
		if(pc >= len(instructions)){
			fmt.Println("Success, by mutating instruction: ", mutator)
			break
		}
		mutate(instructions, mutator)
	}
	fmt.Println("Accumulator: ", ax)
}

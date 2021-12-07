package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Element struct {
	operator byte
	operand  int
}

func solve(s string) int {
	var ret, p, po int
	var op byte
	l := len(s)
	op = '+'
	for p < l {
		if s[p] >= '0' && s[p] <= '9' || s[p] == '(' {
			var n int
			if s[p] == '(' {
				ss := p + 1
				po++
				for po > 0 {
					p++
					if s[p] == '(' {
						po++
					} else if s[p] == ')' {
						po--
					}
				}
				//fmt.Println("subsolution", s[ss:p])
				n = solve(s[ss:p])
			} else {
				n = int(s[p]) - '0'
			}
			switch op {
			case '+':
				ret += n
			case '*':
				ret *= n
			}
			//fmt.Println("n", n)
		} else if s[p] == '+' || s[p] == '*' {
			op = s[p]
		}
		p++
	}

	return ret
}

func solve2(s string) int {
	var p, po int
	var math []Element
	l := len(s)

	for p < l {
		if s[p] >= '0' && s[p] <= '9' {
			var n int
			n = int(s[p]) - '0'
			math = append(math, Element{0, n})
		} else if s[p] == '+' || s[p] == '*' {
			math = append(math, Element{s[p], 0})
		} else if s[p] == '(' {
			ss := p + 1
			po++
			for po > 0 {
				p++
				if s[p] == '(' {
					po++
				} else if s[p] == ')' {
					po--
				}
			}
			math = append(math, Element{0, solve2(s[ss:p])})
		}
		p++
	}

	l = len(math)

	p = 0
	for p < l {
		if math[p].operator == '+' {
			math[p+1].operand += math[p-1].operand
			math = append(math[:p-1], math[p+1:]...)
			l -= 2
			p--
		}
		p++
	}
	p = 0
	for p < l {
		if math[p].operator == '*' {
			math[p+1].operand *= math[p-1].operand
			math = append(math[:p-1], math[p+1:]...)
			l -= 2
			p--
		}
		p++
	}
	if len(math) != 1 {
		fmt.Println("*********WTF")
	}
	return math[0].operand
}

func main() {
	//fmt.Println(solve2("1 + 2 * 3 + 4 * 5 + 6"))
	//fmt.Println(solve2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

	var sum int
	file, err := os.Open("input")

	if err != nil {
		log.Fatalf("failed to open input file")
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
		sum += solve2(line)
	}
	fmt.Println("sum:", sum)

}

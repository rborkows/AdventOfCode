package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Rule struct {
	name   string
	ranges []Range
}

func (rule *Rule) Isvalid(val int) bool {
	for _, r := range rule.ranges {
		if r.Isvalid(val) {
			return true
		}
	}

	return false
}

func (rule *Rule) Arevalid(val []int) bool {
	for _, v := range val {
		if !rule.Isvalid(v) {
			return false
		}

	}
	return true
}

type Range struct {
	start  int
	finish int
}

func (r *Range) Fromstring(s string) {
	sa := strings.Split(s, "-")
	r.start, _ = strconv.Atoi(sa[0])
	r.finish, _ = strconv.Atoi(sa[1])
}

func (r *Range) Isvalid(val int) bool {
	//fmt.Println("Comparing", val, " against ", r, " :", val >= r.start && val <= r.finish)
	if val >= r.start && val <= r.finish {
		return true
	}
	return false
}

type Ticket struct {
	fields []int
}

func (t *Ticket) Fromstring(s string) {
	sa := strings.Split(s, ",")
	for _, n := range sa {
		x, _ := strconv.Atoi(n)
		t.fields = append(t.fields, x)
	}
}

func (t *Ticket) Invalidcount(ranges []Range) (bool, int) {
	ret := 0
	retval := true
	var valid bool
	for _, field := range t.fields {
		valid = false
		for _, r := range ranges {
			if r.Isvalid(field) {
				valid = true
				break
			}
		}
		if !valid {
			retval = false
			ret += field
		}
	}
	return retval, ret
}

func getcolumn(tickets []Ticket, column int) []int {
	var ret []int
	for _, ticket := range tickets {
		ret = append(ret, ticket.fields[column])
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

	var ranges []Range
	var rules []Rule
	re := regexp.MustCompile(`^([^:]+): (\d+-\d+) or (\d+-\d+)`)
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
			break
		}
		ma := re.FindStringSubmatch(line)
		if len(ma) > 2 {

			r1 := Range{}
			r1.Fromstring(ma[2])
			r2 := Range{}
			r2.Fromstring(ma[3])
			rule := Rule{}
			rule.name = ma[1]
			rule.ranges = append(rule.ranges, r1)
			rule.ranges = append(rule.ranges, r2)
			rules = append(rules, rule)
			ranges = append(ranges, r1)
			ranges = append(ranges, r2)
		}
	}

	scanner.Scan()
	_ = scanner.Text() // your ticket:
	scanner.Scan()
	line := scanner.Text() // ticket details
	myticket := Ticket{}
	myticket.Fromstring(line)
	fmt.Println(myticket)

	scanner.Scan() // skip blank line
	scanner.Scan() // nearby tickets:

	var sum int
	var tickets []Ticket
	for scanner.Scan() {
		line := scanner.Text()
		ticket := Ticket{}
		ticket.Fromstring(line)
		tickets = append(tickets, ticket)
	}

	//	fmt.Println(ranges)
	file.Close()

	var validtickets []Ticket
	for _, ticket := range tickets {

		valid, invc := ticket.Invalidcount(ranges)
		if valid {
			validtickets = append(validtickets, ticket)
		}
		sum += invc
	}
	fmt.Println("Part 1 solution: ", sum) // 32835

	field2column := make(map[string]int)
	solvedcolumns := make(map[int]bool)
	for len(solvedcolumns) < len(validtickets[0].fields) {
		fmt.Println("TOP:", validtickets[0])
		for col := 0; col < len(validtickets[0].fields); col++ {
			_, ok := solvedcolumns[col]
			if ok {
				continue // already solved
			}
			ca := getcolumn(validtickets, col)

			rc := make(map[string]int)
			for _, r := range rules {
				_, ok := field2column[r.name] // skip rules that are already solved

				if !ok && r.Arevalid(ca) {
					rc[r.name]++
				}

			}

			fmt.Println(col, len(rc), rc)
			if len(rc) == 1 {
				var fieldname string
				for fn := range rc {
					fieldname = fn
				}
				field2column[fieldname] = col
				solvedcolumns[col] = true
				break
			}

		}
	}
	//fmt.Println("SOLUTION:", field2column)
	solution := 1
	for key := range field2column {
		if strings.HasPrefix(key, "departure") {
			solution *= myticket.fields[field2column[key]]
			fmt.Println(key, myticket.fields[field2column[key]])
		}

	}
	fmt.Println("Solution:", solution)

}

// 12 = class, 9 = arrival location, 7 = arrival track

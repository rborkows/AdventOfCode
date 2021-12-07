package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
	"strconv"
)

type Mask struct {
	mask_and uint64
	mask_or uint64
}

func genmask(mask string)(Mask){
	ret := Mask{0,0}
	ret.mask_and = ^ret.mask_and
	p := 35
	for _,c := range mask {
		switch c {
			case 48:
				ret.mask_and ^= 1<<p
			case 49:
				ret.mask_or |= 1<<p
		}
		p--
	}

	return ret
}

func mask(m Mask, n uint64) uint64{
	n &= m.mask_and
	n |= m.mask_or

	return n
}

func main() {
	file, err := os.Open("input")

        if err != nil {
                log.Fatalf("failed to open input file")
        }

        scanner := bufio.NewScanner(file)
        scanner.Split(bufio.ScanLines)

	mem := make(map[uint64]uint64)
	fmt.Println(mem)

	var m Mask
	for scanner.Scan(){
		line := strings.Fields(scanner.Text())
		if line[0] == "mask"{
			m = genmask(line[2])
			fmt.Println("New Mask: ", m)
		} else {
			address,_ := strconv.Atoi(line[0][4:len(line[0])-1])
			value,_ := strconv.Atoi(line[2])
			fmt.Println("Set ", address, " = ", value)
			mem[uint64(address)] = mask(m, uint64(value))
		}

	}
	file.Close()
	fmt.Println(mem)
	var sum uint64
	for _,v := range mem {
		sum += v
	}
	fmt.Println("Sum: ", sum)


}

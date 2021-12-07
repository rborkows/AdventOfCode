package main

import (
	"fmt" 
	"os"
	"bufio"
	"log"
	"strings"
	"strconv" 
)

func genaddresses(m []byte, a uint64) []uint64{
	var in [][]byte
	var out []uint64

	as := []byte(fmt.Sprintf("%0.36b", a))

	for i,c := range m{
		switch c {
			case 49:
				as[i] = 49
			case 88:
				as[i] = 88
		}
	}

	in = append(in, as)

	for len(in) > 0 {
//		fmt.Println("in: ", in)
		as = in[len(in)-1]
		in = in[:len(in)-1] // pop
		clean := true
		for i,v := range as {
			if(v == 88){
				as1 := make([]byte, len(as))
				copy(as1,as)
				as1[i] = 48
				in = append(in, as1)
				as1 = make([]byte, len(as))
				copy(as1,as)
				as1[i] = 49
				in = append(in, as1)
				clean = false
				break
			}

			
		}
		if(clean){
			var o uint64
			p := 35
			for _,c := range as {
				if c == 49 {
					o |= 1<<p
				}
				p--
			} 
			out = append(out, o)
		}
	}

//	fmt.Println("Out: ", len(out), out)
	return out
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

	var mask []byte
	var addresses []uint64
        for scanner.Scan(){
                line := strings.Fields(scanner.Text())
                if line[0] == "mask"{
                        mask = []byte(line[2])
                        fmt.Println("New Mask: ", mask)
                } else {
                        a,_ := strconv.Atoi(line[0][4:len(line[0])-1])
			address := uint64(a)
                        value,_ := strconv.Atoi(line[2])
                        fmt.Println("Set ", address, " = ", value)
			addresses = genaddresses(mask, address)
			for _,address := range addresses {
	                        mem[uint64(address)] = uint64(value)
			}

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

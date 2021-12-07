package main

import (
	"fmt"
)

func main() {
	lim := 1090937521514009
	step := 256769
	
	lines := 0
	for  ts := 0; ts < lim; ts += step{
		lines++
		if(lines%1000000000 == 0){
			fmt.Println(ts, lim - ts)
		}
	}

}

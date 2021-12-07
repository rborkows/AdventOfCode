package main

import (
	"fmt"
)

func main() {
//	numbers := []int{0,3,6}
	numbers := []int{1,0,16,5,17,4}
	spokenlast := make(map[int]int)
	
	turn := 1
	var say int
	for i := 0; i < len(numbers) - 1; i++ {
		spokenlast[numbers[i]] = turn
		turn++
	}

	fmt.Println(spokenlast)

	say = numbers[len(numbers)-1]

	for turn < 30000000 {
		turn++
//		fmt.Println("Turn", turn, " begins", spokenlast)
		v,ok := spokenlast[say]
		if ok {
//			fmt.Println(say, " last spoken at turn ", spokenlast[say], " current turn is ", turn)
			spokenlast[say] = turn - 1
			say = (turn - 1) - v
		} else {
//			fmt.Println("First time for ", say)
			spokenlast[say] = turn - 1
			say = 0
		}
		if(turn % 10000000 == 0){
			fmt.Println("Turn", turn, " ends, saying", say)
		}
	}
	fmt.Println("Last spoken:", say)

//	fmt.Println(spokenlast)


}

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Point struct {
	x, y, z, w int
}

type Space struct {
	active map[Point]bool
}

func (s *Space) Addpoint(p Point) {
	s.active[p] = true
}

func (s *Space) Delpoint(p Point) {
	delete(s.active, p)
}

func (s *Space) isPoint(p Point) bool {
	_, ret := s.active[p]
	return ret
}

func NewSpace() *Space {
	var s Space
	s.active = make(map[Point]bool)
	return &s
}

func (p *Point) Neighbors() []Point {
	var ret []Point
	offset := []int{-1, 0, 1}
	for _, x := range offset {
		for _, y := range offset {
			for _, z := range offset {
				for _, w := range offset {
					if !(x == 0 && y == 0 && z == 0 && w == 0) {
						ret = append(ret, Point{p.x + x, p.y + y, p.z + z, p.w + w})
					}
				}
			}
		}
	}
	return ret
}

func (s *Space) Activeneighborcount(p Point) int {
	var ret int
	for _, n := range p.Neighbors() {
		_, ok := s.active[n]
		if ok {
			ret++
		}
	}

	return ret
}

func (s *Space) Activecount() int {
	return len(s.active)
}

func (s *Space) Pointsinplay() []Point {
	var ret []Point
	dedup := make(map[Point]bool)

	for k := range s.active {
		dedup[k] = true
		for _, n := range k.Neighbors() {
			dedup[n] = true
		}
	}

	for p := range dedup {
		ret = append(ret, p)
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

	var y, z, w int
	space := NewSpace()
	for scanner.Scan() {
		line := scanner.Text()
		for x, c := range line {

			if c == 35 {
				space.Addpoint(Point{x, y, z, w})
			}
		}

		y++
	}

	var toDelete, toSet []Point
	for c := 0; c <= 6; c++ {
		fmt.Println("Cycle", c, " active count:", space.Activecount())
		inPlay := space.Pointsinplay()
		for _, p := range inPlay {
			anc := space.Activeneighborcount(p)
			if space.isPoint(p) {
				if !(anc == 2 || anc == 3) {
					toDelete = append(toDelete, p)
				}
			} else {
				if anc == 3 {
					toSet = append(toSet, p)
				}
			}
		}
		for _, td := range toDelete {
			space.Delpoint(td)
		}
		for _, ts := range toSet {
			space.Addpoint(ts)
		}
		toDelete = make([]Point, 0)
		toSet = make([]Point, 0)
	}

}

package Easy

import "fmt"

func Timeloop() {
	var n int
	fmt.Scanln(&n)

	for i := 1; i <= n; i++ {
		fmt.Printf("%d Abracadabra\n", i)
	}
}
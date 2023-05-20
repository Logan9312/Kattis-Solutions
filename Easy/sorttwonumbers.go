package Easy

import "fmt"

func SortTwoNumbers() {
	var a, b int
	fmt.Scan(&a, &b)

	if a > b {
		fmt.Println(b, a)
	} else {
		fmt.Println(a, b)
	}
}

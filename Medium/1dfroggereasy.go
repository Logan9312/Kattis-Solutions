package Medium

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func FroggerEasy() {
	in := bufio.NewReader(os.Stdin)
	input, _ := in.ReadString('\n')
	input = strings.Trim(input, "\r\n")
	nsm := strings.Split(input, " ")

	length, _ := strconv.Atoi(nsm[0])
	pos, _ := strconv.Atoi(nsm[1])
	pos = pos - 1
	magic, _ := strconv.Atoi(nsm[2])

	board, _ := in.ReadString('\n')
	board = strings.Trim(board, "\r\n")
	spaces := strings.Split(board, " ")

	history := map[int]bool{}

	i := 0
	for {

		if pos >= length {
			fmt.Println("right")
			break
		}

		if pos < 0 {
			fmt.Println("left")
			break
		}

		num, _ := strconv.Atoi(spaces[pos])
		if num == magic {
			fmt.Println("magic")
			break
		}

		if history[pos] || num == 0 {
			fmt.Println("cycle")
			break
		}

		history[pos] = true

		pos += num
		i++
	}
	fmt.Println(i)
}

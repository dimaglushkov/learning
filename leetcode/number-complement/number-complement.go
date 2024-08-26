package main

import (
	"fmt"
	"strconv"
)

func findComplement(num int) int {
	x := strconv.FormatInt(int64(num), 2)
	b := make([]byte, len(x))
	for i := range x {
		if x[i] == '1' {
			b[i] = '0'
		} else {
			b[i] = '1'
		}
	}
	ans, _ := strconv.ParseInt(string(b), 2, 32)
	return int(ans)
}

func main() {
	testCases := []struct {
		num  int
		want int
	}{
		{
			num:  5,
			want: 2,
		},
		{
			num:  1,
			want: 0,
		},
	}

	successes := 0
	for _, tc := range testCases {
		x := findComplement(tc.num)
		status := "ERROR"
		if fmt.Sprint(x) == fmt.Sprint(tc.want) {
			status = "OK"
			successes++
		}
		fmt.Println(status, "	Expected: ", tc.want, " Actual: ", x)
	}
	if l := len(testCases); successes == len(testCases) {
		fmt.Printf("===\nSUCCESS: %d of %d tests ended successfully\n", successes, l)
	} else {
		fmt.Printf("===\nFAIL: %d tests failed\n", l-successes)
	}

}
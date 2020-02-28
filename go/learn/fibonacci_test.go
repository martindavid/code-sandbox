package learn

import (
	"fmt"
	"testing"
)

func TestRunFibonnaciFunctionSuccess(t *testing.T) {
	fib5 := FibMemoized(5)

	fmt.Println(fib5)

	if fib5 != 8 {
		t.Errorf("Fibonacci 5 should be 8")
	}
}

package main

import "fmt"

type cachekey struct {
	x float64
	n int
}

var cache = make(map[cachekey]float64)

func myPow(x float64, n int) float64 {
	// Abort on special cases
	if n == 0 {
		return 1
	}

	if x == 1 {
		return 1
	}

	// Cache lookup
	if val, ok := cache[cachekey{x, n}]; ok {
		return val
	}

	// Main logic
	if n < 0 {
		cache[cachekey{x, n}] = (1 / myPow(x, -n))
	}
	if n == 2 {
		cache[cachekey{x, n}] = x * x
	} else if n%2 == 0 {
		cache[cachekey{x, n}] = myPow(x, n/2) * myPow(x, n/2)
	} else {
		// n is odd
		cache[cachekey{x, n}] = x * myPow(x, n-1)
	}

	return cache[cachekey{x, n}]
}

func main() {
	result := myPow(2.10000, 3) // 9.261
	fmt.Println(result)
}

// 2^2 = 4^1 = 4
// 2^3 = 4^1 * 2 = 8
// 2^4 = 2^2 * 2^2 = 16
// n^x = n^(x/2) * n^(x/2) -- if x is even
// n^p = n * n^(x - 1) -- if x is odd

def find_outlier(integers)
even = Array.[]
odd = Array.[]

integers.each { |n|  n % 2 == 0 ? even.push(n) : odd.push(n)  }
even.length < odd.length ? even[0] : odd[0]

end

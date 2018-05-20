def solution(number)
 counter = 0
 number.times { |i| counter += i if i % 3 ==0 || i % 5 == 0 }
 return counter
end

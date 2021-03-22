class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        if n < 3:
            return [str(n)]
        for num in range(1, n+1):
            if num%3 == 0 and num%5 == 0:
                result.append("FizzBuzz")
            elif num%3 == 0:
                result.append("Buzz")
            elif num%5 == 0:
                result.append("Fizz")
            else:
                result.append(str(num))
        return result
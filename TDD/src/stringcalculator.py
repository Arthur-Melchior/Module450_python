class StringCalculator:
    def add(number):
        try:
            sum = int(number)
        except:
            sum = 0
        return sum

    def add(numbers):
        parts = numbers.split(';')

        sum = 0
        for part in parts:
            try:
                number = int(part)
            except ValueError:
                number = 0
            if number <= 1000:
                sum += number
        return sum

    def multiply(self: str):
        parts = self.split(';')

        num = 1
        for part in parts:
            try:
                number = int(part)
            except ValueError:
                number = 1
            if number <= 1000:
                num *= number
        return num

    def diviser(self: str):
        parts = self.split(';')

        num = int(parts[0])
        for part in parts[1:]:
            try:
                number = int(part)
            except ValueError:
                number = 1
            if number <= 1000:
                num /= number
        return num

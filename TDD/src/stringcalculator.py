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
    
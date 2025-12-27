from cons import Under_20, Tens, More_than_hundred


def number_to_word(num):
    if num < 20:
        return Under_20[num]
    elif num < 100:
        remainder = num % 10
        if remainder == 0:
            return Tens[num // 10]
        return Tens[num // 10] + " " + Under_20[remainder]
    
    pivot = max([key for key in More_than_hundred if key <= num])
    if num % pivot == 0:
        return f'{number_to_word(num // pivot)} {More_than_hundred[pivot]}'
    return f'{number_to_word(num // pivot)} {More_than_hundred[pivot]} {number_to_word(num % pivot)}'

if __name__ == "__main__":
    print(number_to_word(1111111))
    print(number_to_word(2222222))
    print(number_to_word(3333333))
    print(number_to_word(4444444))
    print(number_to_word(5555555))
    print(number_to_word(6666666))
    print(number_to_word(7777777))
    print(number_to_word(8888888))
    print(number_to_word(9999999))
    print(number_to_word(1000000))

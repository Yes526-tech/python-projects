def narcissistic(value):

    num_total_digit = 0
    length = len(str(value))

    for num in str(value):
        num_total_digit += int(num) ** length
    if num_total_digit == int(value):
        is_narcissistic = True
    else:
        is_narcissistic = False

    return is_narcissistic
narcissistic(153)
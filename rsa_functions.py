def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def calculate_n(prime_list):
    n = 1
    for i in prime_list:
        n *= i
    return n


def calculate_phi(prime_list):
    n = 1
    for i in prime_list:
        n *= (i - 1)
    return n


def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def calculate_e(phi):
    for i in range(1, phi):
        if calculate_gcd(i, phi) == 1 and i != 1:
            return i
    return 1


def calculate_modular_power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def calculate_modular_inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m
    print('error')


def get_uset_inputs():
    prime_check = int(input('Do you want the program to check if a inserted number is a prime? (1) yes (2) no '))
    func_prime_list = list()
    print('Insert positive numbers (one at a time): (type 0 to stop)')
    while True:
        user_input = input("")
        try:
            int(user_input)
        except ValueError:
            print('Type only numbers!!')
            continue
        user_input = int(user_input)
        if user_input < 0:
            print('Only positive numbers are allowed')
            continue
        elif user_input == 0:
            break
        elif prime_check == 1:
            if is_prime(user_input):
                func_prime_list.append(user_input)
            else:
                print('The inserted number is not a prime')
        elif prime_check == 2:
            func_prime_list.append(user_input)
    return func_prime_list


def get_message():
    int_message = int()
    is_int = 0
    while is_int != 1:
        func_message = input('Insert the message (only positive integers): ')
        try:
            int(func_message)
        except ValueError:
            print('Not a positive integer')
            continue
        int_message = int(func_message)
        if int_message <= 0:
            print('Not a positive integer')
            continue
        is_int = 1
    return int_message

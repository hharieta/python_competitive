def decimal_to_biyective(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return 'A'

    result = ""
    while n > 0:
        remainder = (n - 1) % 26
        result = alphabet[remainder] + result
        n = (n - 1) // 26
    return result

def biyective_to_decimal(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(s)):
        result = result * 26 + alphabet.index(s[i]) + 1
    return result

def main():
    conversion_type = int(input())
    if conversion_type == 0:
        number = int(input())
        print(decimal_to_biyective(number))
    elif conversion_type == 1:
        biyective_number = input()
        print(biyective_to_decimal(biyective_number))
    else:
        print("Tipo de conversión no válido.")

if __name__ == "__main__":
    main()

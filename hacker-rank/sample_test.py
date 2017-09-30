def findNumber(arr, k):
    if len(arr) > 0:
        for i in arr:
            if k == i:
                return "YES"
            else:
                return "NO"
    else:
        return "NO"


def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def convertToBinary(number):
    if number == 0: return "0"
    result = ""
    while number:
        result = "1" + result if int(number) & 1 == 1 else "0" + result
        number /= 2
    return result

def toBin(n):
    return ''.join(str(1 & int(n) >> i) for i in range(10)[::-1])


def timeConversion(ampmtime):
    period = ampmtime[-2:]
    hour = int(ampmtime[:2])
    if period == 'PM' and hour <> 12:
        hour += 12
    
    hour_s = "00" if period == 'AM' and hour == 12 else str(hour)

    return str(hour_s) + ampmtime[2:len(ampmtime) - 2]


print(timeConversion("12:59:20AM"))

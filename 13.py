temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(fahrenheit - 32) * (5/9) for fahrenheit in temperatura_fahrenheit]
print(grados_celsius)
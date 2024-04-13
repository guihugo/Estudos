def conversor(h1):
    time_parts = h1.split(':')
    hour = int(time_parts[0])
    minute = time_parts[1]
    second = time_parts[2][:2]  # Remove o 'AM' ou 'PM'

    if 'A' in h1:
        if hour != 12:
            hour += 12
    elif hour == 12:
        hour = 0

    return '{:02d}:{:s}:{:s}'.format(hour, minute, second)

print(conversor('07:05:45AM'))  # Saída esperada: 07:05:45

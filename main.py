p = [3, 10, -6, 0, 8, 122, 14, -30, 12, 4, 200]

s = sorted(p)
print(s)

search_number = int(input("Podaj liczbę:"))

left = 0
right = len(s) - 1

while left <= right:
    mid = (left + right) // 2
    if s[mid] == search_number:
        print(f'Szukana liczba ({search_number}) jest na liście! ')
        break
    elif s[mid] < search_number:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f'Liczby {search_number} nie ma na liście!')

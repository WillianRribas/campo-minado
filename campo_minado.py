def solve_field(field):
    n = len(field)
    m = len(field[0])
    result = [["0" for _ in range(m)] for _ in range(n)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                result[i][j] = "*"
            else:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if is_valid(ni, nj) and field[ni][nj] == "*":
                            result[i][j] = str(int(result[i][j]) + 1)

    return result

def main():
    field_number = 1

    while True:
        try:
            n, m = map(int, input().split())
        except EOFError:
            break

        if n == 0 and m == 0:
            break

        if field_number > 1:
            print()

        field = []
        for _ in range(n):
            try:
                row = input()
            except EOFError:
                break
            field.append(list(row))

        print(f"Field #{field_number}:")
        result = solve_field(field)
        for row in result:
            print("".join(row))
        field_number += 1

if __name__ == "__main__":
    main()

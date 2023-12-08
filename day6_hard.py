times = (41777096)
distances = (249136211271011)


def main():
    s = 0
    for j in range(times):
        if (times-j)*j > distances:
            s += 1
    print(s)

main()
import random, sys, re

def roll(n, sides):
    return [random.randint(1, sides) for _ in range(n)]

def drop_lowest(dice, k):
    s = sorted(dice)
    return s[k:], s[:k]

if __name__ == "__main__":
    # ad-hoc: python dice.py 3d6 2d8 1d20 ...
    for arg in sys.argv[1:]:
        m = re.fullmatch(r"(\d+)d(\d+)", arg)
        n, s = int(m.group(1)), int(m.group(2))
        d = roll(n, s)
        print(f"{arg}: {d} = {sum(d)}")

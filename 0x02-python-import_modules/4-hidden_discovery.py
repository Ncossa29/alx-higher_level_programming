#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    for i in range(len(n)):
        if (n[i][:2] != "__"):
            print(n[i])

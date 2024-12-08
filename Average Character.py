def average_ascii_char(s):
    total_ascii_value = sum(ord(char) for char in s)
    average_ascii_value = total_ascii_value // len(s)
    return chr(average_ascii_value)

if __name__ == "__main__":
    s = input()
    avg_char = average_ascii_char(s)
    print(avg_char)

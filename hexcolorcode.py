import re

if __name__ == "__main__":
    test_string = input("Enter your data: ")
    patterns = r'#([a-fA-F0-9]{6})'
    matches = re.findall(patterns, test_string)
    print('Search results: ', matches)


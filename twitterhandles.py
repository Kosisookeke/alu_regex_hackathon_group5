import re

if __name__ == "__main__":
    test_string = input("Enter your data: ")
    patterns = r'@([a-zA-Z0-9_]+)'
    matches = re.findall(patterns, test_string)
    print('Search results: ', matches)
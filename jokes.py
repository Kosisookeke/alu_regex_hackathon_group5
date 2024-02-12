import re

if __name__ == "__main__":
    test_string = input("Enter your data: ")
    patterns = r'Why did the .*? Because.*?'
    matches = re.findall(patterns, test_string)
    print('Search results: ', matches)

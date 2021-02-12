# 709. To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns the same string
# in lowercase.


# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"


def to_lower_case(str: str) -> str:
    return str.lower()


# print(to_lower_case("Hello"))

def to_lower_case_verbose(str: str) -> str:
    l1 = []  # list to store lower case char

    for c in str:
        if "A" <= c <= "Z":  # check whether the char is uppercase
            unicode = ord(c) + 32  # add 32 unicode value to it
            char = chr(unicode)  # convert into Char
            l1.append(char)
        else:
            l1.append(c)  # add to list as it is in lowercase

    return ("".join(l1))


print(to_lower_case_verbose("Hello"))


def to_lower_case_using_unicode_one_line(str):
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
    # return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)


print(to_lower_case_using_unicode_one_line("Hello"))





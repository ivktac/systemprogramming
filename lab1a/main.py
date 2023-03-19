import re

def generate_word(mask):
    pattern = r"\{(\w),\s*(\d)\}"

    def replace(match):
        letter = match.group(1)
        digit = int(match.group(2))
        return letter * digit
    
    return re.sub(pattern, replace, mask)

if __name__ == "__main__":
    mask = input("Enter a mask: ")
    word = generate_word(mask)

    # open file and write into it
    with open("output.txt", "w") as f:
       f.write(word)

    print("Word generated: " + word)
import random
import string

# generate a random length sized sequence of characters based in a list of valid_chars
def generate_password(length, valid_chars_list):
    password = ''.join(random.choices(valid_chars_list, k=length))
    return password

#Execute code when called from terminal
if __name__ == "__main__":
    
    # List of valid characters to be used as possible values when generating a password
    valid_chars = string.digits + string.ascii_letters + string.punctuation
    # Call for function to generate password
    generated_password = generate_password(16, valid_chars)
    # Print the result from generate_password function
    print(f'Generated password: ', generated_password)
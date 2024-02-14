import os
import sys
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        return f'"{quote_data["content"]}" - {quote_data["author"]}'
    else:
        return "Failed to fetch a quote. Please try again later."

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = "Random Quote Generator"
    print(f'{"-" * 40}\n{" " * 8}{app_name}{" " * 8}\n{"-" * 40}')
    while True:
        user_input = input("Press Enter to get a random quote or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            break

        quote = get_random_quote()
        print("\n", quote, "\n")

if __name__ == "__main__":
    main()

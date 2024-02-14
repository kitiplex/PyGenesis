import os
import sys
import asyncio
from openai import AsyncOpenAI

from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

GPT_MODEL = "gpt-3.5-turbo"

messages = [{
    "role": "system", "content": "Your are a helpful assistant. Follow instructions carefully. Answer as concise as possible."
}]


def print_message(role, content):
    print(f'{role.capitalize()} : {content}', end="")

async def chat_completion():
    while True:
        prompt = input('\nYou: ')
        print("GinaBot: ", end="")

        messages.append(
          {"role": "user", "content": prompt}   
        )

        completion = await client.chat.completions.create(
            model= GPT_MODEL,
            messages=messages,
            temperature=0.8,
            stream=True
        )

        async for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content or "", end="")
        
            if prompt.lower() in ["bye","exit","goodbye","end"]:
                print("Thank you and goodbye!")
                sys.exit()
            else:
                continue


def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = f"GinaBot"
    print(f'{"-" * 38}\n{" " * 12}{app_name}{" " * 12}\n{"-" * 38}')
    asyncio.run(chat_completion())

if __name__ == '__main__':
    main()
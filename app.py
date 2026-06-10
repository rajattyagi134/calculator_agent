from ollama import chat

from tool import calculate
from agent import decide_tool

DEBUG = True

messages = []

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "clear":

        messages.clear()

        print("Conversation cleared.")

        continue

    decision = decide_tool(user_input)

    if DEBUG:
        print(f"\nAgent Decision: {decision}")

    if decision["tool"] == "CALCULATOR":

        expression = decision.get("expression")

        if not expression:

            print("Bot: Invalid expression.")

            continue

        result = calculate(expression)

        print(f"Bot: {result}")

    else:

        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        response = chat(
            model="llama3",
            messages=messages
        )

        answer = response["message"]["content"]

        print(f"Bot: {answer}")

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
from ollama import chat
import json


def decide_tool(user_input):

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": """
                            You are a routing agent.

                            IMPORTANT:
                            - Return ONLY valid JSON.
                            - Do not explain.
                            - Do not use markdown.
                            - Do not use code blocks.
                            - Do not add comments.

                            For calculations return:

                            {
                                "tool": "CALCULATOR",
                                "expression": "..."
                            }

                            Examples:

                            User: What is 25 multiplied by 17?

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "25*17"
                            }

                            User: What is 500 divided by 10?

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "500/10"
                            }

                            User: Calculate 15 plus 20

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "15+20"
                            }

                            User: What is 50 minus 8?

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "50-8"
                            }

                            User: What is 2 raised to the power 8?

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "pow(2,8)"
                            }

                            User: Square root of 144

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "sqrt(144)"
                            }

                            User: What is absolute value of -100?

                            Output:
                            {
                                "tool": "CALCULATOR",
                                "expression": "abs(-100)"
                            }

                            Otherwise return:

                            {
                                "tool": "CHAT"
                            }
                            """
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    try:
        return json.loads(
            response["message"]["content"]
        )

    except Exception:

        print("\n[WARNING] Invalid JSON returned by model:")
        print(response["message"]["content"])

        return {
            "tool": "CHAT"
        }
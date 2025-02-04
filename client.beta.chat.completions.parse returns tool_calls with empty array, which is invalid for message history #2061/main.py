import openai

client = openai.OpenAI()

messages = [
    {"role": "user", "content": "What color is the sky?"},
]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=messages,
)

print(completion.choices[0].message)
messages.append(completion.choices[0].message)
completion.choices[0].message.tool_calls = None  # Hotfix
messages.append(
    {"role": "user", "content": "What color is the ocean?"},
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)

print(completion.choices[0].message)

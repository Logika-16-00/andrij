import g4f

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = g4f.ChatCompletion.create(
        model=("gpt-4"),
        messages=[{"role": "user", "content": user_input}]
    )
    print(response)
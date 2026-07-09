import ollama

def llm(text):
    response = ollama.chat(
        model="qwen3:latest",
        messages=[
            {"role":"user","content":text}
        ]
    )
    print('Answer generated...')

    return(response["message"]["content"])

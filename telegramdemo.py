import requests

def generate_text(model, prompt):
    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-002/jobs",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {model}"
        },
        json={
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.5,
        },
    )

    if response.status_code != 200:
        raise Exception("Failed to generate text")

    return response.json()["choices"][0]["text"]

generated_text = generate_text("<model_api_key>", "Write a story about a dog and a cat who became best friends.")
print(generated_text)


def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot<token>/sendMessage?text={generated_text}&chat_id={chat_id}"
    requests.get(url)

if __name__ == "__main__":
    key = ""
    prompt = ""
    chat_id = ""
    text = generate_text(key, prompt)
    send_message(text, chat_id)

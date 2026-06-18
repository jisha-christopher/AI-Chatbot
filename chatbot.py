from transformers import pipeline

model = pipeline(
    "text-generation",
    model="distilgpt2"
)

def get_response(text):

    prompt = f"""
Customer:{text}
Support:
"""

    output = model(
        prompt,
        max_new_tokens=50
    )

    response = output[0]["generated_text"]

    return response
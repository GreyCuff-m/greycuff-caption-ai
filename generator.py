from transformers import pipeline

caption_generator = pipeline("text-generation", model="gpt2")

def generate_caption(topic, mood, style):
    prompt = f"Write an Instagram caption about {topic} in a {mood} mood with a {style} style. Include emojis and relevant hashtags."
    result = caption_generator(prompt, max_length=60, num_return_sequences=1)[0]
    return result['generated_text']

import openai

# Initialize OpenAI API client
openai.api_key = 'YOUR_API_KEY_HERE'

def generate_story_prompt(prompt: str) -> str:
    """
    Generate story continuation from a prompt using a large language model.
    
    :param prompt: The initial text or prompt for the story.
    :return: Generated story continuation.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.9,
            n=1,
            stop=None
        )
        generated_text = response.choices[0].text.strip()
        return generated_text
    except Exception as e:
        return f"Error generating story: {e}"

# Example usage
user_prompt = "Once upon a time in a mystical land of Everwood, a young adventurer named Aria discovered an ancient map that led to a hidden treasure..."
story_continuation = generate_story_prompt(user_prompt)
print(story_continuation)

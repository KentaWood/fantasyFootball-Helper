import openai
from config import API_KEY

# Set your OpenAI API key
openai.api_key = API_KEY
"""
>>> ask_openai("What is 1 + 1?")
1 + 1 equals 2.
"""
def ask_openai(prompt, model="gpt-4o-mini", max_tokens=250, temperature=0.7):
    """
    Send a prompt to OpenAI GPT model and return the response.

    Parameters:
    - prompt (str): The question or request to send to the model.
    - model (str): The OpenAI model to use (default is 'gpt-4o-mini).
    - max_tokens (int): The maximum length of the response (default is 100).
    - temperature (float): The creativity level of the response (default is 0.7).

    Returns:
    - str: The response from the model.
    """
    
    # Create a chat completion
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "I want you to usually give general advice about who to choose or id it is a good idea to choose this player to be playing in this week's fantasy. and Write your advice in under 150 words"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(ask_openai("What is 1 + 1?"))


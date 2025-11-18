from openai import OpenAI
client = OpenAI(api_key="your-api-key-here")

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "low"},
    instructions="Talk like a baby",
    input="Are semicolons needed in python?"
)
print(response.output_text)

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "high"},
    instructions="Talk like a proffesional software developer",
    input="Are semicolons needed in python?"
)
print(response.output_text)
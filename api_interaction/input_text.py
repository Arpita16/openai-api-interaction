from openai import OpenAI
client = OpenAI(api_key="your-api-key-here")
response=client.responses.create(
    model="gpt-4o",
    input="Write a joke about programmers."
    )
print(response.output_text)








from openai import OpenAI
client = OpenAI(api_key="your-api-key-here")

response = client.responses.create( 
                model="gpt-4o",
                tools= [{"type": "web_search"}],
                input="What is the latest news about OpenAI?"
                )
print(response.output_text)
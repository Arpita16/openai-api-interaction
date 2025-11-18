from openai import OpenAI
client = OpenAI(api_key="your-api-key-here")
response = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Write the name of the characters in this movie"
                },
                {
                    "type": "input_image",
                    "image_url":"https://static.wikia.nocookie.net/insideout/images/1/1c/Inside_Out_Wallpaper.jpeg/revision/latest?cb=20240629233820"
                }
            ]
        }
    ]
)
print(response.output_text)
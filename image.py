import os
import json
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_ENDPOINT_URL_IMAGE"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY_IMAGE"),
)

result = client.images.generate(
    model="Dalle3",
    prompt="A painting of a sunset over a mountain",
    n=1,
)

image_url = json.loads(result.model_dump_json())["data"][0]["url"]

print(image_url)
# URLの画像が有効なのは約5日間。

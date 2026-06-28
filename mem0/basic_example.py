from mem0 import MemoryClient
from dotenv import load_dotenv

load_dotenv()

import os

client = MemoryClient(api_key=os.environ.get('MEM0_API_KEY'))

client.add("I have a meeting at 11 AM tomorrow", user_id="ravindra")

result = client.search("when is my meeting tomorrow?", filters ={'user_id': 'ravindra'})

print(result)

for result in result["results"]:
    if result['score'] > 0.30:
        print(result["memory"])
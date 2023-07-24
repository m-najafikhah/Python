import requests
import argparse
import os
import openai

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help= "The prompt to send to the OpenAI API")
parser.add_argument("file_name", help= "Name of the file to save Python script")
args= parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
#api_key = "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"
api_key = os.getenv("OPENAI_API_KEY") 

request_headers= {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
request_data= {
    "model": "text-davinci-003",
    #"messages": [{"role": "user", "content": "write pythone script for hello world!!"}]
    "prompt": f"Write python script to {args.prompt}.Provide only code, no text",
    "max_tokens": 100,
    "temperature": 0.5
}

response= requests.post(api_endpoint, headers= request_headers, json=request_data)


if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open (args.file_name + ".py", "w") as file:
        file.write(response_text)


else:
    print(f"Request failed!! with status code: {str(response.status_code)}")
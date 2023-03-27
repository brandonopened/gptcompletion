import csv
import requests
import json

# Function to send requests to ChatGPT API
def query_chatgpt(prompt, api_key):
    url = "https://api.openai.com/v1/engines/chatgpt-3.5-turbo/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Replace with your API key from OpenAI
API_KEY = "YOURPROMPTKEY"

# Read prompts from a CSV file
input_file = "prompts.csv"
output_file = "responses.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(["Prompt", "Response"])

    for row in csv_reader:
        prompt = row[0]
        print(f"Processing prompt: {prompt}")

        # Query the ChatGPT API
        response = query_chatgpt(prompt, API_KEY)

        if 'choices' in response:
            answer = response['choices'][0]['text'].strip()
            print(f"Generated response: {answer}")

            # Write the prompt and response to the output CSV file
            csv_writer.writerow([prompt, answer])
        else:
            print("Error: Could not generate a response")

print("Done!")

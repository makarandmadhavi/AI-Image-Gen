import requests
import json
import os
import random
import string
import argparse
import time

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("prompt_file", help="path to the text file containing prompts")
args = parser.parse_args()

# Set the API endpoint URL
url = "https://stablediffusionapi.com/api/v3/text2img"

# Read the prompt file into a list of lines
with open(args.prompt_file) as f:
    prompt_lines = f.readlines()

# Remove any leading/trailing whitespace from each line
prompt_lines = [line.strip() for line in prompt_lines]

# Generate a list of request payloads for each prompt line
payloads = [
    {
        "key": "pVpYOg0B3fPrRGnCpuIcVz7FPYUAYy3GQSaOGJSrWpIsUsvw5ApmywfAagyp",
        "model_id": "midjourney",
        "prompt": line,
        "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
        "width": "1024",
        "height": "1024",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "webhook": None,
        "track_id": None
    } for line in prompt_lines
]

# Send the POST request for each prompt line
for i, payload in enumerate(payloads):
    # Send the POST request
    response = requests.post(url, json=payload)

    # Generate a random filename for the response JSON file
    filename = f"response_{i}.json"


    # Wait for 33 seconds before sending the next request (API rate limit)
    time.sleep(33)


'''
    # Save the response JSON to a file in the same directory as the script
    with open(os.path.join(os.getcwd(), filename), 'w') as f:
        json.dump(response.json(), f)
'''
import requests
import json
import os
import random
import random
import csv

import itertools


# List of landscapes and subcategories
landscapes = {
    "mountain": ["range", "peak", "valley", "canyon"],
    "forest": ["dense forest", "rainforest", "autumn forest", "bamboo forest"],
    "beach": ["tropical beach", "rocky beach", "sandy dune", "coral reef"],
    "riverside": ["river valley", "waterfall", "rapids", "marsh"]
}

# List of weather conditions
weather = ["sunny", "cloudy", "rainy", "stormy", "foggy", "snowy"]

# List of times of day
times_of_day = ["daytime", "nighttime", "dusk", "dawn"]

# List of lighting conditions
lighting = ["morning", "midday", "night", "overcast"]

# List of camera angles
angles = ["low angle", "high angle", "wide angle", "telephoto"]

# List of camera distances
distances = ["close-up", "medium shot", "long shot"]

# List of additional environmental factors
factors = ["windy", "foggy", "rainy", "snowy"]

# Generate all possible prompts
prompts = {}
for landscape, subcategories in landscapes.items():
    landscape_prompts = []
    for subcategory in subcategories:
        for weather_condition, time_of_day, lighting_condition, angle, distance, factor in itertools.product(weather, times_of_day, lighting, angles, distances, factors):
            prompt = f"Generate a photo-realistic image of a {weather_condition} {time_of_day} {landscape} ({subcategory}) landscape with {lighting_condition} lighting, taken from a {angle} {distance} and with {factor} environmental conditions."
            landscape_prompts.append(prompt)
    prompts[landscape] = landscape_prompts

allprompts = []
# Print the prompts for each landscape
for landscape, landscape_prompts in prompts.items():
    print(f"Prompts for {landscape}:")
    print(len(landscape_prompts))
    for prompt in landscape_prompts:
        allprompts.append(prompt)

len(allprompts)
url = "https://stablediffusionapi.com/api/v3/text2img"

# payload = {
#         "key": "pVpYOg0B3fPrRGnCpuIcVz7FPYUAYy3GQSaOGJSrWpIsUsvw5ApmywfAagyp",
#         "model_id": "midjourney",
#         "prompt": allprompts[1],
#         "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
#         "width": "1024",
#         "height": "1024",
#         "samples": "1",
#         "num_inference_steps": "20",
#         "seed": None,
#         "guidance_scale": 7.5,
#         "safety_checker": "yes",
#         "webhook": None,
#         "track_id": None
#     }

for i in range(0,40):
    # Choose the type of landscape to generate
    prompt = random.choice(prompts["riverside"])
    payload = {
        "key": "pVpYOg0B3fPrRGnCpuIcVz7FPYUAYy3GQSaOGJSrWpIsUsvw5ApmywfAagyp",
        "model_id": "midjourney",
        "prompt": prompt,
        "negative_prompt": "((out of frame)), ((extra fingers)), mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), (((tiling))), ((naked)), ((tile)), ((fleshpile)), ((ugly)), (((abstract))), blurry, ((bad anatomy)), ((bad proportions)), ((extra limbs)), cloned face, (((skinny))), glitchy, ((extra breasts)), ((double torso)), ((extra arms)), ((extra hands)), ((mangled fingers)), ((missing breasts)), (missing lips), ((ugly face)), ((fat)), ((extra legs)), anime",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "webhook": None,
        "track_id": None
    }
    response = requests.post(url, json=payload)
    response = response.json()
    filename = "response_" + str(response["id"]) +".json"
    print(response)
    with open(os.path.join(os.getcwd(), filename), 'w') as f:
        json.dump(response, f)
    
    
    # write response to CSV file

    with open('response.csv', mode='a', newline='') as response_file:
        writer = csv.writer(response_file)
        writer.writerow([response['status'], response['generationTime'], response['id'], response['output'], response['meta']])

    # download image and store it in a folder
    image_url = response['output'][0]
    response_image = requests.get(image_url)
    with open('riverside/riverside_'+str(response['id'])+'.png', mode='wb') as image_file:
        image_file.write(response_image.content)


import sys, json, requests
import simplejson as json
import os
import zipfile

collection_name = 'Google%20Scanned%20Objects'
owner_name = 'GoogleResearch'
# The server URL
base_url ='https://fuel.ignitionrobotics.org'
# Path to get the models in the collection
next_url = '/1.0/models?page=2&per_page=100&q=collections:{}'.format(collection_name)
next_url = '/1.0/models?per_page=100&page={}&q=collections:Google%20Scanned%20Objects'
# Path to download a single model in the collection
download_url = 'https://fuel.ignitionrobotics.org/1.0/{}/models/'.format(owner_name)
count = 0
total_count = 0
# Iterate over the pages
# while next_url:
downloaded = {}

os.makedirs('google_scanned_models/', exist_ok=True)

for i in range(1, 1100):
    print(count)
    # Get the contents of the current page.
    try:
        r = requests.get(base_url + next_url.format(str(i)))
        models = json.loads(r.text)
    except:
        continue

    for model in models:
        model_name = model['name']
        print(f"Downloading ({count + 1}/{total_count}) {model_name}")
        model_url = download_url + model_name + '.zip'
        model_path = f"google_scanned_models/{model_name}.zip"
        
        # Download the model
        with requests.get(model_url, stream=True) as r:
            with open(model_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        # Unzip the model
        with zipfile.ZipFile(model_path, 'r') as zip_ref:
            zip_ref.extractall(f"google_scanned_models/{model_name}")
        
        count += 1
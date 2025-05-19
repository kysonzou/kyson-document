import os
import re
import requests

def download_image(url, local_path):
    """Download an image from a URL to the specified local path."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download {url}")

def replace_network_images(note_path, assets_dir):
    """Replace network images in the note with local images in assets_dir."""
    with open(note_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find all image URLs (e.g., ![alt text](https://example.com/image.png))
    image_urls = re.findall(r'!\[.*?\]\((http[s]?://.*?)\)', content)
    base_name = os.path.splitext(os.path.basename(note_path))[0].replace(" ","")

    for idx, url in enumerate(image_urls, start=1):
        local_image_name = f"{base_name}-{idx}.png"
        local_image_path = os.path.join(assets_dir, local_image_name)

        # Download and save image
        download_image(url, local_image_path)

        # Replace URL with local path in the note content
        content = content.replace(url, f"../Assets/{local_image_name}")

    # Save the updated note
    with open(note_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_notes_folder(notes_folder, assets_dir):
    """Process all notes in the folder to replace network images with local images."""
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    for root, _, files in os.walk(notes_folder):
        for file in files:
            if file.endswith(".md"):  # Only process Markdown files
                note_path = os.path.join(root, file)
                replace_network_images(note_path, assets_dir)
                print(f"Processed {note_path}")

# Example usage
notes_folder = "02-Notes"  # Replace with your actual notes folder path
assets_dir = "03-Assets"
process_notes_folder(notes_folder, assets_dir)


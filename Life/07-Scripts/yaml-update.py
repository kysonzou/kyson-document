import os
import re
import yaml  # PyYAML
from datetime import datetime
from pathlib import Path


def get_file_times(file_path):
    path = Path(file_path)
    
    # Get the creation time (birth time) if available, otherwise use st_ctime
    if hasattr(path.stat(), 'st_birthtime'):
        creation_time = path.stat().st_birthtime
    else:
        creation_time = path.stat().st_ctime
    
    modification_time = path.stat().st_mtime

    # Format times as "YYYY-MM-DD HH:mm"
    creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M')
    modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M')
    return creation_date, modification_date

def adjust_yaml_in_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Match YAML front matter
            yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                data = yaml.safe_load(yaml_content)
                
                # Modify YAML data
                if 'category' in data  and 'subtags' in data:
                    # original_category = data['category']
                    # original_tags = data['tags']
                    
                    # Swap category and tags, and add subtags after tags
                    #data['category'] = original_tags
                    #data['subtags'] = original_category

                    
                    # Get file creation and modification dates
                    #creation_date, modification_date = get_file_times(file_path)

                    # Re-order category to be the first key
                    ordered_data = {'category': data['category'],
                                    'tags': data['subtags']}

                    for key, value in data.items():
                        if key in ('status' , 'assistance'):
                            ordered_data[key] = value

                    
                    # Reconstruct the YAML front matter
                    new_yaml_content = yaml.dump(ordered_data, allow_unicode=True , sort_keys=False)
                    new_content = f"---\n{new_yaml_content}---\n" + content[yaml_match.end():]
                    
                    # Write back the modified content
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                        
            print(f"Processed: {filename}")

# 调用函数，并指定Obsidian文件夹路径
adjust_yaml_in_files('02-Notes')
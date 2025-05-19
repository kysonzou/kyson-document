import os
import yaml
import re 

def read_yaml_content(filepath):
    """从文件中读取 YAML 数据。"""

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Match YAML front matter
    yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        data = yaml.safe_load(yaml_content)
        return data



def write_yaml_content(filepath, yaml_data):
    """将 YAML 数据写入指定文件。"""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('---\n')
        yaml.dump(yaml_data, file, allow_unicode=True, sort_keys=False)
        file.write('---\n')

def process_files(directory_path):
    """遍历文件，检查和生成 tags-index 文件。"""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                yaml_data = read_yaml_content(filepath)

                if yaml_data:
                    # 检查 YAML 中是否包含有效的 tags
                    tags = yaml_data.get('tags')
                    if tags:
                        if not isinstance(tags, list):
                            tags = [tags]  # 若 tags 不是列表，则转换成列表

                        for tag in tags:
                            index_file_name = f"{tag}-index.md"
                            index_file_path = os.path.join(root, index_file_name)

                            # 如果 tags-index 文件不存在，则创建
                            if not os.path.exists(index_file_path):
                                new_yaml_data = yaml_data.copy()
                                new_yaml_data['assistance'] = "true"
                                write_yaml_content(index_file_path, new_yaml_data)
                                print(f"Created {index_file_name} with assistance: true")

# Obsidian 文件目录

process_files('02-Notes')
import pytest
import yaml


class YamlReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_yaml(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"错误: 文件 {self.file_path} 未找到。")
            return None
        except yaml.YAMLError as e:
            print(f"错误: 解析 YAML 文件时出错: {e}")
            return None

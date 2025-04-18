import allure
import pytest

from utils.yaml_tool import YamlReader

yaml_reader = YamlReader("test_case/test_quan_app_content/test_quan_app_content.yaml")
case_config = yaml_reader.read_yaml()
skip_boolean = False

@pytest.mark.online
@allure.title("测试用例示例")
@allure.description("这是一个完整的测试用例示例，包含标签、严重级别、步骤和附件。")
@allure.tag("example", "demo")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.skipif(skip_boolean, reason="由于条件为真，跳过此测试用例")
def test_function():
    result = 1 + 1
    assert result == 2

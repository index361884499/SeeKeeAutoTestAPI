import time

import pytest
import os

if __name__ == "__main__":
    # 定义测试用例所在的目录
    test_dir = "test_case"
    # 定义 Allure 结果文件的存放目录
    allure_results_dir = "allure/results"
    # 定义 Allure 测试报告的存放目录
    curTime = time.strftime("%Y%m%d-%H%M%S")
    allure_report_dir = f"allure/reports/{curTime}"

    # 执行 Pytest 测试用例，并将结果保存到 allure_results_dir
    pytest.main([
        "-s",  # 显示标准输出
        "-v",  # 详细输出
        f"--alluredir={allure_results_dir}",
        test_dir
    ])

    # 检查系统是否安装了 Allure 命令行工具
    allure_available = os.system("allure --version") == 0

    if allure_available:
        # 生成 Allure 测试报告
        os.system(f"allure generate {allure_results_dir} -o {allure_report_dir} --clean")
        print(f"Allure 测试报告已生成，路径为: {allure_report_dir}")
    else:
        print("未检测到 Allure 命令行工具，请先安装 Allure 以生成测试报告。")
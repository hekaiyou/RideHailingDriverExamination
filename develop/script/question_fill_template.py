import os
import sys
# pip install pyperclip
import pyperclip as poc


def tool_fill_template(question_md_file):
    # 项目根目录路径
    project_directory = "./"
    # 初始化内容模板
    template_content = (
        """现在需要开发一个出租车司机从业资格模拟考试系统, 目前已经在 `develop/demo/index-tailwindcss.html` 文件里实现一个静态网站。
一、具体业务流程: 管理员在后台开通账户密码后, 出租车司机作为学员, 使用这个账户密码可以登录系统进行选择一个课程进行【顺序练习】、【模拟考试】、查看【我的错题】。
二、核心功能:
    1、运营后台 (移动端H5):
        学员管理页: 新增学员, 学员信息包括姓名（必填）、身份证号（必填）、手机号选填；支持编辑、删除、查询学员信息
    2、学员使用端 (移动端H5):
        • 登录页: 身份证登录, 身份证号输入框、密码输入框（红字提示：密码默认身份证号后六位）, 点击【确认】按钮, 完成的登录；注意, 这里登录的账号密码校验的是, 这个身份证号是否在【运营后台-学员管理页】存在, 同时判断这个密码是否为【身份证号后6位】;
        • 登录后, 有两个菜单: 【我的课程】、【个人中心】默认定位到【我的课程】页; 【我的课程】和【个人中心】使用两个tap菜单分开
        • 【我的课程】页: 两行显示两个课程, 每行都有一个图片加文字；文字就是课程标题，两行标题分别是：【长沙市网络预约出租车驾驶员区域科目从业资格培训】、【长沙市网络预约出租车驾驶员公共科目从业资格培训】；点击每个课程，进入【课程学习页】；
        • 【课程学习】页: 有三个模块，分别是【顺序练习】、【模拟考试】、【我的错题】，点击每个模块分别进入对应模块的页面
        • 【顺序练习】页: 页面结构如下--页面上半部分显示题目和选项, 页面底部有5个按钮【上一题】、【结束练习】、【下一题】、【选题】、重做; 本页面一共轮播500道题; 题目显示不同的题型; 比如判断题、单选题，每次答对，自动进入下一题；若答错，在选项中将正确答案打勾并标记绿色，错误答案前打叉并标红色，需手动点击下一题；【选题弹框样式，：将所有题目序号列出来，可点击具体题目序号】
        • 【模拟考试】页: 显示开始规则 (规则内容--1、考试科目: 长沙市网络预约出租车驾驶员区域科目从业资格培训模拟考试; 2、试题数量: 50题; 3、考试时间: 60分钟; 4、通过标准: 满分50分, 40分通过)，点击【开始模拟考试】，进入考试页面，页面结构如下--页面上半部分显示题目和选项, 页面底部有5个按钮【上一题】、【下一题】、【选题】、【60分钟倒计时】、【交卷】; 本页面一共轮播50道题; 题目显示不同的题型, 比如判断题、单选题; 每次答对, 自动进入下一题; 若答错, 在选项中将正确答案打勾并标记绿色，错误答案前打叉并标红色，需手动点击下一题；点【交卷】按钮之后，显示模拟考试成绩；若考试倒计时结束，则自动提交提交，并显示模拟考试成绩。点击【交卷】按钮，如果全部题目没有做完，弹框提示：还有未完成题目，确定提交么？
        • 【我的错题】页: 本页面汇总在【顺序练习】、【模拟考试】页面答错的题目, 对这些题目重新作答, 答对则将该题从本页面移除。\n"""
    )
    files_to_read_file_list = [
        'develop/demo/index-tailwindcss.html',
        'ride_hailing_driver_examination/manage.py',
        'ride_hailing_driver_examination/my_app/__init__.py',
        'ride_hailing_driver_examination/my_app/admin.py',
        'ride_hailing_driver_examination/my_app/apps.py',
        'ride_hailing_driver_examination/my_app/models.py',
        'ride_hailing_driver_examination/my_app/tests.py',
        'ride_hailing_driver_examination/my_app/views.py',
    ]
    files_to_read_dir_list = [
        'ride_hailing_driver_examination/ride_hailing_driver_examination',
        'ride_hailing_driver_examination/templates',
    ]
    # 需要读取的文件及其在模板中的标识符
    files_to_read = {}
    # 读取 files_to_read_file_list 列表中指定的文件, 并将其添加到 files_to_read 字典中
    for file_path in files_to_read_file_list:
        # 获取文件扩展名, 去除点号
        file_ext = os.path.splitext(file_path)[1][1:]
        # 将文件路径和扩展名添加到 files_to_read 字典中
        files_to_read[file_path] = file_ext
    # 遍历 files_to_read_dir_list 列表中指定的目录及其子目录
    for dir_path in files_to_read_dir_list:
        # 使用 os.walk 遍历目录树
        for root, dirs, files in os.walk(os.path.join(project_directory, dir_path)):
            for file in files:
                if '.DS_Store' in file or '.gitkeep' in file or '.pyc' in file:
                    continue
                # 构建文件的完整路径
                full_path = os.path.join(root, file)
                # 获取文件相对于项目根目录的相对路径
                relative_path = os.path.relpath(full_path, project_directory)
                # 获取文件扩展名, 去除点号
                file_ext = os.path.splitext(file)[1][1:]
                # 将文件的相对路径和扩展名添加到 files_to_read 字典中
                files_to_read[relative_path] = file_ext
    # 读取每个文件的内容并填充到模板中
    for file_path, language in files_to_read.items():
        full_path = os.path.join(project_directory, file_path)
        # 确定文件是否存在
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                file_content = f.read()
                template_content += (
                    f"\n{file_path}\n```{language}\n{file_content}\n```\n"
                )
        else:
            template_content += f"\n{file_path} 不存在或无法读取\n"
            print(f"警告: {file_path} 不存在或无法读取")
    # 读取问题文件的内容并填充到模板中
    with open(question_md_file, "r", encoding="utf-8") as f:
        question_content = f.read()
        template_content += f"\n{question_content}"
    # 打印模板内容
    # print(template_content)
    # 保存为输出文件
    with open(
        os.path.join(project_directory, "develop/cache/AICodeAsks.md"),
        "w",
        encoding="utf-8",
    ) as output_file:
        output_file.write(template_content)
    # 将 template_content 的内容复制到系统剪贴板
    poc.copy(template_content)
    print("模板内容已复制到系统剪贴板")
    # 在同目录下查看是否存在 AICodeAnswer.md 文件
    if not os.path.exists(os.path.join(project_directory, "develop/cache/AICodeAnswer.md")):
        # 没有时创建一个空的文本文件
        with open(
            os.path.join(project_directory, "develop/cache/AICodeAnswer.md"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write("")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python question_fill_template.py <question_md_file>")
    else:
        question_md_file = str(sys.argv[1])
        tool_fill_template(question_md_file)

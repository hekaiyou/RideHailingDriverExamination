import os
import sys
# pip install pyperclip
import pyperclip as poc


def tool_fill_template(question_md_file):
    # 项目根目录路径
    project_directory = "./"
    # 初始化内容模板
    template_content = (
        """有一个 UE 插件 `UeInputReplay`, 用于录制玩家的输入, 然后回放, 代码如下。\n"""
    )
    files_to_read_file_list = [
        'README.md',
        'UeInputReplay/UeInputReplay.uplugin',
    ]
    files_to_read_dir_list = [
        'UeInputReplay/Source',
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
                if '.DS_Store' in file:
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

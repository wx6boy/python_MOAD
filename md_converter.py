import os
from sys import argv


def create_md(path):
    files_list = []
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py') and filename != os.path.basename(__file__):
                check_substring = True
                with open(path + "/" + filename) as f:
                    if "# title" in f.read():
                        files_list.append(os.path.join(dirname, filename))

    md_path = path + "/" + path.split("/")[-1] + ".md"

    if os.path.exists(md_path):
        os.remove(md_path)

    if files_list:

        f = open(md_path, 'a+')
        f.write("#" + path.split("/")[-1] + "\n\n")
        f.close()

        titles = []

        for current_file in files_list:
            f = open(current_file)
            line = f.readline()
            line = line.replace("# title", "") + ""
            line = line.replace("\n", "") + ""
            titles.append(line)
            f.close()

        for i in range(len(titles)):
            title = titles[i]
            titles[i] = f'+ [{title}](#{title})\n'
        titles = ''.join(titles)

        f = open(md_path, 'a+')
        f.write(titles)
        f.close()

        for current_file in files_list:
            f = open(current_file)
            lines = f.readlines()

            for i in range(len(lines) - 1):
                line = lines[i]
                if line.startswith('# title'):
                    lines[i] = line.replace("# title", "\n##") + "\n"
                elif line.startswith('# description'):
                    lines[i] = line.replace("# description", "") + "\n"
                elif line.startswith('# code'):
                    lines[i] = '```python\n'
            lines.append('\n```\n')
            f = open(md_path, 'a+')
            f.write(''.join(lines))
            f.close()


if __name__ == "__main__":
    if len(argv) < 2:
        print("You need to write in parameter directory to catalog of .py files.")
    else:
        file_directory = argv[1]
        if os.path.exists(file_directory) and os.path.isdir(file_directory):
            create_md(file_directory)
        else:
            print("No such directory")

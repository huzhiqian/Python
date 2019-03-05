import os
import time

path = r"D:\SaveImage_2019_3_2"


def get_all_file():
    for root, dirs, files in os.walk(path):
        print("当前目录路径:{0}\n".format(root))
        print("当前路径下所有子目录:{0}\n".format(dirs))
        print("当前路径下所有文件:{0}\n".format(files))
        for item in files:
            print("文件名：{0}".format(item))

        print("文件总数：{0}".format(len(files)))


start_time = time.process_time_ns()
get_all_file()
end_time = time.process_time_ns()
print("耗时：{0}".format(str((end_time-start_time)/1000000)))


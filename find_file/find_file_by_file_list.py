import os

if __name__ == '__main__':
    base = os.path.curdir
    again = True
    while again:
        input_list = input("请输入：").split(' ')
        for root, dirs, files in os.walk(base):
            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list

            # 遍历文件
            for f in files:
                s = os.path.join(root, f)
                flag = False
                for t in input_list:
                    if t.lower() not in f.lower():
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    print(s)

            # 遍历所有的文件夹
            # for d in dirs:
            #     print(os.path.join(root, d))
        # if input("是否继续：（Y）？").lower() == 'y':
        #     again = True
        # else:
        #     again = False

import os
# 5-6, 9-20
path = "C:\\**\\C\\input"
fileName = "input"
nowIndex = 1
# 重命名
for i in range(1, 21):
    nowFile = fileName + str(i) + ".txt"
    if os.path.exists(os.path.join(path, nowFile)):
        if i != nowIndex:
            os.rename(os.path.join(path, nowFile), os.path.join(path, fileName + str(nowIndex) + ".txt"))
            print(nowFile + "重命名为" + fileName + str(nowIndex) + ".txt")
        nowIndex += 1
    else:
        print(nowFile + "不存在")



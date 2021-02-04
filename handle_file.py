import os
from PIL import Image


def circle(filePath, fn, item_data):
    w = item_data['size']
    """ 把图片变成圆形图片。fn：图片路径 """
    ima = Image.open(fn).convert("RGBA")
    ima = ima.resize((w, w), Image.ANTIALIAS)
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    # 最后生成圆的半径
    r3 = w // 2
    imb = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
    pima = ima.load()  # 像素的访问对象
    pimb = imb.load()
    r = float(r2 / 2)  # 圆心横坐标

    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r)  # 到圆心距离的横坐标
            ly = abs(j - r)  # 到圆心距离的纵坐标
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径

            if l < r3:
                pimb[i - (r - r3), j - (r - r3)] = pima[i, j]

    save_dir = f"{filePath}\daxigua\\res\\raw-assets\\{item_data['fileName'][0:2]}\\{item_data['fileName']}"
    imb.save(save_dir)


def pre_handle(filePath):
    flag = True
    names = os.listdir(filePath)
    for name in names:
        filename = name.split('.')[0]
        item_data = get_filename_size(filename)
        if name == "daxigua":
            flag = False
        if item_data == None:
            continue
        circle(filePath, f"{filePath}\{name}", item_data)
    if flag:
        raise Exception("请检查文件是否配置完整!")


# 根据名字获取文件名和文件大小
def get_filename_size(name):
    data = [
        {
            "name": "葡萄",
            "fileName": "ad16ccdc-975e-4393-ae7b-8ac79c3795f2.png",
            "size": 52
        },
        {
            "name": "樱桃",
            "fileName": "0cbb3dbb-2a85-42a5-be21-9839611e5af7.png",
            "size": 80
        },
        {
            "name": "橘子",
            "fileName": "d0c676e4-0956-4a03-90af-fee028cfabe4.png",
            "size": 108
        },
        {
            "name": "柠檬",
            "fileName": "74237057-2880-4e1f-8a78-6d8ef00a1f5f.png",
            "size": 119
        }, {
            "name": "猕猴桃",
            "fileName": "132ded82-3e39-4e2e-bc34-fc934870f84c.png",
            "size": 153
        },
        {
            "name": "西红柿",
            "fileName": "03c33f55-5932-4ff7-896b-814ba3a8edb8.png",
            "size": 183
        }, {
            "name": "桃",
            "fileName": "665a0ec9-6c43-4858-974c-025514f2a0e7.png",
            "size": 193
        },
        {
            "name": "菠萝",
            "fileName": "84bc9d40-83d0-480c-b46a-3ef59e603e14.png",
            "size": 258
        }, {
            "name": "椰子",
            "fileName": "5fa0264d-acbf-4a7b-8923-c106ec3b9215.png",
            "size": 308
        }, {
            "name": "西瓜",
            "fileName": "564ba620-6a55-4cbe-a5a6-6fa3edd80151.png",
            "size": 318
        }, {
            "name": "大西瓜",
            "fileName": "5035266c-8df3-4236-8d82-a375e97a0d9c.png",
            "size": 408
        },
    ]
    for item in data:
        if name == item['name']:
            return item
    return None


if __name__ == '__main__':
    pre_handle('F:\\桌面\\合成大西瓜\\')



def reader_from_file(path):
    '''
    从csv中读取
    :param path:
    :return: 从文件中读取后生成的列表
    '''
    list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            tl = [int(q) for q in line[0].split(" ")]
            list.append(tl)

    return list
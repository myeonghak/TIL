# 1. 매 줄마다 "1. 2. 3. ..." 넘버링
# 2. LS 토큰은 줄바꿈 뒤 한칸 들여 쓰기 (\n\t)
# 3. 라인마다 한 줄씩 띄우기 (\n -> \n\n)

def TIL_process(file_name):
    with open(f"G:\내 드라이브\노트목록\{file_name}", 'r', encoding="UTF-8") as file:
        data = file.read()#.replace('\n', '')

    title=data[:data.index("\n\n")]

    LS_token="\u2028"

    num_of_line=data.count("\n")

    if data[-1:]=="\n":
        data=data[:-1]

    for i in range(num_of_line):
        if (i==0) :
            data=data.replace("\n",f"gongbackgongback",1)
        else:
            data=data.replace("\n",f"gongbackgongback{i}. ",1)

    data=data.replace("gongback","\n")

    data=data.replace(LS_token,"\n\t")

    with open(f'C:\\Users\\nilsi\\Desktop\\TIL_result\\{file_name}', 'w', encoding="UTF-8") as file:
        file.write(data)
        
    return True

import os

TIL_list=[file for file in os.listdir('G:\내 드라이브\노트목록') if "[TIL]" in file]

for file_name in TIL_list:
    try:
        # print(file_name)
        TIL_process(file_name)
    except:
        print(f"something's wrong with {file_name}")
        with open(f"G:\내 드라이브\노트목록\{file_name}", 'r', encoding="UTF-8") as file:
            data = file.read()#.replace('\n', '')
        with open(f'C:\\Users\\nilsi\\Desktop\\TIL_result\\{file_name}', 'w', encoding="UTF-8") as file:
            file.write(data)
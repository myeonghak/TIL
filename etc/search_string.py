import os

def search_string_in_file(py_path, text_to_search):
    with open(py_path, "r",encoding='utf-8-sig') as text_file:
        data=text_file.readlines()
    data="".join(data)
    if text_to_search in data:
        print(py_path)
        return True
    

def traverse_dir(dir_path,tar_extension, text_to_search):
    
    for entity in os.listdir(dir_path):
        if "." in entity:
            if "."+tar_extension in entity:
                try:
                    search_string_in_file(dir_path+"\\"+entity, text_to_search)
                except:
                    pass
        else:
            traverse_dir(dir_path+"\\"+entity, tar_extension, text_to_search)
            
traverse_dir(r"C:\Users\nilsi\anaconda3\Lib\site-packages\shap","py","summary_plot")
import os,shutil

dict_extension = {
    "audio_extension"  : (".mp3",".m4a",".wav",".flac"),
    "video_extension"  :(".mp4",".mkv",".flv",".mpeg",".3gp",".wemb"),
    "documents_extension"  : (".doc",".pdf",".txt",".xlsx",".pptx",".PDF",".xls"),
    "pic_extension"  : (".png","JPEG",".jpg"),
    "zip_extension" :(".zip","tar.gz",".dmg"),
    "application_extension":(".exe",".msi")
}
folderpath = input("Enter Folder Path : ");

# def file_finder(folderpath,file_extensions):
#     files =[]
#     for file in os.listdir(folderpath):
#         for extension in file_extensions:
#             if file.endswith(extension):
#                 files.append(file)
#     return files
file_finder = lambda folderpath,file_extensions:[file  for extension in file_extensions for file in os.listdir(folderpath) if file.endswith(extension)]
# print(file_finder(folderpath,documents_extension))
try:
    for extension_type,extension_tuple in dict_extension.items():
        for file in os.listdir(folderpath):
            for extension in extension_tuple:
                if file.endswith(extension):
                    folder_name = extension_type.split("_")[0]+"Files"
                    folder_path =os.path.join(folderpath,folder_name)
                    if os.path.exists(folder_path) : 
                        pass;
                    else:
                        os.mkdir(folder_path);
                else:
                    pass;

        for item in  file_finder(folderpath,extension_tuple):
            item_path =os.path.join(folderpath,item);
            item_new_path = os.path.join(folder_path,item);
            shutil.move(item_path,item_new_path);

        print("Calling File Finder");
        file_finder(folderpath,extension_tuple);
except Exception as error:
    print(error);
    
                


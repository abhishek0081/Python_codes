# w : write mode  it will delete file if it is in that diractory and create a new file
# a : will overwrite the data if it find the file then it will start writing that file
# if can't  file new file will be created
# r+ : raead as well as write at the same time but it will not create file 

with open("name.xyz","r+") as f:
    f.seek(len(f.read()));
    f.write("Yo Hi There : \n");
    # f.read("")
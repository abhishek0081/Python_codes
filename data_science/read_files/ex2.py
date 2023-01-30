# from os import readlink


# with open("read.html","r") as rf:
#     with open("r1.txt","w") as wf:
#         for line in rf.readlines():
#             if "<a href=" in line:
#                 pos =line.find("<a href=");
#                 first_quote = line.find("\"",pos);
#                 second_quote = line.find("\"",first_quote+1);
#                 url = line[first_quote+1:second_quote];
#                 wf.write(url+"\n");


# BETTER SOLUTION
with open("read.html","r") as rf:
    with open("r1.txt","w") as wf:
        page = rf.read()
        link_exist = True
        while link_exist:
            pos = page.find("<a href=")
            if pos ==-1:
                link_exist = False
            else:
                first_quote = page.find("\"",pos);
                second_quote = page.find("\"",first_quote+1);
                url = page[first_quote+1:second_quote];
                wf.write(url+"\n");
                page= page[second_quote:]

                


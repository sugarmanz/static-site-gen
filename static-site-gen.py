"""
static-site-gen.py

This program allows a user to quickly fill out '.html'
templates using various text files. The goal is to allow
a user to develop a website using variables and then be
able to quickly fill in the variables by running this
program and save the new '.html' file without destroying
the old. This allows for very quick changes to one text
file that will change the rest of the website, saving
lots of precious time. There are several different useful
operations a user may do, such as create a post or change
the config.txt file.

Author: Jeremiah Zucker
"""

import os
import shutil
from django.utils.datetime_safe import datetime

class Post:
    attributes = ["name","date","description","full"]
    def __init__(self, name, date, description, full):
        self.name = name
        self.date = date
        self.description = description
        self.full = full

    def get(self, arg):
        if arg == "name":
            return self.name
        elif arg == "date":
            return self.date
        elif arg == "description":
            return self.description
        elif arg == "full":
            return self.full
        else:
            return None

def main():
    checkReadme()
    checkDir()
    checkConfig()
    info = dict()
    task = input("What would you like to do? ('h' for help) ")
    while (task != "q" and task != "Q"):
        info = fillDict(info)
        if (task == "a" or task == "A"):
            createPost()
        elif (task == "g" or task == "G"):
            print("Generate site.")
            createSite(info)
        elif (task == "h" or task == "H"):
            print("(A)dd posts, (G)enerate pages, (H)elp, (I)nformation, (U)pdate config.txt, (Q)uit")
        elif (task == "i" or task == "I"):
            file = open("README.txt","r")
            print(file.read())
            file.close()
        elif (task == "u" or task == "U"):
            print("Update config.txt")
            updateConfig()
        else:
            print("Not a valid command. Type 'h' for a list of valid commands.")
        task = input("What would you like to do? ")
    input("Press ENTER to close.")
    return

def checkReadme():
    try:
        Readme = open("README.txt")
    except FileNotFoundError:
        print("Writing README...")
        Readme = open("README.txt","a+")
        Readme.write("README.txt for static-site-gen.py\nauthor: Jeremiah Zucker \nemail: jrz6220@rit.edu\n")
        Readme.write("\nThis program is a simple static site generator.\nIt will create all of the necessary directories for you.\n")
        Readme.write("The only necessary action for you to take is to \nfill in all of the information. You may create posts, pages,\n")
        Readme.write("and update information all from the terminal when\nis running this program.\n")
        Readme.write("\n1. Drop 'static-site-gen.py' into a folder, preferably empty.\n")
        Readme.write("2. Run the program.\n")
        Readme.write("3. Follow prompts and fill out info.\n")
        Readme.write("4. Final .html files will be in 'SiteHTMLs' folder.\n")
        Readme.write("5. Upload .html files to where ever you are hosting your site.\n")
        Readme.write("6. Run program whenever you have more info to add and re-upload.\n")
        Readme.write("7. Enjoy!\n")
        print("Finished writing README.")
    Readme.close()

def checkDir():
    print("Checking directory...")
    setupDir()

def checkConfig():
    filename = "Content/config.txt"
    try:
        config = open(filename,"r")
    except FileNotFoundError:
        if (input("Config.txt not found. Setup directory? (y/n) ") == "y"):
            setup()
        else:
            print("Setup cancelled.")
            input("Press ENTER to close.")
            return
        config = open(filename,"r")
    config.close()

def setup():
    setupConfig()
    moreInfo()

def setupDir():
    RootName = os.getcwd()
    print("Creating Content folder...")
    if not os.path.exists(RootName+"\Content"):
        os.makedirs(RootName+"\Content")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating Content\Images folder...")
    if not os.path.exists(RootName+"\Content\Images"):
        os.makedirs(RootName+"\Content\Images")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating Content\Posts folder...")
    if not os.path.exists(RootName+"\Content\Posts"):
        os.makedirs(RootName+"\Content\Posts")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating Content\Videos folder...")
    if not os.path.exists(RootName+"\Content\Videos"):
        os.makedirs(RootName+"\Content\Videos")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating Templates folder...")
    if not os.path.exists(RootName+"\Templates"):
        os.makedirs(RootName+"\Templates")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating Templates\Posts folder...")
    if not os.path.exists(RootName+"\Templates\Posts"):
        os.makedirs(RootName+"\Templates\Posts")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating SiteHTMLs folder...")
    if not os.path.exists(RootName+"\SiteHTMLs"):
        os.makedirs(RootName+"\SiteHTMLs")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Creating SiteHTMLs\Posts folder...")
    if not os.path.exists(RootName+"\SiteHTMLs\Posts"):
        os.makedirs(RootName+"\SiteHTMLs\Posts")
        print("Folder created.")
    else:
        print("Folder already exists.")
    print("Directory ready!")

def setupConfig():
    file = open("Content/config.txt",'+a')
    file.write("Name: "+input("Full Name: ")+"\n")
    file.write("Email: "+input("Email: ")+"\n")
    file.write("Facebook: "+input("Facebook Link: ")+"\n")
    file.write("LinkedIn: "+input("LinkedIn Link: ")+"\n")
    file.write("Github: "+input("Github Link: ")+"\n")
    file.write("Occupation: "+input("Occupation: ")+"\n")
    file.close()

def moreInfo():
    file = open("Content/config.txt","+a")
    moreFields = input("Are there any more fields you would like to add? (y/n) ")
    while moreFields == "y":
        field = input("Field: ")
        file.write(str(field)+": "+input(field+": ")+"\n")
        moreFields = input("Are there any more fields you would like to add? (y/n) ")
    file.close()

def updateConfig():
    fileName = "Content/config.txt"
    fileNewName = "Content/config1.txt"
    file = open(fileName,"r")
    fileNew = open(fileNewName,"+w")
    print("For each line, press ENTER to keep,'y' to change, or 'd' to delete.")
    for line in file:
        print(line.replace("\n"," (y/n/d) "))
        action = input()
        if action == "d":
            pass
        elif action == "y":
            i = line.find(":")
            fileNew.write(line[:i+2]+input(line[:i+2])+"\n")
        else:
            fileNew.write(line)
    file.close()
    os.remove(fileName)
    fileNew.close()
    os.rename(fileNewName,fileName)
    moreInfo()

def fillDict(info):
    config = open("Content/config.txt")
    for line in config:
        i = line.find(": ")
        key = line[:i]
        value = line[i+2:].strip("\n")
        info[key] = value
    config.close()
    return info

def getPostList():
    ListPost = []
    for post in os.listdir(os.getcwd()+"\\Content\\Posts"):
        if post[-4:] == ".txt":
            file = open(os.getcwd()+"\\Content\\Posts\\"+post,'r')
            for line in file:
                if line[:6] == "Name: ":
                    name = line[6:]
                elif line[:6] == "Date: ":
                    date = line[6:]
                elif line[:13] == "Description: ":
                    description = line[13:]
                    line = file.readline()
                    while line[:6] != "Full: " and line != "":
                        description = description + line
                        line = file.readline()
                    full = line[6:]
                    line = file.readline()
                    while line != "":
                        full = full + line
                        line = file.readline()
                elif line[:6] == "Full: ":
                    full = line[6:]
                    desline = file.readline()
                    while desline != "":
                        full = full + desline
                        desline = file.readline()
            try:
                ListPost.append(Post(name.strip("\n"),date.strip("\n"),description,full))
            except UnboundLocalError:
                print("\nError in file. "+post+" not properly formatted.")
    return ListPost

def createSite(variableDict):
    files = []
    listPost = getPostList()
    for html in os.listdir(os.getcwd()+"\\Templates"):
                if html[-5:] == ".html":
                    files.append(html)
                elif os.path.exists(os.getcwd()+"\\Templates\\"+html):
                    if html == "Posts":
                        for post in listPost:
                            files.append(post.name+".html")
    if len(files) == 0:
        print("\nThere are no templates found!\nPlease make sure that your templates are in the templates folder.\nOperation cancelled. No files created.\n")
        return

    print("\nWARNING: This will replace all HTML files in the SiteHTMLs\nfolder with the same name as those generated here.\n\nFor a list of files that will be affected, type 'f'.\nOtherwise 'y' to continue, or ENTER to cancel.")
    warning = input("(f/y/n) ")
    while warning != 'y' and warning != 'Y':
        if warning == 'f':
            print("\nFiles in SiteHTMLs that will be affected.")
            print(files)
            warning = input("Continue? (y) ")
        else:
            print("Operation cancelled. No files generated.\n")
            return
    print("\nGenerating site...")
    for html in os.listdir(os.getcwd()+"\\Templates"):
        if html[-5:] == ".html":
            print("Writing "+html+"...")
            file = open("Templates/"+html,"r")
            newFile = open("SiteHTMLs/"+html,"w+")
            text = file.read()
            for key in variableDict:
                text = text.replace("{{ "+key+" }}",variableDict.get(key))
                text = text.replace("{{"+key+"}}",variableDict.get(key))
            newFile.write(text)
            file.close()
            newFile.close()
            print(html+" written!")
        elif os.path.exists(os.getcwd()+"\\Templates\\"+html):
            if html == "Posts":

                for post in listPost:
                    print("Writing "+post.name+".html...")
                    file = open("Templates/Posts/posts.html","r")
                    newFile = open("SiteHTMLs/Posts/"+post.name+".html","w+")
                    text = file.read()
                    for attribute in post.attributes:
                        getAttribute = post.get(attribute)
                        text = text.replace("{{ "+attribute+" }}",getAttribute)
                        text = text.replace("{{"+attribute+"}}",getAttribute)
                    for key in variableDict:
                        text = text.replace("{{ "+key+" }}",variableDict.get(key))
                        text = text.replace("{{"+key+"}}",variableDict.get(key))
                    newFile.write(text)
                    file.close()
                    newFile.close()
                    print(post.name+".html written!")
    print("Site files generated successfully!\n")

def createPost():
    name = input("Name: ")
    while len(name) < 1:
        name = input("Name must be at least 1 character or longer.\nName: ")
    date = input("Date (Leave blank for today's date): ")
    if date == "":
        date = datetime.now()
    print("NOTE: It is recommended to type out the 'description' and the 'full'\nfor the post in a text editor, rather than this prompt.\nTo do so, just navigate to Content\Posts and edit the '.txt'.")
    description = input("Description: ")
    full = input("Full: ")
    okay = False
    try:
        while (okay == False):
            post = open("Content/Posts/"+name+".txt")
            if input("Content/Posts/"+name+".txt will be deleted. Continue? (y) ") != "y":
                if input("Rename Post? (y) ") == "y":
                    name = input("Name: ")
                else:
                    return
            else:
                okay = True
            post.close()
        post = open("Content/Posts/"+name+".txt","w+")
    except FileNotFoundError:
        post = open("Content/Posts/"+name+".txt","a+")
    post.write("Name: "+name+"\nDate: "+str(date)+"\nDescription: "+description+"\nFull"+full)
    post.close()


main()
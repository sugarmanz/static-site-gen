"""
static-site-gen.py

This program will take input from a config.txt
and create fill out templates

Author: Jeremiah Zucker
"""

import os

def main():
    checkReadme()
    checkDir()
    info = dict()
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
    info = fillDict(info)
    config.close()
    posts = {}
    task = input("What would you like to do? ('h' for help) ")
    while (task != "q" and task != "Q"):
        if (task == "a" or task == "A"):
            """
            Add a post object.
            """
        elif (task == "g" or task == "G"):
            print("Generate site.")
            createSite(info, posts)
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

def newRootName():
    x = 0
    while (x == 0):
        currRoot = os.getcwd()
        newRoot = input("New folder name (if left blank, will become 'Your Name's Website': ")
        if (newRoot == ""):
            while currRoot[-1] != "\\":
                currRoot = currRoot[:-1]
            file = open("Content/config.txt")
            name = ""
            for line in file:
                if line.find("Name: ") > -1:
                    name = line[6:].strip("\n")
            if name == "":
                name = "Fail"
            newPath = currRoot+name
            if not os.path.exists(newPath):
                os.makedirs(newPath)
                x = x + 1
            else:
                print("Folder already exists. Please choose another name.")
        else:
            while currRoot[-1] != "\\":
                currRoot = currRoot[:-1]
            newPath = currRoot+newRoot
            if not os.path.exists(newPath):
                os.makedirs(newPath)
                x = x + 1
            else:
                print("Folder already exists. Please choose another name.")

def createSite(variableDict,listPost):
    files = []
    for html in os.listdir(os.getcwd()+"\\Templates"):
                if html[-5:] == ".html":
                    files.append(html)
                elif os.path.exists(os.getcwd()+"\\Templates\\"+html):
                    if html == "Posts":
                        for post in listPost:
                            files.append(post.name+".html")
    if len(files) == 0:
        print("\nThere are no templates found!\nPlease make sure that your templates are in the templates folder.\n\nOperation cancelled. No files created.\n")
        return
    
    ("\nWARNING: This will replace all HTML files in the SiteHTMLs\nfolder with the same name as those generated here.\n\nFor a list of files that will be affected,\ntype 'f'. Otherwise 'y' to continue, or ENTER to cancel.")
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
                    file = open("Templates/Posts/"+html,"r")
                    newFile = open("SiteHTMLs/Posts/"+post.name+".html","w+")
                    text = file.read()
                    for attribute in post.attributes:
                        text = text.replace("{{ "+attribute+" }}",post.attribute)
                        text = text.replace("{{"+attribute+"}}",post.attribute)
                    for key in variableDict:
                        text = text.replace("{{ "+key+" }}",variableDict.get(key))
                        text = text.replace("{{"+key+"}}",variableDict.get(key))
                    newFile.write(text)
                    file.close()
                    newFile.close()
                    print(post.name+".html written!")
    print("Site files generated successfully!\n")


main()
import sys
sys.path.append('C:/Users/Garrison/Documents/13th_Grade/geoparsing/SUMMER/env/Lib/site-packages/weasyprint')
import pdfkit
import os
import shutil
import time


opts = {
 'page-size': 'Letter',
 'orientation': 'Landscape',
 'margin-top': '0.75in',
 'margin-right': '0.75in',
 'margin-bottom': '0.75in',
 'margin-left': '0.75in',
 'encoding': "UTF-8",
 'no-outline': None
 }

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#This code tells the program where wkhtmltopdf.exe is on the machine.

url_list = ['https://www.hollywoodreporter.com/features/racist-sexist-classic-how-hollywood-is-dealing-with-its-problematic-content', 'https://www.fakedoesntwork.com/news', 'https://www.greenwichtime.com/news/article/Cuomo-seeks-to-buy-time-amid-scandals-turns-to-15999489.php', 'https://www.wikipedia.org/', 'https://www.google.com/', 'https://en.wikipedia.org/wiki/Central_African_Republic', 'https://www.albanyherald.com/features/health/covid-19-death-rates-10-times-higher-in-countries-where-most-adults-are-overweight-report/article_5ee60b49-22a5-5f0d-935c-3893f786f4ec.html', 'https://www.boxofficemojo.com/date/2021-03-03/weekly/', 'https://www.the-sun.com/uncategorized/2442184/supersonic-jet-spike-london-new-york-inside/', 'https://www.the-sun.com/uncategorized/2442184/supersonic-jet-spike-london-new-york-inside/']
#'https://www.wikipedia.org/', 'https://www.google.com/', 'https://en.wikipedia.org/wiki/Central_African_Republic']
#This is a list of URL's that you want to be turne dinto PDFs.

dest_Folder = r"C:/Users/Garrison/Documents/13th_Grade/geoparsing/SUMMER/PDFS"
    #This is the folder path you want PDFs to be written to.

global newpath

def Make_Folder_Name():
    lcTime = time.strftime("%Y%m%d%H%M", time.localtime())
    global clock
    clock = lcTime[0 : 4] + "_" + lcTime[4 : 6] + "_" + lcTime[6 : 8] + "_" + lcTime[8 : 10] + "." + lcTime[10 : 12]
    global newpath
    newpath =  dest_Folder + "/" + str(clock)
    #This function creates the variable newpath, taking elements from the time, creating a string
    #that should be unique, unless you create many new folders in rapid succession.
    #This new folder is where new PDFs will be written to later on.

def Make_Folder():
    global newpath
    Check_Folder_Name()
def Check_Folder_Name():
    global newpath
    if os.path.exists(newpath):
        newpath = newpath + "_d"
        Make_Folder()
    else:
        os.makedirs(newpath)
    #This function, alongside Check_Folder_Name() creates a loop that evaluates whether or not newpath already exists...
    #If newpath exists, these functions append "_d" (short for duplicate) onto newpath and then reevaluates if newpath
    #exists.  Once newpath no longer exists, these functions create a new folder in dest_folder using newpath.
    #This new (guaranteed unique) folder is where new PDFs will be written to later on.

def PDF_Time():
    Make_Folder_Name()
    Make_Folder()
    n = -1
    errors = 0
    done = 0
    global newpath
    for x in url_list:
        try:
            n += 1
            std = done
            segments = x.split('.')
            name = str(segments[1])
            #1
            
            if os.path.exists(newpath + "/" + name + "_pdf.pdf"):
                name = name + "_" + str(n)
            global opts
            pdfkit.from_url(x, newpath + "/" + name + "_pdf.pdf", options=opts, configuration=config)
            done += 1
            print("Done printing document #" + str(n) + "!")
        except Exception as e:
            errors += 1
            print(e)
            if os.path.exists(newpath + "/" + name + "_pdf.pdf"):
                error_file_name = "000_Errors_with_pdfs.txt"
            else:
                error_file_name = "000_Errors_no_pdfs.txt"
            f=open(newpath + "/" + error_file_name, "a+")
            f.writelines(x)
    if os.path.exists(newpath + "/000_Errors_with_pdfs.txt"):
        if os.path.exists(newpath + "/000_Errors_no_pfds.txt"):
            print("---")
            print("---")
            print("Errors occurred, both with and without creating PDFs.")
            errorless = False
        else:
            print("---")
            print("---")
            print("All errors created PDFs.")
            errorless = False
    else:
        if os.path.exists(newpath + "/000_Errors_no_pfds.txt"):
            print("---")
            print("---")
            print("All errors failed to create PDFs.")
            errorless = False
        else:
            print("---")
            print("---")
            print("NO ERRORS!  WOOHOO!")
            errorless = True
    print("Done printing all documents!")
    if errorless == False:
        print("There were " + str(errors) + " errors.")
    #This function calls on other functions to create a new, unique folder.
    #Then, this function generates PDFs from all urls in the list url_list and writes them to the new folder.
    #It also prints helpful updates along the way. 

PDF_Time()

#to do:
    #make an exception so that webpages that do not work are skipped
        #also create a list of urls that were not able to print
        #print the list to a txt file?
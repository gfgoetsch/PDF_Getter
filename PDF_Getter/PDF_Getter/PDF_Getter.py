
import sys
sys.path.append('C:/Users/Garrison/Documents/13th_Grade/geoparsing/SUMMER/env/Lib/site-packages/weasyprint')
import pdfkit
import os
import shutil
import time
import multiprocessing
import concurrent.futures

#%%%%%%%%%%%%%%%%%%%%%%% HERE AND BELOW IS CONFIGURATION ##########################################
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

url_list = ['https://www.wikipedia.org/', 'https://www.hollywoodreporter.com/features/racist-sexist-classic-how-hollywood-is-dealing-with-its-problematic-content', 'https://www.fakedoesntwork.com/news', 'https://www.greenwichtime.com/news/article/Cuomo-seeks-to-buy-time-amid-scandals-turns-to-15999489.php', 'https://www.wikipedia.org/', 'https://www.google.com/', 'https://en.wikipedia.org/wiki/Central_African_Republic', 'https://www.albanyherald.com/features/health/covid-19-death-rates-10-times-higher-in-countries-where-most-adults-are-overweight-report/article_5ee60b49-22a5-5f0d-935c-3893f786f4ec.html', 'https://www.boxofficemojo.com/date/2021-03-03/weekly/', 'https://www.the-sun.com/uncategorized/2442184/supersonic-jet-spike-london-new-york-inside/', 'https://www.the-sun.com/uncategorized/2442184/supersonic-jet-spike-london-new-york-inside/']
#'https://www.wikipedia.org/', 'https://www.google.com/', 'https://en.wikipedia.org/wiki/Central_African_Republic']
#This is a list of URL's that you want to be turne dinto PDFs.

dest_Folder = r"C:/Users/Garrison/Documents/13th_Grade/geoparsing/SUMMER/PDFS"
    #This is the folder path you want PDFs to be written to.

#GLOBAL VARIABLES
global newpath
newpath = "placeholder"
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% HERE AND ABOVE IS CONFIGURATION %%%%%%%%%%%%%%%%%%%%%%%%%%%

def Find_Time():
    global newpath
    lcTime = time.strftime("%Y%m%d%H%M", time.localtime())
    clock = lcTime[0 : 4] + "_" + lcTime[4 : 6] + "_" + lcTime[6 : 8] + "_" + lcTime[8 : 10] + "." + lcTime[10 : 12]
    newpath = dest_Folder + "/" + str(clock)
    #dig into the line right above this one
    Make_Folder()
def Make_Folder():
    Check_Folder_Name()
def Check_Folder_Name():
    global newpath
    if os.path.exists(newpath):
        newpath = newpath + "_d"
        Make_Folder()
    else:
        os.mkdir(newpath)
    #The above functions create a folder with a unique name based on the time.

def Get_PDF(url):
    global newpath
    name = url
    n_list = name.split(".")
    true_name = "placeholder"
    for n in n_list:
        if "www" in n:
            pass
        elif "http" in n:
            pass
        else:
            true_name = str(n)
            break
    #why does globals()["newpath"] still = placeholder?
    if os.path.exists(newpath + "/" + true_name + "_pdf.pdf"):
        print("This already exists!")
    else:
        try:
            pdfkit.from_url(url, newpath + "/" + true_name + "_pdf.pdf", options=opts, configuration=config)
        except Exception as e:
           print(e)
   
def Cleanup():
    print("Done printing all docs!")



if __name__ == "__main__":
    Find_Time()
    f_list = []
    for url in url_list:
        Get_PDF(url)
#    for url in url_list:
#        p = multiprocessing.Process(target=Get_PDF, args=[url])
#        p.start()
#        f_list.append(p)
#    for f in f_list:
#        f.join()
#    Cleanup()
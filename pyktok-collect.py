import csv
import pyktok as pyk
import sys

def collect_metadata(inputFile, outputFile):
    """Call pyktok with a list of URLs to collect post metadata.
    """

    try:
        urls = []
        with open(inputFile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                urls.append(row[0])
        print(urls)
    except FileNotFoundError:
        print(f"File '{inputFile}' couldn't be found.")
        return 
    
    pyk.specify_browser('chrome')
    pyk.save_tiktok_multi_urls(urls,  # list of URLs to visit
                               False, # don't save videos   
                		       outputFile, # csv file
                		       1) # max time sleep
    
if __name__ == "__main__":
    _, fin, fout = sys.argv
    collect_metadata(fin, fout)

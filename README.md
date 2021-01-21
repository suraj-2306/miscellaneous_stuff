# miscellaneous_stuff
Small scripts or conifgs to make life easier

## 1. Paper_extractor
  - This is based off [scihub.py](https://github.com/zaytoun/scihub.py). I'd suggest you to go through it for thorough understanding of how the pdf are scraped.
  - This works for Ieee and springer papers.
  - I've added another script to help you with autorenaming the downloaded pdfs.
### Usage
  - call them in the following way
  - `python3 /path/to/scihub.py -d "The url of the pdf" -o "output directory"`
  - Then call the name.py to scrape the title from the pdf and rename the file with it.
  - `python3 /path/to/name.py -o "ouput directory"`
### Known Issues
  - Dont have other pdf's in the present folder when you call name.py. This may rename it unnecessarily.
  - Not all websites work.
 

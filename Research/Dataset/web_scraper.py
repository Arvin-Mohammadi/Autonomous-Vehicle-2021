
# =================================================================================================
# -- IMPORT ---------------------------------------------------------------------------------------
# =================================================================================================



import  os
import  pandas as pd
import  time
import  requests
import  colorama 

from    selenium import webdriver
from    selenium.webdriver.common.keys import Keys
from    colorama import Fore, Back, Style

colorama.init()


# Configure proxy settings
proxies = {
    'http': '127.0.0.1:2081',
    'https': '127.0.0.1:2081',
}


# =================================================================================================
# -- LIST OF URLS ---------------------------------------------------------------------------------
# =================================================================================================

# fetching the list of urls from google
def fetch_image_urls(query: str, max_link_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):


    # scroll to the end of the page 
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


    # make the url with the search term
    search_url = "https://www.google.com/search?q={q}&sxsrf=ALiCzsYJMtXFwSIXkBv2VvFlPiGXZHc8JA:1671960629837&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjIya3bupT8AhUVTTABHRbbDXAQ_AUoAXoECAEQAw&biw=1536&bih=794&dpr=1.25"


    # load the page 
    wd.get(search_url.format(q=query))


    image_urls = set()
    image_count = 0
    results_start = 0


    # looping over in page to find images 
    while image_count < max_link_to_fetch:


        scroll_to_end(wd)


        # get all image thumbnail results 
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)


        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")


        # clicking on the images and waiting till it loads 
        for img in thumbnail_results[results_start:number_results]:
            try: 
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue 


        # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.iPVvYb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))


            image_count = len(image_urls)


            if len(image_urls) >= max_link_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else: 
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            load_more_button = wd.find_elements_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")


        # move the result startpoint further down
        results_start = len(thumbnail_results)


    return image_urls



# =================================================================================================
# -- SAVING IMAGES --------------------------------------------------------------------------------
# =================================================================================================


# this function will download the file from the given url and save it to the target folder path
def persist_image(folder_path: str, url: str, counter):


    # this sends a request to the url and extract its content
    try:
        image_content = requests.get(url, proxies=proxies, verify=False).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")


    # write the given image down into the target folder
    try:
        f = open(os.path.join(folder_path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
        f.write(image_content)
        f.close()

        print(f"SUCCESS - saved {url} - as {folder_path}")


    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


# =================================================================================================
# -- DOWNLOADING THE IMAGES -----------------------------------------------------------------------
# =================================================================================================

def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images: int=5): 


    # updates the target folder path to .\image\search-term
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))            


    # makes the directory if there is none
    if not os.path.exists(target_folder):                                                          
        os.makedirs(target_folder)


    # finds the chrome driver 
    with webdriver.Chrome(executable_path=driver_path) as wd:      

        # gathers the urls                                 
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=5)   
 
    # loops over the urls 
    for counter, elem in enumerate(res):       

        # downloads the content of the urls
        persist_image(target_folder, elem, counter) 


# =================================================================================================
# -- LOOP -----------------------------------------------------------------------
# =================================================================================================

def loop():
    
    DRIVER_PATH = 'D:\\chromedriver.exe'
    

    # looping over until input "exit" recieved by user
    while True: 


        print(Fore.GREEN + "\nexit - quit the script", "s search--term - starts searching the web" + Fore.WHITE, sep='\n')


        # input command
        input_string = input("Input command: ") 
        

        # in case of entering "exit", exits the scripts
        if input_string == "exit":             
            break


         # in case of entering "s search-term", initialize the search and download script
        elif input_string[0] == "s":           
            search_term = input_string[2:]

            try:
                N_IMAGES = int(input('Number of Images: '))

            except:
                print(Fore.RED + "Input must be an integer" + Fore.WHITE)
                continue
            
            search_and_download(search_term=search_term, driver_path=DRIVER_PATH, number_images=N_IMAGES)
        

        # in any other case of input, goes back to the start of the loop
        else:                                   
            pass

        

# =================================================================================================
# -- DOWNLOADING THE IMAGES -----------------------------------------------------------------------
# =================================================================================================

loop()
from seleniumbase import BaseCase
import time
from datetime import datetime
from csv import DictReader
import os
from seleniumbase.common.exceptions import NoSuchElementException

class TestTiktok(BaseCase):
    def test_save_html_page(self):
        """
        1. log in manually 
        2. traverse through the vids in the vid_list
        3. where we scroll down once to get comments
        4. save html file fo each vid
        """
        current_time = datetime.now().strftime("%m-%d-%M")
        target_folder = f"{self.data.split('.')[0].split('_')[-1]}-{current_time}"
        os.mkdir(target_folder)

        self.open('https://www.tiktok.com/')
        time.sleep(30) #manually log in
        #self.click('//*[@id="loginContainer"]/div/div/div[3]/div/div[2]/div/div/div')
        
        vid_list = []
        vid_path = f"./pre-processing/url-csv/{self.data}"
        with open(vid_path,"r") as file:
            reader = DictReader(file)          
            for row in reader:
                vid_list.append(row['Video URL'])

        print(f"we have {len(vid_list)} videos")

        for i,vid in enumerate(vid_list):
            time.sleep(5)
            self.open(vid)
            try: 
                self.scroll_to_bottom()
                soup = self.get_beautiful_soup(source=None)

                if soup.find(id="tiktok-verify-ele"):
                    print("element exception!! Check if CAPTCHA appeared!!")
                    time.sleep(15)
                    self.open(vid)
                    self.scroll_to_bottom()
                    soup = self.get_beautiful_soup(source=None)

                with open(f"{target_folder}/vid_{i}.html", "w") as file:
                    file.write(str(soup))
            except:
                #if page x load:
                try:
                    self.open(vid)
                    self.scroll_to_bottom()
                    soup = self.get_beautiful_soup(source=None)
                    with open(f"{target_folder}/vid_{i}.html", "w") as file:
                        file.write(str(soup))
                except NoSuchElementException:
                    print("no element found, moving on to next vid..")
                    pass #just move on to next vid
from seleniumbase import BaseCase
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from datetime import datetime
from csv import DictReader
import os
import pytest
from seleniumbase.common.exceptions import NoSuchElementException
import random
import csv 
import pdb
from collections import deque

#pass in self.var1 param on command line
class TestTiktok(BaseCase):
    @pytest.mark.run(order=1)
    def test_manual_login(self):
        self.open('https://www.tiktok.com/explore')
        time.sleep(40)
    def test_scroll(self):
        scroll = {'Society': 'Food', 'Sports':'Sports', 'Food':'Drama', 'Beauty':'Cars'}
        last_hour = datetime.min
        link_queue = deque()
        with open('./links.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                link_queue.append(row[0])

        print("entering loop")
        while True:
            try:
                current_time = datetime.now()
                current_hour = current_time.hour
                if current_hour != last_hour:
                    last_hour = current_hour
                    distributed_link = link_queue.popleft()
                    print('link:', distributed_link)
                    self.open(distributed_link)
                    try:
                        self.press_right_arrow('html', times=60)
                    except:
                        time.sleep(185)
                    time.sleep(1)
                    headers = ['distributed_link','persona','current_time','rec_1','rec_2','rec_3','rec_4','rec_5','rec_6','rec_7','rec_8']
                    file_path = "./recommended.csv"
                    exists = os.path.exists(file_path)
                    with open(f"./recommended.csv", "a") as f:
                        writer = csv.writer(f)
                        if not exists:
                            writer.writerow(headers)
                        row = [distributed_link,self.var1,current_time]
                        for _ in range(0,8):
                            time.sleep(5)
                            try:
                                self.click('/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[6]/div[2]/div[1]')
                            except:
                                try:
                                    self.click('//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]')
                                except:
                                    print("ERROR from link", distributed_link, "close session and try again")
                                    break
                            time.sleep(1)
                            try:
                                self.press_right_arrow('html', times=20)
                            except:
                                time.sleep(185)
                            time.sleep(1)
                            row.append(self.get_current_url())
                        writer.writerow(row)

                    self.open('https://www.tiktok.com/explore')
                    time.sleep(10)
                    self.scroll_into_view(f'span:contains("{scroll[self.var1]}")')
                    self.click(f'span:contains("{self.var1}")')
                    self.click('//*[@id="main-content-explore_page"]/div/div[2]/div/div[1]') #first vid

                time.sleep(1)
                self.press_down_arrow()
                time.sleep( random.randint(10,20))
            except:
                continue

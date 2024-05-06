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
        self.open('https://www.google.com')
        time.sleep(40)
    def test_scroll(self):
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

                        self.open('https://www.google.com/search?q=do+not+close+browser%21%21+test+running&sca_esv=5fd2585313e87e19&sca_upv=1&hl=en&source=hp&ei=220gZredAcSfptQP6sCzEA&iflsig=ANes7DEAAAAAZiB76_wLBbEd0L6OXIWBiuEpnE5C8adP&ved=0ahUKEwj39oyixcqFAxXEj4kEHWrgDAIQ4dUDCA8&uact=5&oq=do+not+close+browser%21%21+test+running&gs_lp=Egdnd3Mtd2l6IiNkbyBub3QgY2xvc2UgYnJvd3NlciEhIHRlc3QgcnVubmluZzIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSOVEUOUBWLNCcAl4AJABAZgBmgGgAd4bqgEFMzEuMTK4AQPIAQD4AQGYAjOgAuUbqAIKwgIQEAAYAxjlAhjqAhiMAxiPAcICEBAuGAMY5QIY6gIYjAMYjwHCAgsQLhiABBixAxiDAcICERAuGIAEGLEDGNEDGIMBGMcBwgILEAAYgAQYsQMYgwHCAgUQLhiABMICDhAuGIAEGLEDGNEDGMcBwgIOEC4YgAQYsQMYgwEYigXCAggQLhiABBixA8ICCxAuGIAEGNEDGMcBwgIFEAAYgATCAggQABiABBixA8ICDhAAGIAEGLEDGIMBGIoFwgIUEC4YgAQYsQMY0QMYgwEYxwEYigXCAgQQABgDwgIUEC4YgAQYsQMYgwEYxwEYjgUYrwHCAgoQABiABBhGGP8BwgIGEAAYFhgewgIIEAAYFhgeGA_CAgcQABiABBgNwgIGEAAYDRgewgIIEAAYBRgNGB7CAgUQIRifBcICCxAAGIAEGIYDGIoFwgIIEAAYgAQYogTCAggQABiiBBiJBZgDBZIHBTM5LjEyoAe0uAI&sclient=gws-wiz')

            except:
                continue

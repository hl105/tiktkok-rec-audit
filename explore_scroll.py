from seleniumbase import BaseCase
import time
from datetime import datetime
from csv import DictReader
import os
import pytest
from seleniumbase.common.exceptions import NoSuchElementException
import random

#pass in self.var1 param on command line
class TestTiktok(BaseCase):
    @pytest.mark.run(order=1)
    def test_manual_login(self):
        self.open('https://www.tiktok.com/explore')
        time.sleep(30)
    def test_save_html_page(self):
        self.click(f'//*[@id="main-content-explore_page"]/div/div[1]/div[1]/button[{self.var1}]')
        self.click('//*[@id="main-content-explore_page"]/div/div[2]/div/div[1]') #first vid
        for i in range(0,20):
            self.press_down_arrow()
            time.sleep(random.randint(10,20))
            self.send_keys('/html/body','l')
            time.sleep(3)
            if random.randint(1,10) == 1: #about once every 20 times
                self.sendkeys('//body','l')

        #instead of cron maybe just get current time?
        #
                
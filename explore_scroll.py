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
        time.sleep(40)
    def test_scroll(self):
        last_hour = datetime.min
        while True:
            scroll = {'Society': 'Food', 'Singing': 'Singing', 'Sports':'Sports', 'Food':'Drama', 'Beauty':'Cars'}
            self.open('https://www.tiktok.com/explore')
            time.sleep(10)
            self.scroll_into_view(f'span:contains("{scroll[self.var1]}")')
            self.click(f'span:contains("{self.var1}")')
            self.click('//*[@id="main-content-explore_page"]/div/div[2]/div/div[1]') #first vid
            try:
                self.press_down_arrow()
                time.sleep( random.randint(10,20))
                self.send_keys('/html/body','l')
                time.sleep(3)
                if random.randint(1,5) == 1: #about once every 20 times
                    self.sendkeys('//body','l')

                current_time = datetime.now()
                current_hour = current_time.hour
                if current_hour != last_hour:
                    self.open('https://www.tiktok.com/@funnycats0ftiktok/video/7326218472130694442?is_from_webapp=1&sender_device=pc&web_id=7340475663080785450')
                    soup = self.get_beautiful_soup(source=None)
                    with open(f"persona_{self.var1}/{current_hour}.html", "w") as file:
                        file.write(str(soup))
                    last_hour = current_hour
                    time.sleep(100)
            except:
                pass
        
                
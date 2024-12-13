from selenium import webdriver
import time
class Copy:
    def setUp(self):
        self.driver=webdriver.Chrome()
    def fetch_page(self):
        try:
            
            self.driver.get("https://www.btreesystems.com/selenium-with-python-training-in-chennai/")
            time.sleep(2)
            page_source=self.driver.page_source.encode('utf-8')
            with open('result.html','wb')as f:
                f.write(page_source)
        except exception as e:
            print(f"an error occured:{str(e)}")
    def teardown(self):
        self.driver.quit()
if __name__=="__main__":
    fet=Copy()
    fet.setUp()
    fet.fetch_page()
    fet.teardown()

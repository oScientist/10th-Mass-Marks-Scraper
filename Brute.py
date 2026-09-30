import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
#options.add_argument("--headless=new")  # modern headless mode
#options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://bisedgkhan.edu.pk/RESULLLT_MA0002025/index.php")

def rollnoentry(rollno): #Sends the roll  number

 Box = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/input[2]")
 Box.send_keys(f"{rollno}")
def clickthebutton(): #Clicks to send the roll
 
 Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/form/button")
 Button.click()
def numberfinder(): #Returns Numbers
 Numbers1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/table[1]/tbody/tr[10]/td[4]")
 return Numbers1.text
def Namefinder(): #Returns Name
  Name =  driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/p[2]")
  return Name.text
def FatherNameFinder(): #Returns Father name
 Fathername = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/p[3]")
 return Fathername.text

def Program(rollnofunction): #Core of program
 rollnoentry(rollnofunction)
 clickthebutton()
 time.sleep(0.3)
 number2 = numberfinder()
 name = Namefinder()
 fatname = FatherNameFinder()
 return number2, name, fatname
def driverexitter():
 driver.quit()

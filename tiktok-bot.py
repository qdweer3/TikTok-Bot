import os
from selenium import webdriver
from time import sleep
from colorama import init, Fore, Style

init(autoreset=True)


def loop1(): #views
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        print("")
        print(">>> Views Sent <<<")
        print("")
        sleep(330)
        loop1()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop1()


def loop2(): #followers
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        print("")
        print(">>> Followers Sent <<<")
        print("")
        sleep(2520)
        loop2()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop2()


def loop3(): #shares
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop3()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div/div/form/button").click()
        sleep(10)
        driver.refresh()
        print("")
        print(">>> Shares Sent <<<")
        print("")
        sleep(110)
        loop3()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop3()


def loop4(): #likes
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        print("")
        print(">>> Hearts Sent <<<")
        print("")
        sleep(3015)
        loop4()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop4()


def loop5(): #comment likes
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop5()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form/ul/li/div/button").click()
        driver.refresh()
        print("")
        print(">>> Comment Likes Sent <<<")
        print("")
        sleep(60)        
        loop5()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop5()



print(Style.BRIGHT + '\n------------- TIKTOK BOT -------------\n')
print(Fore.RED + "This tool is for educational purposes only")
print(Fore.RED + "Do not use it for illegal work or without the consent of the tiktok account owner")
print(Fore.RED + "I am not responsible for any action taken using this script")
print(Fore.RED + "I am not responsible for any damage of any kind for using this script")
print(Style.BRIGHT + '\n--------------------------------------\n')
vidUrl = input(">>> Your Video URL : ")
bot = int(input(">>> What do you want to do? \n> 1 - Get Views \n> 2 - Get Followers \n> 3 - Get Shares \n> 4 - Get Likes \n> 5 - Get Comments Likes \n> Please insert a number from the list : "))
print("\n--------------------------------------")

if (bot > 5 or bot < 1):
     print("You can insert just 1, 2, 3, 4 or 5\nExiting...")
     sleep(5)
else:
    PATH = os.getcwd() + "/chromedriver" # EDITED TO LINUX
    driver = webdriver.Chrome(PATH)
    driver.get("https://zefoy.com/")

    if bot == 1:
        loop1()
    elif bot == 2:
        loop2()
    elif bot == 3:
        loop3()
    elif bot == 4:
        loop4()
    else: #bot == 5
        loop5()

from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

playlist_list = []

credentials = [
    {'email': 'your old account email', 'password': 'x'},
    {'email': 'your new email', 'password': 'x'},
]

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://open.spotify.com/')

def log_in(credential):
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
    time.sleep(1)
    driver.find_element_by_id('login-username').send_keys(credential['email'])
    driver.find_element_by_id('login-password').send_keys(credential['password'])
    driver.find_element_by_id('login-button').click()
    time.sleep(3)

for _ in range(2):
    if _ == 0:
        log_in(credentials[_])
        # Entrar a la biblioteca
        driver.get('https://open.spotify.com/collection/playlists')
        time.sleep(3)
        #Obtener los links
        playlist_elements = driver.find_elements_by_class_name('f7ebc3d96230ee12a84a9b0b4b81bb8f-scss')
        
        for playlist in playlist_elements:
            playlist_list.append(playlist.get_attribute('href'))
            
        driver.quit()
    else:
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get('https://open.spotify.com/')
        log_in(credentials[_])
        for playlist in playlist_list[1:]:
            driver.get(playlist)
            time.sleep(2)
            song_list = driver.find_elements_by_xpath('//*[@class="_07bed3a434fa59aa1852a431bf2e19cb-scss d12d20a78fbc13787860287d10063d04-scss"]')
            for song in song_list:
                song.click()
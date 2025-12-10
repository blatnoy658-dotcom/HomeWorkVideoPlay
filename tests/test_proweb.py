import time
from pages.home_page import HomePage
from pages.login_page import LoginPage

DURATION = 2

# noinspection PyBroadException
def test_login_chrome(driver_chrome):
    driver = driver_chrome
    driver.get("https://my.proweb.uz/log-in")

    login_page = LoginPage(driver)
    login_page.enter_phone_input("998977253512")
    time.sleep(1.2)

    login_page.click_btn_next()
    login_page.enter_password("ledmonitor12345")
    time.sleep(1.2)

    login_page.click_btn_submit()

    # Закрытие активных сеансов
    try:
        login_page.click_btn_sessions()
        time.sleep(1)
        login_page.click_btn_finish()
        time.sleep(1)
    except:
        pass

    home_page = HomePage(driver)
    home_page.click_video_inst()
    time.sleep(DURATION)
    home_page.click_work_inst()
    time.sleep(DURATION)
    home_page.click_watch_video()
    time.sleep(DURATION)
    home_page.click_video_play()
    time.sleep(DURATION)
    # home_page.click_video_rating_5()
    # time.sleep(3)
    home_page.click_fullscreen_btn()
    time.sleep(10)
    home_page.click_video_stop()
    home_page.click_fullscreen_exit()
    time.sleep(1)
    home_page.click_profile_icon()
    time.sleep(1)
    home_page.click_exit_btn()
    time.sleep(1)
    home_page.click_confirm_exit()


# noinspection PyBroadException
def test_login_edge(driver_edge):
    driver = driver_edge
    driver.get("https://my.proweb.uz/log-in")

    login_page = LoginPage(driver)
    login_page.enter_phone_input("998977253512")
    time.sleep(1.2)

    login_page.click_btn_next()
    login_page.enter_password("ledmonitor12345")
    time.sleep(1.2)

    login_page.click_btn_submit()

    try:
        login_page.click_btn_sessions()
        time.sleep(1)
        login_page.click_btn_finish()
        time.sleep(1)
    except:
        pass

# Переход домой после логина
    home_page = HomePage(driver)
    home_page.click_video_inst()
    time.sleep(DURATION)
    home_page.click_work_inst()
    time.sleep(DURATION)
    home_page.click_watch_video()
    time.sleep(DURATION)
    home_page.click_video_play()
    time.sleep(DURATION)
    # home_page.click_video_rating_5()
    # time.sleep(3)
    home_page.click_fullscreen_btn()
    time.sleep(10)
    home_page.click_video_stop()
    home_page.click_fullscreen_exit()
    time.sleep(1)
    home_page.click_profile_icon()
    time.sleep(1)
    home_page.click_exit_btn()
    time.sleep(1)
    home_page.click_confirm_exit()


# noinspection PyBroadException
# def test_login_firefox(driver_fire_fox):
#     driver = driver_fire_fox
#     driver.get("https://my.proweb.uz/log-in")
# 
#     login_page = LoginPage(driver)
#     login_page.enter_phone_input("998977253512")
#     time.sleep(1.2)
# 
#     login_page.click_btn_next()
#     login_page.enter_password("ledmonitor12345")
#     time.sleep(1.2)
# 
#     login_page.click_btn_submit()
# 
#     try:
#         login_page.click_btn_sessions()
#         time.sleep(1)
#         login_page.click_btn_finish()
#     except:
#         pass
#
    # home_page = HomePage(driver)
    # home_page.click_video_inst()
    # time.sleep(DURATION)
    # home_page.click_work_inst()
    # time.sleep(DURATION)
    # home_page.click_watch_video()
    # time.sleep(DURATION)
    # home_page.click_video_play()
    # time.sleep(DURATION)
    # # home_page.click_video_rating_5()
    # # time.sleep(3)
    # home_page.click_fullscreen_btn()
    # time.sleep(10)
    # home_page.click_video_stop()
    # home_page.click_fullscreen_exit()
    # time.sleep(1)
    # home_page.click_profile_icon()
    # time.sleep(1)
    # home_page.click_exit_btn()
    # time.sleep(1)
    # home_page.click_confirm_exit()
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# noinspection PyBroadException,PyArgumentList
class HomePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

        self.video_inst = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__top > div > div.list-tile.home-card__top-content-list > div > div.course-avatar.home-card__top-content-list-icon")

        self.work_inst = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")

        self.watch_video = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card > div > div.lesson-card-left > div.lesson-card-left_actions")

        self.video_play = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")

        # self.video_rating_5 = (By.CSS_SELECTOR, ".videolesson__general-footer-rating span:nth-child(5)")

        self.fullscreen_btn = (By.CSS_SELECTOR, "button.baseavatar_fullscreen")
        self.fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button.baseicon.baseavatar_fullscreen-exit")

        self.profile_icon = (By.CSS_SELECTOR, ".header__avatar")
        self.exit_btn = (By.CSS_SELECTOR, ".inforation div:nth-child(4)")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog .material-dialog__window-actions button:nth-child(2)")



    def safe_click(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        element = wait.until(EC.presence_of_element_located(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)

        wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)



    def click_video_inst(self):
        self.safe_click(self.video_inst)

    def click_work_inst(self):
        self.safe_click(self.work_inst)

    def click_watch_video(self):
        self.safe_click(self.watch_video)

    def click_video_play(self):
        self.safe_click(self.video_play)

    # def click_video_rating_5 (self):
    #     self.safe_click(self.video_rating_5)


    # noinspection PyArgumentList
    def click_video_stop(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            video = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
            )
            ActionChains(self.driver).move_to_element(video).perform()
        except:
            pass


        self.safe_click(self.video_play)

    def click_fullscreen_btn(self ):
        self.safe_click(self.fullscreen_btn)

    def click_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)


        try:
            video = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
            )
            ActionChains(self.driver).move_to_element(video).perform()
        except:
            pass


        try:
            exit_btn = wait.until(
                EC.element_to_be_clickable(self.fullscreen_exit)
            )


            self.driver.execute_script("arguments[0].click();", exit_btn)
            return

        except:
            pass


        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # -------- LOGOUT --------

    def click_profile_icon(self):
        # На всякий случай закрываем fullscreen повторно
        try:
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            pass

        self.safe_click(self.profile_icon)

    def click_exit_btn(self):
        self.safe_click(self.exit_btn)

    def click_confirm_exit(self):
        self.safe_click(self.confirm_exit)

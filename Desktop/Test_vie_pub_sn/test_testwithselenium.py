import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestTestwithselenium:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()  # Vous pouvez utiliser Chrome ou un autre navigateur si nécessaire
        self.driver.implicitly_wait(10)  # Attente implicite

    def teardown_method(self, method):
        self.driver.quit()

    def close_overlay(self):
        try:
            overlay = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".overlay-class"))  # Mettez à jour le sélecteur CSS
            )
            self.driver.execute_script("arguments[0].click();", overlay)
            print("Overlay fermé.")
        except Exception as e:
            print(f"Échec de la fermeture de l'overlay: {e}")

    def scroll_to_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((by, value))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            print(f"Défilé jusqu'à l'élément {value}.")
        except Exception as e:
            print(f"Échec du défilement jusqu'à l'élément {value}: {e}")
            raise

    def click_element(self, by, value):
        try:
            self.scroll_to_element(by, value)
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((by, value))
            )
            self.driver.execute_script("arguments[0].click();", element)
            print(f"Élément {value} cliqué.")
        except Exception as e:
            print(f"Échec du clic sur l'élément {value}: {e}")
            raise

    def move_to_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((by, value))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print(f"Déplacement vers l'élément {value}.")
        except Exception as e:
            print(f"Échec du déplacement vers l'élément {value}: {e}")
            raise

    def test_testwithselenium(self):
        self.driver.get("https://www.vie-publique.sn/")
        self.driver.set_window_size(761, 710)

        self.close_overlay()  # Fermer l'overlay si nécessaire

        # Exemple de sélecteurs CSS mis à jour pour les tests
        self.click_element(By.CSS_SELECTOR, ".i-heroicons\\3A bars-3")
        self.click_element(By.CSS_SELECTOR, ".relative:nth-child(2) > ul > li:nth-child(2) .truncate")
        self.click_element(By.CSS_SELECTOR, ".rounded-lg:nth-child(1) .mb-4")

        self.move_to_element(By.CSS_SELECTOR, "a > .flex")
        self.click_element(By.CSS_SELECTOR, ".i-heroicons\\3A bars-3")
        self.click_element(By.CSS_SELECTOR, ".relative:nth-child(2) > ul > li:nth-child(3) .truncate")
        self.click_element(By.CSS_SELECTOR, ".rounded-lg:nth-child(1) .text-sm")

        # Continuer avec les autres actions de clic et de défilement...

        # Assurez-vous de vérifier que chaque élément est présent et visible avant de tenter de cliquer

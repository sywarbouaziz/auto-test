from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialiser le navigateur
driver = webdriver.Chrome()

# Naviguer vers Google
driver.get("https://www.google.com")

# Recherche avec le mot-clé "Test Auto"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Test Auto")
search_box.send_keys(Keys.RETURN)

# Attendre un moment pour les résultats de la recherche
time.sleep(2)

# Cliquer sur l'onglet "Images"
images_tab = driver.find_element(By.XPATH, "//a[text()='Images']")
images_tab.click()

# Attendre un moment pour le chargement des images
time.sleep(2)

# Vérifier le bon affichage des données sur la page (Vous pouvez ajouter des vérifications spécifiques ici)
# Exemple : assert "Google Images" in driver.title

# Prendre une capture d'écran
driver.save_screenshot("screenshot.png")

# Fermer le navigateur
driver.quit()

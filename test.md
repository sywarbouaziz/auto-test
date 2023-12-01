# Documentation d'exécution des tests avec Selenium et Python

## Prérequis

1. **Python et pip :** Assurez-vous d'avoir Python installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger depuis [le site officiel de Python](https://www.python.org/downloads/). Pip, le gestionnaire de paquets Python, doit également être installé.

2. **Selenium :** Installez le module Selenium en exécutant la commande suivante dans votre terminal ou votre invite de commande :

    ```bash
    pip install selenium
    ```

3. **Navigateur web et driver :** Assurez-vous d'avoir le navigateur Chrome installé sur votre machine. Téléchargez le driver Chrome depuis [la page officielle](https://sites.google.com/chromium.org/driver/) et assurez-vous que le chemin du driver est ajouté à votre variable d'environnement `PATH`.

## Exécution des tests

1. **Téléchargement du script :** Téléchargez le script de test (dans notre exemple, `test.py`) sur votre machine.

2. **Exécution du script :** Utilisez la commande suivante pour exécuter le script depuis votre terminal ou votre invite de commande :

    ```bash
    python test.py
    ```
    Vous devriez voir le message suivant dans votre terminal si l'exécution a fonctionné correctement :

    ```
    Navigating to Google...
    Performing search...
    Clicked on the 'Images' tab.
    Found X images on the page.  # X sera remplacé par le nombre réel d'images trouvées
    Screenshot saved successfully.
    Browser closed successfully.
    ```

## Interprétation

Pour interpréter les résultats des tests, vous pouvez utiliser les critères suivants :

1. **Onglet "Images"*:**  L'onglet "Images" doit être présent sur la page..

2. **Nombre de résultats :** Le nombre de résultats d'images affiché sur la page doit être supérieur à 0.

3. **Capture d'écran :** La capture d'écran générée ("screenshot.png") doit être valide et doit refléter le bon déroulement des actions automatisées.

Si l'un de ces critères n'est pas rempli, le test est considéré comme un échec. Assurez-vous de vérifier ces aspects lors de l'analyse des résultats.

## Conseils supplémentaires

- **Vérification manuelle :** Après l'exécution des tests, examinez visuellement la capture d'écran générée ("screenshot.png") pour confirmer le bon déroulement des actions automatisées.

- **Personnalisation des tests :** Modifiez le script en fonction de vos besoins spécifiques. Vous pouvez ajouter d'autres vérifications, assertions, ou actions pour couvrir davantage de scénarios.

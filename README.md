# Solar Campus Intelligence Platform (SCIP) — version aplatie

Cette version du projet est **spécialement organisée pour un déploiement
via l'interface web de GitHub sur mobile** (upload fichier par fichier),
qui ne préserve pas les sous-dossiers lors d'un "Add files via upload"
multiple. Tous les modules Python sont donc à plat à la racine, avec un
préfixe qui remplace le dossier d'origine :

| Préfixe            | Correspond à (version "propre" avec dossiers) |
|--------------------|-----------------------------------------------|
| `config_*.py`      | `config/*.py`                                 |
| `database_*.py`    | `database/*.py`                               |
| `models_*.py`      | `models/*.py`                                 |
| `services_*.py`    | `services/*.py`                               |
| `services_ai_*.py` | `services/ai/*.py`                            |
| `integration_*.py` | `integration/*.py`                            |
| `api_*.py`         | `api/*.py` et `api/routers/*.py`              |
| `exports_*.py`     | `exports/*.py`                                |
| `components_*.py`  | `components/*.py`                             |

Seul le dossier **`pages/`** reste un vrai dossier : Streamlit exige que
les pages de l'application multipage soient dans un dossier appelé
exactement `pages`, au même niveau que `Home.py`.

## Procédure de mise en ligne depuis un téléphone (GitHub web)

### 1. Créer le dossier `pages/` (obligatoire, à faire en premier)

Le glisser-déposer de fichiers depuis un téléphone ne crée pas de
sous-dossiers de façon fiable. La méthode qui marche à coup sûr :

1. Sur la page du dépôt GitHub, ouvrir **Add file → Create new file**.
2. Dans le champ du nom de fichier, taper directement :
   `pages/01_Tableau_de_bord.py` (le `/` crée automatiquement le dossier).
3. Coller le contenu du fichier correspondant.
4. Commit.
5. Répéter pour les 13 autres pages (`pages/02_Digital_Twin.py`, etc.).

### 2. Ajouter tous les fichiers restants à la racine

Une fois `pages/` créé, tous les autres fichiers (`Home.py`,
`requirements.txt`, `config_settings.py`, `models_building.py`, etc.)
peuvent être ajoutés normalement via **Add file → Upload files**,
puisqu'ils n'ont pas besoin de sous-dossier : ils vont tous à la racine
du dépôt, au même niveau que `pages/`.

### 3. Paramètres Streamlit Cloud

- **Main file path** : `Home.py`
- **Python version** : lu automatiquement depuis `.python-version` (3.12)

## Démarrage local (si vous avez accès à un ordinateur avec Git)

```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run Home.py
```

## Note pour la suite du développement

Cette structure aplatie est optimisée pour la mise en ligne rapide, pas
pour la lisibilité à long terme. Dès que vous avez accès à un ordinateur
(ou à `git` via une application comme Termux), il est recommandé de
repasser à la version avec sous-dossiers (`models/`, `services/`, etc.)
en clonant le dépôt et en réorganisant les fichiers avec de vraies
commandes `git mv`, ce qui préserve correctement l'arborescence.

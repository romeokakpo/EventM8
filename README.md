## 📘 README.md – Plateforme de Gestion d'Événements (FastAPI)

````markdown
# 🎉 Plateforme de Gestion d'Événements – FastAPI

Une API complète de gestion d’événements construite avec **FastAPI**, offrant des fonctionnalités avancées comme :

✅ Authentification sécurisée (JWT)  
✅ Création et inscription à des événements  
✅ Commentaires et interactions sociales  
✅ Notifications temps réel (WebSocket)  
✅ Recommandation intelligente d’événements  
✅ Documentation Swagger et support Docker

---

## 🚀 Fonctionnalités

- 🔐 Inscription et connexion (JWT, bcrypt)
- 👥 Multi-rôles : organisateurs, participants
- 📅 Création, modification, suppression d’événements
- ✍️ Commentaires et likes sur les événements
- 📬 Notifications temps réel avec WebSocket
- 📈 Recommandation d'événements personnalisée
- 📄 Exportation iCal / intégration Google Calendar (optionnel)
- 🧪 Tests automatisés avec Pytest
- 🐳 Docker-ready

---

## 🧱 Technologies

- **Backend** : FastAPI, SQLAlchemy, Pydantic
- **Auth** : OAuth2 + JWT (`python-jose`, `passlib`)
- **Database** : PostgreSQL (ou SQLite pour test)
- **Realtime** : WebSocket natif
- **Recommandation** : scikit-learn
- **CI/CD** : GitHub Actions
- **Containerisation** : Docker & Docker Compose

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/romeokakpo/EventM8.git
cd EventM8
```
````

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d’environnement

Créer un fichier `.env` :

```
SECRET_KEY=changeme
DATABASE_URL=sqlite:///./app.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Lancer le projet

```bash
uvicorn app.main:app --reload
```

<!-- ---

## 🧪 Tests

```bash
pytest
``` -->

---

## 📚 Documentation interactive

- Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc : [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🐳 Docker (optionnel)

```bash
docker build -t gestion-evenements .
docker run -d -p 8000:8000 gestion-evenements
```

Ou avec `docker-compose` :

```bash
docker-compose up --build
```

---

## ✨ Crédits

Ce projet a été développé pour démontrer une maîtrise avancée de **FastAPI**, SQLModel, sécurité JWT, WebSocket et bonnes pratiques API REST.

---

## 📩 Contact

> ✉️ romeokakpo3@gmail.com  
> 💼 [Ton LinkedIn](https://www.linkedin.com/in/ton-profil)  
> 🔗 Licence : MIT

```

```

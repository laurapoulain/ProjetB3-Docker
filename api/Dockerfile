# build des dependances python
FROM python:3.11-slim AS builder

WORKDIR /app

# copie des dépendances et intallation des dépendances python (en mode user)
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# image finale
FROM python:3.11-slim
WORKDIR /app

# creation / utilisation d'un utilisateur non-root
RUN useradd -m appuser
USER appuser

# copie des dependances python précedemment installées 
COPY --from=builder /root/.local /home/appuser/.local
COPY . .

# ajout des libs python dans le path
ENV PATH="/home/appuser/.local/bin:${PATH}"

# execution de notre application
CMD ["python", "app.py"]

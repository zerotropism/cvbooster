# 🚀 CV Booster

Application Streamlit permettant d'optimiser des CV en fonction d'une description de poste, en utilisant un LLM local via Ollama.

## Fonctionnalités

- 📋 Saisie d'une description de poste (texte ou fichier Word)
- 📊 Classement automatique des CV par pertinence
- ✨ Réécriture du CV sélectionné pour mieux correspondre au poste
- 📥 Export du CV optimisé en Word, PDF ou TXT

## Prérequis

- [uv](https://docs.astral.sh/uv/) (gestionnaire de paquets)
- [Ollama](https://ollama.com/) installé et en cours d'exécution
- Modèle Ollama téléchargé (défini dans `config.yaml`)

## Installation

```bash
git clone https://github.com/<your-username>/cvbooster.git
cd cvbooster
uv sync
```

## Configuration

Editer le fichier `config.yaml` à la racine du projet :

```yaml
model: llama3.2

prompts:
  rank:
    default: |
      ...
  rewrite:
    default: |
      ...
```

## Lancement

```bash
uv run streamlit run src/main.py
```

## Structure du projet

```
cvbooster/
├── config.yaml
├── README.md
├── src/
│   ├── main.py          # Interface Streamlit
│   ├── llm_client.py    # Appels au LLM via Ollama
│   ├── config.py        # Chargement de la configuration
│   ├── cv_loader.py     # Chargement des CV
│   └── exporters.py     # Export Word/PDF/TXT
```
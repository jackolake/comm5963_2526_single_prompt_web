# CUHK MSc in New Media - Flask Revamp

This project is a modernized Flask + Tailwind CSS website inspired by the original programme pages at `https://pg.com.cuhk.edu.hk/pgp_nm/`.

## What was revamped

- Modern responsive layout with clear content hierarchy
- Route structure aligned with original sections:
  - Home
  - Programme
  - Curriculum
  - Admissions
  - Faculty
  - Research
  - Students and Alumni
  - Contact
- CUHK-inspired color palette centered on purple and yellow/gold accents

## Color palette source

Colors were sampled from CUHK CSS assets under `https://www.cuhk.edu.hk/english/css/`.

Primary values used:

- Purple: `#7D2882`
- Deep Purple: `#73216D`
- Purple Accent: `#964C90`
- Yellow: `#F0AA23`
- Gold: `#E6AE00`

## Tech stack

- Python 3
- Flask
- Tailwind CSS (CDN runtime config)

## Quick start

```bash
python -m pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:5000`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Run with Docker

```bash
docker build -t cuhk-new-media .
docker run --rm -p 5000:5000 cuhk-new-media
```

Open `http://127.0.0.1:5000`.

## Project structure

- `app/__init__.py`: App factory
- `app/routes.py`: Route handlers and page content
- `app/templates/`: Jinja templates
- `app/static/css/site.css`: Custom theme enhancements
- `run.py`: Local dev runner
- `tests/test_app.py`: Basic route and content tests


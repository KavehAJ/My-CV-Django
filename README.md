# My CV Django

A one-page personal resume/portfolio website built with Django, showcasing my skills, experience, and projects.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in a real secret key:

   ```bash
   cp .env.example .env
   ```

   You can generate a secret key with:

   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   ```

3. Run the development server:

   ```bash
   cd MyCV
   python manage.py runserver
   ```

## Deployment notes

- Set `DJANGO_DEBUG=False` and fill in `DJANGO_ALLOWED_HOSTS` with your real
  domain(s) before deploying.
- Never commit the `.env` file — it's already excluded via `.gitignore`.

## License

See `LICENSE`.

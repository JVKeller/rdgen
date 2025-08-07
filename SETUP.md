# RustDesk Generator Setup Guide

This guide covers the complete setup process for the RustDesk custom client generator Django application.

## Prerequisites

- Python 3.11+
- Git
- GitHub account with a repository fork of rustgen

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rustgen.git
   cd rustgen
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install python-dotenv django-cors-headers
   ```

## Configuration

1. **Create environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your values:**
   - `SECRET_KEY`: Generate using Django's utility
   - `GHUSER`: Your GitHub username
   - `GHBEARER`: GitHub Personal Access Token (see below)
   - `GENURL`: URL where your Django app runs (e.g., http://192.168.1.100:9000)
   - `REPONAME`: Your repository name (usually 'rustgen')

3. **GitHub Personal Access Token:**
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Create token with these scopes:
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows)
   - Copy token to `GHBEARER` in `.env`

4. **Enable GitHub Actions workflows:**
   ```bash
   # Replace YOUR_TOKEN with your GitHub token
   curl -L -X PUT \
     -H "Accept: application/vnd.github+json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "X-GitHub-Api-Version: 2022-11-28" \
     https://api.github.com/repos/YOUR_USERNAME/rustgen/actions/workflows/generator-windows.yml/enable
   
   # Repeat for other platforms: generator-linux.yml, generator-android.yml, generator-macos.yml
   ```

## Running the Application

1. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Start the development server:**
   ```bash
   python manage.py runserver 0.0.0.0:9000
   ```

3. **Access the application:**
   - Open browser to `http://your-server-ip:9000`
   - Fill out the generator form
   - Submit to trigger GitHub Actions workflow

## Troubleshooting

### CORS/CSRF Errors
- Ensure your domain/IP is in `CSRF_TRUSTED_ORIGINS` in settings.py
- Check that `{% csrf_token %}` is present in forms
- Verify CORS middleware is properly configured

### GitHub API Errors
- **404 Not Found**: Workflows may be disabled, use curl commands above to enable
- **403 Forbidden**: Token needs `repo` scope for admin access
- **401 Unauthorized**: Check token validity and permissions

### Environment Variables Not Loading
- Verify `.env` file exists and has correct format
- Check that `python-dotenv` is installed
- Ensure `load_dotenv()` is called in settings.py

## Security Notes

- Never commit `.env` file to git
- Use strong, unique SECRET_KEY for production
- Rotate GitHub tokens regularly
- Use HTTPS in production environments

## Features Implemented

- ✅ CORS/CSRF protection configured
- ✅ Environment variable management
- ✅ GitHub Actions integration
- ✅ Custom security middleware for development
- ✅ Favicon handling
- ✅ Comprehensive error handling
- ✅ Debug logging for troubleshooting

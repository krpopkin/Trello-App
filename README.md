# Trello-App

A simple Flask application to generate status reports from your Trello boards.

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Demo](#demo)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Configuration](#configuration)  
  - [Running Locally](#running-locally)  
  - [Deployment](#deployment)  
- [Project Structure](#project-structure)  
- [Notebook](#notebook)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)

## About

Trello-App is a lightweight web interface built with Flask to:

1. **Fetch** all your Trello boards (projects).  
2. **Render** a dropdown menu allowing you to select a specific board or “All boards.”  
3. **Generate** status reports for the selected board(s).

This repo includes the core Flask app, Jinja2 templates, custom CSS, and a sample Jupyter notebook.

## Features

- **Board selection** via dynamic dropdown.  
- **Status report generation** for one or multiple boards.  
- **Minimal dependencies**: Flask, Gunicorn.  
- **Heroku-ready** with a `Procfile`.  

### Prerequisites

- Python 3.7+  
- `pip` package manager  

### Installation

1. **Clone** the repo  
   ```bash
   git clone https://github.com/krpopkin/Trello-App.git
   cd Trello-App
   ```

2. **(Optional) Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

To integrate with the Trello API, export your credentials as environment variables:

```bash
export TRELLO_API_KEY=<your_trello_api_key>
export TRELLO_TOKEN=<your_trello_token>
```

> **Note:** Update `flask_app.py` to use these environment variables for Trello API calls.

### Running Locally

```bash
python flask_app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Deployment

The included **Procfile** lets you deploy to Heroku easily:

```
web: gunicorn app:app
```

Make sure your Flask entry-point is named `app.py` (or update the Procfile accordingly).

## Project Structure

```
Trello-App/
├── .gitattributes
├── assets/
│   └── screenshot.png                  # Demo screenshot (if added)
├── Display_recs_With_Variant_Filter.ipynb  # Sample Jupyter notebook
├── Procfile
├── flask_app.py                        # Main Flask application
├── requirements.txt
├── static/
│   └── css/
│       └── style.css                   # Custom styling
└── templates/
    └── index.html                      # Jinja2 template for the form
```

## Notebook

- **Display_recs_With_Variant_Filter.ipynb**  
  Demonstrates how to display recommendations with variant filtering using a Jupyter notebook format.

## Contributing

1. Fork it (<https://github.com/krpopkin/Trello-App/fork>)  
2. Create your feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am "Add foo feature"`)  
4. Push to the branch (`git push origin feature/foo`)  
5. Open a Pull Request

## License

This project is currently unlicensed. If you’d like to open-source it under a standard license, consider adding an [MIT](https://opensource.org/licenses/MIT) or [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license file.

## Author

**Ken Popkin**  
*GitHub:* [@krpopkin](https://github.com/krpopkin)  
*Email:* krpopkin@gmail.com

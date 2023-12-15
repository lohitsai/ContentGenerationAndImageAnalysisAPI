# Content Generation and Image Analysis API

## Introduction

This API allows users to Generate Product title as well as SEO (Search Engine Optimized Keywords). It also analyzes images and sends extracted keywords from the image.

    Note : Debug mode is True for testing purposes

## Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.10
- PIP

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lohitsai/ContentGenerationAndImageAnalysisAPI
   ```

2. Navigate to the project directory:

   ```bash
   cd ContentGenerationAndImageAnalysisAPI
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run Server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Generate Product Description and SEO keywords:**

  ```
  GET http://127.0.0.1:8000/api/product/<product-title>/
  ```

  Response Example:
  ![img](https://i.imgur.com/n5jVhCs.png)

- **Extract Keywords from an Image**

  ```
  POST http://127.0.0.1:8000/api/image/
  ```

  Request Body Data Format:

       Note: The Image Data should be sent in the "picture" Key in the Form Data

  ![img](https://i.imgur.com/6RqU53D.png)

  Response Example:
  ![img](https://i.imgur.com/z8o4JwX.png)

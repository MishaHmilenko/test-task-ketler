# test-task-ketlet
Test task for creating comments on photos.

## Project launching

 1. Clone repository
    ```
    git clone https://github.com/MishaHmilenko/test-task-ketler
    ```

 2. Create `.env` file
    ```
    SPREADSHEET_ID=your_spreadsheet_id
    AUTHORIZATION_GOOGLE_API_TOKEN=your_authorization_google_token
    COMMENT_GENERATOR_API_TOKEN=your_comment_generator_api_token
    ```
    
 3. Install dependencies
    ```
    pip install poetry
    poetry isntall
    ```
    
 4. Set `PYTHONPATH`
    ```
    $env:PYTHONPATH="C:/Users/your_username/Projects/test-task-ketler"
    ```
    
 5. Run script
    ```
    python src/main.py
    ```

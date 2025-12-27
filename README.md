# Short Fetcher

A Streamlit web application that fetches video descriptions from YouTube Shorts using the YouTube Data API v3.

## Features

- 🎥 Extract video descriptions from YouTube Shorts URLs
- 🔐 Secure API key input (password-masked)
- 📋 Easy-to-use web interface
- 🔗 Supports multiple YouTube URL formats (shorts/, v=, be/)

## Prerequisites

- Python 3.11 or higher
- YouTube Data API v3 key from Google Cloud Console
- `uv` package manager (recommended) or `pip`

## Installation

### Using uv (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd short-fetcher
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run streamlit run app.py
   ```

### Using pip

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd short-fetcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or install directly:
   ```bash
   pip install streamlit google-api-python-client youtube-transcript-api
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Getting a YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the **YouTube Data API v3**
4. Navigate to **Credentials** > **+ Create Credentials** > **API Key**
5. Copy your API key

## Usage

1. Start the application using one of the methods above
2. Open your browser to the URL shown in the terminal (typically `http://localhost:8501`)
3. Enter your YouTube API key in the sidebar
4. Paste a YouTube Shorts URL in the input field
5. Click **Fetch Description** to retrieve the video description

### Supported URL Formats

The application supports the following YouTube URL formats:
- `https://www.youtube.com/shorts/VIDEO_ID`
- `https://youtube.com/shorts/VIDEO_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Project Structure

```
short-fetcher/
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Dependency lock file
└── README.md          # This file
```

## Dependencies

- `streamlit>=1.52.2` - Web framework for the application
- `google-api-python-client>=2.187.0` - YouTube Data API client
- `youtube-transcript-api>=1.2.3` - YouTube transcript API (for future features)

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]


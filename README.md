# Side School Portfolio

A modern web portfolio project with live reload functionality for seamless development.

## Project Overview

This project is a web portfolio that includes:
- A responsive web interface
- Live reload functionality for development
- Custom favicon support
- Modern web development features

## Features

- **Live Reload**: Automatic page refresh when files are modified
- **Development Server**: Built-in HTTP server with WebSocket support
- **Favicon Support**: Custom favicon generation and management
- **Modern Web Standards**: HTML5, CSS3, and JavaScript support

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sideschool-portfolio.git
cd sideschool-portfolio
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the development server:
```bash
python server.py
```

2. The server will automatically:
   - Start on port 8000
   - Open your default web browser to `http://localhost:8000`
   - Enable live reload functionality
   - Watch for file changes

3. To stop the server, press `Ctrl+C` in the terminal.

## Project Structure

- `index.html`: Main webpage
- `server.py`: Development server with live reload
- `resize_favicon.py`: Favicon generation utility
- `requirements.txt`: Python dependencies
- `site.webmanifest`: Web app manifest file
- `favicon/`: Directory containing favicon assets

## Development

The project uses a custom development server that provides:
- Automatic page reloading when files are modified
- WebSocket-based communication for live updates
- Proper MIME type handling
- Cache control headers for development

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
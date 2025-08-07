# Domain Availability Checker

A Flask-based web application that helps users check domain name availability and provides intelligent domain name suggestions using OpenAI's API.

## 🚀 Features

- ✨ Real-time domain availability checking using WHOIS API
- 🤖 AI-powered domain name suggestions using OpenAI
- 📧 Email notification system for domain status updates
- 🌐 Support for multiple Top Level Domains (TLDs)
- 💅 Clean and responsive user interface

## 🏗️ Project Structure

```
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── data/
│   └── tld_list.json      # List of supported TLDs
├── services/
│   ├── domain_checker.py  # Domain availability checking service
│   ├── notifier.py        # Email notification service
│   └── suggestions.py     # Domain name suggestion service
├── static/
│   └── style.css         # Application styling
├── templates/
│   └── email_template.html # Email notification template
└── utils/
    └── helpers.py        # Utility functions
```

## 🛠️ Prerequisites

- Python 3.7 or higher
- WHOIS API key
- OpenAI API key
- Flask

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/Venkat8161/Domain_Availability_Checker.git
cd Domain_Availability_Checker
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Unix or MacOS
source venv/bin/activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add the following variables:
```
WHOIS_API_KEY=your_whois_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
FLASK_ENV=development
```

## 🚀 Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

## 💡 Usage

1. Enter your desired domain name in the search box
2. Select TLD options (optional)
3. Click "Check Availability"
4. View results including:
   - Domain availability status
   - AI-generated domain suggestions
   - Similar available domains
5. Optionally enable email notifications for domain status updates

## 🔧 Configuration

The application can be configured through the following environment variables:
- `WHOIS_API_KEY`: Your WHOIS API key for domain checking
- `OPENAI_API_KEY`: Your OpenAI API key for AI suggestions
- `FLASK_ENV`: Application environment (development/production)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- OpenAI for providing the AI suggestions API
- WHOIS API for domain availability checking
- Flask community for the excellent web framework

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

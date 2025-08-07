from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

WHOIS_API_KEY = os.getenv("WHOIS_API_KEY")


def check_domain_availability(domain):
    url = f"https://domain-availability.whoisxmlapi.com/api/v1"
    params = {
        "apiKey": WHOIS_API_KEY,
        "domainName": domain,
        "outputFormat": "JSON"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'DomainInfo' in data:
        return data['DomainInfo']['domainAvailability'] == 'AVAILABLE'
    else:
        return False


def generate_alternative_domains(base_name):
    # Sample suggestions, expand later with LLM or heuristics
    suffixes = [".xyz", ".co", ".io", "app.com", "online", "site"]
    suggestions = []

    for s in suffixes:
        domain = f"{base_name}.{s}" if '.' not in s else f"{base_name}{('.' if s[0] != '.' else '')}{s}"
        if check_domain_availability(domain):
            suggestions.append(domain)

    return suggestions


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("domain_input").strip().lower()
        if "." in user_input:  # full domain
            is_available = check_domain_availability(user_input)
            alternatives = generate_alternative_domains(user_input.split(".")[0]) if not is_available else []
            return render_template("result.html", domain=user_input, available=is_available, alternatives=alternatives)
        else:
            # brand name input – suggest domains
            suggestions = generate_alternative_domains(user_input)
            return render_template("result.html", brand=user_input, suggestions=suggestions)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# Auto-i18

**Auto-i18** is a Python-based tool that automates translation of JSON language files using the [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) multilingual model. It supports over 200 languages and is ideal for internationalizing applications efficiently.

## Features

- Translate entire JSON files into supported target languages
- Uses the state-of-the-art NLLB (No Language Left Behind) model
- Simple command structure and extendable architecture
- Automatically saves translated files with language-based filenames

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Forsrobin/auto-i18.git
cd auto-i18
```

2. Install dependencies:

```bash
pip install transformers torch
```

## Usage

Prepare a source JSON file in UTF-8 encoding, e.g., `messages/master.json`.

Example usage:

```python
from translator import Translator

translator = Translator("messages/master.json")
translated = translator.start("fra_Latn")  # Translate to French
```

This will generate `messages/fra_Latn.json` with all translated strings.

## Supported Languages

The tool includes a comprehensive list of over 200 supported languages, each defined by its readable name and internal language code (e.g., `"French": "fra_Latn"`).

You can verify if a language is supported using:

```python
translator.check_if_language_exists("fra_Latn")
```

## Directory Structure

```
auto-i18/
├── messages/
│   └── master.json       # Your source language file
├── translator.py         # Main translation logic
├── README.md
```

## License

This project is licensed under the MIT License.

## Disclaimer

Translation quality may vary by language. Always review translated output before using in production environments.

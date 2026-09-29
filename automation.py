import json
import re
from datetime import date
from pathlib import Path

JSON_FILE = Path("age.json")
README_FILE = Path("README.md")

data = json.loads(JSON_FILE.read_text())

birth_date = date.fromisoformat(data["birth_date"])
today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

data["age"] = age
JSON_FILE.write_text(json.dumps(data, indent=4) + "\n")

readme = README_FILE.read_text()

readme = re.sub(
    r'<h4 id="age">Age : \d+</h4>',
    f'<h4 id="age">Age : {age}</h4>',
    readme
)

README_FILE.write_text(readme)
import json

messy_data = [
    "  john doe, JOHN@EXAMPLE.COM ",
    "jane smith, jane@example.com",
    "   ",
    "  mike brown, MIKE@EXAMPLE.COM  ",
]


def clean_inputs(items):
    result = []

    for item in items:
        # Remove extra spaces and convert to lowercase
        cleaned = item.strip().lower()

        # Ignore empty values
        if not cleaned:
            continue

        # Split name and email
        parts = cleaned.split(",")

        if len(parts) == 2:
            name = parts[0].strip()
            email = parts[1].strip()

            result.append({"name": name.title(), "email": email})

    return result


cleaned_data = clean_inputs(messy_data)

print(cleaned_data)


with open("cleaned.json", mode="w") as f:
    json.dump(cleaned_data, f, indent=4)
with open("cleaned.json", mode="r") as f:
    data = json.load(f)
    print(f"data from cleaned.json: {data}")

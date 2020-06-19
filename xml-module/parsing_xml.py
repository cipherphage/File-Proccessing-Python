import sys
import defusedxml.ElementTree as ET 

file_name = "products.xml"

try:
    tree = ET.parse(file_name)
except FileNotFoundError:
    print(f"File not found: {file_name}")
    sys.exit(1)

for product in tree.findall("product"):
    name = product.findtext("name")
    description = product.findtext("description")
    price = product.find("price")
    currency = price.get("currency") or "USD"

    if currency == "EUR":
        price_text = f"{price.text.replace('.',',')} \u20ac"
    else:
        price_text = f"${price.text}"

    message = f"""
    {name} - {price_text}
    {description}"""

    print(message)
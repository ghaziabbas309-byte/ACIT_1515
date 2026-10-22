#csv_text = """lunch,bento box b - sashimi,box combo,$9.59
#dinner,vegetable sushi,6 rolls,$3.50
#dinner,tuna roll,3 rolls,$4.50
#dinner,roe,2 rolls,$3.95
#lunch,bento box a - chicken teriyaki,box combo,$8.59"""


from menu_data import csv_text

def parse_csv(text):
    """Parses the CSV text into a list of item dictionaries."""
    items = []
    lines = text.strip().split("\n")
    for line in lines:
        parts = line.split(",")
        if len(parts) == 4:
            category = parts[0].strip()
            name = parts[1].strip()
            quantity = parts[2].strip()
      
            price = float(parts[3].strip().replace("$", "")) * 1.8
            
            items.append({
                "category": category,
                "name": name,
                "quantity": quantity,
                "price": price
            })
    return items

def group_and_sort_items(items):
    """Groups items by category and sorts them alphabetically by name."""
    grouped = {}
    for item in items:
        cat = item["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(item)
    
   
    for cat in grouped:
        grouped[cat].sort(key=lambda x: x["name"])
        
    return grouped

def format_menu(grouped_items):
    """Formats the menu into the required text layout."""
    output_lines = []
    
    for category, items in sorted(grouped_items.items()):
        category_title = f"- {category.capitalize()} Items *"
        output_lines.append(category_title)
        
        for item in items:
            price_formatted = f"${item['price']:.2f}"
            line = f" {price_formatted}\t{item['name']}, {item['quantity']}"
            output_lines.append(line)
        
        output_lines.append("")
        
    return "\n".join(output_lines).strip()

def main():
    items = parse_csv(csv_text)
    grouped_items = group_and_sort_items(items)
    formatted_output = format_menu(grouped_items)
    print(formatted_output)

if __name__ == "__main__":
    main()
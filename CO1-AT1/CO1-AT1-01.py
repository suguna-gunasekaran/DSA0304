import re
 
# ---------------------------------------------------------------------
# Sample product catalogue
# ---------------------------------------------------------------------
products = [
    "Wireless Mouse", "Wireless Keyboard", "Bluetooth Headphones",
    "Gaming Laptop", "Laptop Stand", "USB-C Charger", "Smartwatch",
    "Smartphone Case", "Wireless Earbuds", "Mechanical Keyboard",
    "4K Monitor", "Portable Charger", "Laptop Bag", "Noise Cancelling Headset",
]
 
 
def search_exact(keyword):
    """Exact (whole product name) match, case-sensitive."""
    pattern = re.compile(rf"^{re.escape(keyword)}$")
    return [p for p in products if pattern.match(p)]
 
 
def search_prefix(prefix):
    """Products whose name starts with the given prefix (case-insensitive)."""
    pattern = re.compile(rf"^{re.escape(prefix)}", re.IGNORECASE)
    return [p for p in products if pattern.match(p)]
 
 
def search_suffix(suffix):
    """Products whose name ends with the given suffix (case-insensitive)."""
    pattern = re.compile(rf"{re.escape(suffix)}$", re.IGNORECASE)
    return [p for p in products if pattern.search(p)]
 
 
def search_partial(keyword):
    """Products containing the keyword anywhere (case-insensitive)."""
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [p for p in products if pattern.search(p)]
 
 
def search_case_insensitive(keyword):
    """Case-insensitive whole-word search."""
    pattern = re.compile(rf"\b{re.escape(keyword)}\b", re.IGNORECASE)
    return [p for p in products if pattern.search(p)]
 
 
def display_results(title, results):
    print(f"\n{title}")
    print("-" * 50)
    if results:
        for r in results:
            print(f"  -> {r}")
    else:
        print("  No matching products found.")
    print(f"  Total matches: {len(results)}")
    return len(results)
 
 
def main():
    print("=" * 55)
    print(" PRODUCT SEARCH SYSTEM")
    print("=" * 55)
    print(f"\nProduct Catalogue ({len(products)} items):")
    for p in products:
        print(f"  * {p}")
 
    report = {}
 
    report["Exact Search: 'Gaming Laptop'"] = display_results(
        "1. EXACT SEARCH -> 'Gaming Laptop'", search_exact("Gaming Laptop"))
 
    report["Prefix Search: 'Wireless'"] = display_results(
        "2. PREFIX SEARCH -> 'Wireless'", search_prefix("Wireless"))
 
    report["Suffix Search: 'Keyboard'"] = display_results(
        "3. SUFFIX SEARCH -> 'Keyboard'", search_suffix("Keyboard"))
 
    report["Partial Search: 'phone'"] = display_results(
        "4. PARTIAL SEARCH -> 'phone'", search_partial("phone"))
 
    report["Case-Insensitive Search: 'laptop'"] = display_results(
        "5. CASE-INSENSITIVE SEARCH -> 'laptop'", search_case_insensitive("laptop"))
 
    print("\n" + "=" * 55)
    print(" SEARCH REPORT SUMMARY")
    print("=" * 55)
    for query, count in report.items():
        print(f"  {query:<38}: {count} match(es)")
 
 
if __name__ == "__main__":
    main()
 

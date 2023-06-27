from page import Page

page = Page(275680888)

print("Page Information: ")
print(f"""
Title: {page.title}
Price: {page.price} NOK
Description: {page.description}
Sold: {page.sold}

City: {page.location["postalPlace"]}
Categories: {page.categories}
""")
from flask import Flask, render_template, redirect, url_for, request, session
from config import get_db

app = Flask(__name__)
app.secret_key = "your_secret_key"   # change for production


# -------------------------------
#  HOME PAGE (PRODUCT LIST)
# -------------------------------
@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cat = request.args.get("category")

    if cat:
        # case-insensitive compare
        cursor.execute("SELECT * FROM products WHERE LOWER(category) = LOWER(%s)", (cat,))
    else:
        cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()
    return render_template("index.html", products=products, category=cat)


# -------------------------------
#  ADD TO CART (SESSION CART)
# -------------------------------
@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    # If session cart doesn't exist → create one
    cart = session.get("cart", [])
    cart.append(product_id)
    session["cart"] = cart
    session.modified = True
    return redirect(url_for("cart"))


# -------------------------------
#  VIEW CART (works for 1 or many ids)
# -------------------------------
@app.route("/cart")
def cart():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cart = session.get("cart", [])

    # Empty cart handling
    if not cart:
        return render_template("cart.html", items=[], total=0)

    # Build parameterized placeholders (%s,%s,...) based on cart length
    format_strings = ",".join(["%s"] * len(cart))
    query = f"SELECT id, name, price, description, image, category FROM products WHERE id IN ({format_strings})"

    # execute with tuple of ids (works for single id too)
    cursor.execute(query, tuple(cart))
    items = cursor.fetchall()

    # preserve order and duplicates (session may have same id multiple times)
    # items_from_db is unique rows; we need to create final_items per cart list to reflect duplicates
    id_to_item = {item['id']: item for item in items}
    final_items = []
    for pid in cart:
        if pid in id_to_item:
            final_items.append(id_to_item[pid])

    total = sum(item["price"] for item in final_items)

    return render_template("cart.html", items=final_items, total=total)


# -------------------------------
#  REMOVE ONE ITEM FROM CART (removes first occurrence)
# -------------------------------
@app.route("/remove/<int:product_id>")
def remove_item(product_id):
    cart = session.get("cart", [])
    if product_id in cart:
        cart.remove(product_id)  # removes first occurrence
        session["cart"] = cart
        session.modified = True
    return redirect(url_for("cart"))


if __name__ == "__main__":
    app.run(debug=True)

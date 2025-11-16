from flask import Flask, render_template, redirect, url_for, request, session
from config import get_db

app = Flask(__name__)
app.secret_key = "your_secret_key"   # Needed for session cart


# -------------------------------
#  HOME PAGE (PRODUCT LIST)
# -------------------------------
@app.route("/")
def index():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cat = request.args.get("category")

    if cat:
        cursor.execute("SELECT * FROM products WHERE category=%s", (cat,))
    else:
        cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()
    return render_template("index.html", products=products, category=cat)


# -------------------------------
#  ADD TO CART (SESSION CART)
# -------------------------------
@app.route("/add/<int:id>")
def add_to_cart(id):

    # If session cart doesn't exist → create one
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect(url_for("cart"))


# -------------------------------
#  VIEW CART
# -------------------------------
@app.route("/cart")
def cart():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Empty cart handling
    if "cart" not in session or len(session["cart"]) == 0:
        return render_template("cart.html", items=[], total=0)

    cart_ids = session["cart"]

    # Convert list into tuple for SQL query
    ids_tuple = tuple(cart_ids)

    query = f"SELECT * FROM products WHERE id IN {ids_tuple}"
    cursor.execute(query)

    items = cursor.fetchall()

    total = sum(item["price"] for item in items)

    return render_template("cart.html", items=items, total=total)


# -------------------------------
#  REMOVE ONE ITEM FROM CART
# -------------------------------
@app.route("/remove/<int:id>")
def remove_item(id):
    if "cart" in session:
        if id in session["cart"]:
            session["cart"].remove(id)
            session.modified = True

    return redirect(url_for("cart"))


if __name__ == "__main__":
    app.run(debug=True)

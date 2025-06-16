const express = require('express');
const path = require('path');
const mysql = require('mysql2');
const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');

// MySQL connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'local_store'
});

db.connect(err => {
  if (err) throw err;
  console.log('MySQL Connected');
});

// In-memory cart (with quantity)
let cart = [];

// Home page with optional category filter
app.get('/', (req, res) => {
  const category = req.query.category;
  let sql = 'SELECT * FROM products';
  let values = [];

  if (category) {
    sql += ' WHERE category = ?';
    values.push(category);
  }

  db.query(sql, values, (err, results) => {
    if (err) throw err;
    res.render('index', { products: results });
  });
});
app.get('/add-to-cart/:id', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT * FROM products WHERE id = ?';
  db.query(sql, [id], (err, results) => {
    if (err) throw err;
    if (results.length > 0) {
      cart.push(results[0]);  // ✅ Add to cart
    }
    res.redirect('/cart');    // ✅ Redirect to cart (optional)
  });
});


// View cart
app.get('/cart', (req, res) => {
  let total = 0;
  cart.forEach(p => total += Number(p.price)); // ✅ Ensure price is treated as number
  res.render('cart', { cart, total });        // ✅ total is now passed
});
// Remove from cart
app.get('/remove-from-cart/:id', (req, res) => {
  const id = parseInt(req.params.id);
  cart = cart.filter(p => p.id !== id);
  res.redirect('/cart');
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

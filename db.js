const mysql = require('mysql');

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '', // use your password here
  database: 'local_store'
});

db.connect((err) => {
  if (err) throw err;
  console.log('MySQL connected!');
});

module.exports = db;

var mysql = require('mysql');
var conn = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: '',
    database:'test',
    port: 3306
});
conn.connect();
conn.query('SELECT count(1) as solution from p_role', function(err, rows, fields) {
    if (err) throw err;
    console.log('The solution is: ', rows[0].solution);
});
conn.end();
var express = require('express');

var app = express();

app.use(express.static(__dirname + '/static'));

var db = {};

app.get('/woo', function(req, res) {
  var token = req.query.oauth_token;
  db[0] = token;
  res.render('logged_in.html', { token: token });
});

app.listen(3000);

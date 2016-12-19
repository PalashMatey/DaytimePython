var express = require('express');
var path = require('path')
//instantiate Express
var app = express();

//Set up REST responses
app.get('/', function(req, res){
  res.send('Hello from Express!');
});

app.get('/about',function(req,res){
    res.sendFile(path+ 'index.html');
});
//Start the server
app.listen(4000, function(){
  console.log("Express running on port 4000.");
});
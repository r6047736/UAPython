var express = require('express');
var app = express();
var fs = require("fs");
var exec = require('child_process').exec;
var colors = require('colors/safe');
var BASEDIR = __dirname;

app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});




app.get('/listUsers', function (req, res) {
    fs.readFile( __dirname + "/" + "user.json", 'utf8', function (err, data) {
        console.log( data );
        res.end( data );
    });
})




app.get('/readfile/:fileName',function(req,res){
    var filename = req.params.fileName;


    fs.readFile( BASEDIR+"/"+filename,'utf8', function(err, data){

        if (err)
            res.send(JSON.stringify(err));
        else
            res.send(JSON.stringify(data));
        console.log(data || err);

    });

})

app.get('/runcmd/:cmd',function(req,res){
    var cmd = req.params.cmd;
    console.log(" your enter a command ", cmd);

    runcomd(cmd,res);
});

app.get('/current', function (req, res) {
/*
    fs.readdir(__dirname, function(err, items) {
        console.log(items);

        for (var i=0; i<items.length; i++) {
            console.log(items[i]);
        }
    });
    */

    exec("ls "+__dirname, function(err,stdout,stderr){
        if(err) {
          //  console.log(colors.blue(err));
        }
        else if(stderr){
           // console.log(colors.red('stderr',stderr));
        }
        else {
            //   var data = JSON.parse(stdout);
          //  console.log(colors.green(stdout));
        }
        res.send( JSON.stringify(stderr || err || stdout) );
    });



})


var runcomd = function(command,res){




    exec(command, function(err,stdout,stderr){
        if(err) {
            console.log(colors.blue(err));
        }
        else if(stderr){
            console.log(colors.red('stderr',stderr));
        }
        else {

            //   var data = JSON.parse(stdout);
            console.log(colors.green(stdout));
        }
        res.send( JSON.stringify(stderr || err || stdout) );
    });

}





var server = app.listen(8081,'localhost', function () {

    var host = server.address().address
    var port = server.address().port

    console.log("Example app listening at http://%s:%s", host, port)

})


var express = require('express');

var app = express();
var fs = require("fs");
var exec = require('child_process').exec;
var spawn= require('child_process').spawn;
var multer = require('multer');
var storage = multer.diskStorage({
    destination: function(req,file,callback){

        callback(null,'./uploads');
    },
    filename:function(req,file,callback){


        callback(null, file.originalname + new Date());
    }
})
var upload = multer({storage:storage}).single('pyfiles');

var assigns = [
    {name:"a5", id:"a5",num:"5"},
    {name:"a6", id:"a6",num:"6"},
    {name:"a7", id:"a7",num:"7"}];



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



app.get('/assignList',function(req,res){
    res.send(assigns);


})




app.post('/upload',function(req,res){

console.log("request")


    upload(req,res,function(err){
        if (err){
            console.log(err);
            return res.end("error uploading file")
        }



        var dir = 'root/'+req.body.num+"tests/uploads/"+ req.body.dir;

        if (!fs.existsSync(dir)){
            fs.mkdirSync(dir);
        }

        if (!req.file || !req.body.num ){
               console.log("No file")
            //res.send("No file uploaded")
            return;
        }
console.log(req.body)
        movefile(req.file.path,dir+"/"+ req.file.originalname);



    })

})


app.get('/getfiles',function(req,res){
    var dir = req.query.studentDir;
    var assignId = req.query.assigId;
    if (!assignId)
        return;

    fs. readdir("root/"+assignId+"tests/uploads/"+dir , function(err, items) {

        if (!fs.existsSync("root/"+assignId+"tests/uploads/"+dir)){
            fs.mkdirSync("root/"+assignId+"tests/uploads/"+dir);
        }

        if (err){
            console.log(err);

        }
        console.log(items)
        res.send(items);


    })


})



function movefile (tmpDir, finalDir){
    var source = fs.createReadStream(tmpDir);
    var dest = fs.createWriteStream(finalDir);

    source.pipe(dest);
    source.on('end', function() {
        fs.unlink(tmpDir);

    });
    source.on('error', function(err) { /* error */ });
}


app.get('/test/',function(req,res){
    var asId = req.query.assigNum;
    var studentworkingDir = req.query.currentDir ;
    var assignmentworkingDir;

    console.log(req.query);

    var re ="";

    deploySh  =spawn("bash",['test-all.sh','../tatt/','../uploads/'+studentworkingDir],{
        cwd: BASEDIR +'/root/'+asId+'tests/tests'
    })


    deploySh.stdout.on('data', function(data){
        console.log(data);
        re += data;
    });

    deploySh.stderr.on('data', function(data) {
        console.log(data);
        re += data;
    });
    deploySh.on('close', function(code) {
        if (code !== 0) {

            res.send(JSON.stringify(re));
        }

    });



})


var server = app.listen(8081,'localhost', function () {

    var host = server.address().address
    var port = server.address().port

    console.log("Example app listening at http://%s:%s", host, port)

})


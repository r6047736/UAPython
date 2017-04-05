var express = require('express');

var app = express();
var fs = require("fs-extra");
var Promise = require('bluebird');
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

var assNumToassName={
    "a5":"puter-1",
    "a6":"hangman",
    "a7":"puter-2"
}



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
        if (!req.body.num){
            return res.end("No assignment number selected")
        }

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
       // console.log(items)
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
    console.log("checking the tests directory...exist?")

    //check the current student directory exist "tests" folder? If not copy from
    if (!fs.existsSync("root/"+asId+"tests/uploads/"+studentworkingDir+"/tests")){
        console.log("directory does not existed");
        //create dir first, other wise throws error
        fs.mkdirSync("root/"+asId+"tests/uploads/"+studentworkingDir+"/tests");
        // COPY TESTS FOLDER TO STUDENT WORK DIR
        fs.copySync("root/"+asId+"tests/tests", "root/"+asId+"tests/uploads/"+studentworkingDir+"/tests");
    }
    else{
        console.log("dir existed , skip")
    }

    console.log("finish checking")

    var re ="";

    var deploySh  = spawn("bash",['test-all.sh','../../../tatt/','../'],{
        cwd: BASEDIR +'/root/'+asId+'tests/uploads/'+studentworkingDir+'/tests'
    });


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

    deploySh.on('error', function( err ){ console.log(err)  })

})








app.get("/tests_names/",function(req,res){

            var assignId = req.query.id;
            var studentWrokingDir = req.query.dir;
            var assignmentDir = assNumToassName[assignId];

            if (!assignId || !studentWrokingDir || !assignmentDir)
                return;

           // console.log("get all of diff files ",assignId ,",",studentWrokingDir,",",assignmentDir )
            dir  = "root/"+assignId+"tests/uploads/"+studentWrokingDir+"/tests/"+assignmentDir;


            var testsnames = readAllfolders( dir)

            //res.send(testsnames);

            var result = [];




            var promises = [];

            for ( var i in testsnames){
                var a = {
                    name:testsnames[i],
                    actual:'',
                    expected:''
                }
                result.push(a);
                var name = a.name;

                var p1 =
                    new Promise(function(resolve,reject){


                        var test_name = name;  // save to a new variable, cus name is changing
                        var test_index = i;
                        fs.readFile(dir + "/" + test_name+"/actual.txt","utf-8", function(err, data){



                            if (err)
                                reject(err);
                            else
                            {
                                //addActualOutput(result,test_name,"actual",data );
                                result[test_index].actual = data;
                                resolve(data);
                            }

                        });
                    })

                var p2 = new Promise(function(resolve,reject){

                    var test_name2 =  name;    // save to a new variable, cus name is changing
                    var test_index2 = i;
                    fs.readFile(dir + "/" + test_name2+"/expected.txt","utf-8", function(err, data){

                        if (err)
                            reject(err);
                        else
                        {
                            //addActualOutput(result,test_name2,"expected",data );
                            result[test_index2].expected = data;
                            resolve(data);
                        }

                    });
                })

                promises.push(p1)
                promises.push(p2)





            }

    Promise.all(promises).then(function(data){
            res.send(result);
        }


    )







})










readAllfolders = function(dir){
    var f = [];
    files = fs.readdirSync(dir);

    files.forEach(function(folder){
        if (fs.statSync(dir+'/'+folder).isDirectory()){
            console.log(folder)
            f.push(folder);
        }
    })
    return f;
}


var server = app.listen(process.env.PORT || 8081,'localhost', function () {

    var host = server.address().address;
    var port = server.address().port;

    console.log("Example app listening at http://%s:%s", host, port)

    if (!fs.existsSync("uploads/")){
        fs.mkdirSync("uploads/");
    }


})


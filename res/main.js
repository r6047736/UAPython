
var SERVER = "http://127.0.0.1:8081";
var currentPath = "/";
var filetreePointer = null;


//$("#savedir").val(randomDirectory);
//alert(randomDirectory);


angular.module('UAPython', [])

    .controller('IDEcontroller', function($scope,$window) {
        $scope.randomDirectory = Date.now().toString();
        $scope.assigmentList =[];
        $scope.assignId = "";
        $scope.currentUploadedFiles = [];


            $scope.relativepath = $window.currentPath;
            $scope.filetree =[];

        $("#clean_actual").on('click',function(){
            //console.log($scope.assignId );
            $("#actual_text").html("");
        })

        $('#test').on('click',function(){

            $.get(SERVER+'/test', { currentDir:  $scope.randomDirectory , assigNum: $scope.assignId.id },function(data){

                    $("#actual_text").html("<pre>"+JSON.parse(data)+"</pre>" + $("#actual_text").html() );

                }
            )
        })

        $("#fileupload").on('change',function(){

            $("#submitButton").html(this.files[0].name)

        });








        $scope.readdir=function(){

            $.get(SERVER+'/getfiles', { studentDir:  $scope.randomDirectory ,assigId:  $scope.assignId.id  },function(data){

                    console.log(data);
                    $scope.currentUploadedFiles = data;
                    $scope.$apply();
                }
            )
        }

        var t = setInterval(function(){
            $scope.readdir();
        }, 5000)



        function getAssList(){

          $.get(SERVER+'/assignList',function(data){
              console.log(data);
              $scope.assigmentList = data;
              $scope.$apply();
              console.log($scope.assigmentList);

          })
        }
        getAssList();





















    });




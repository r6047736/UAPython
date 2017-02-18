
var SERVER = "http://127.0.0.1:8081";
var currentPath = "";




angular.module('UAPython', [])
    .controller('IDEcontroller', function($scope) {
            $scope.filetree =[];



        $("#clean_actual").on('click',function(){
            $("#actual_text").html("");
        })

        $('#runcmd').on('click',function(){
            var cmd = $("#cmd_text").val();
            if (!cmd)
                return;
            $.get(SERVER+'/runcmd/'+cmd, function(data){
                    $("#actual_text").html("<pre>"+JSON.parse(data)+"</pre>" + $("#actual_text").html() );
                    ///$("#actual_text").append("<pre>"+JSON.parse(data)+"</pre>")
                }
            )
        })

        $scope.getfiletree = function(){
            $.get(SERVER+'/current', function(data){
                    // $("#filetree").html("<pre>"+JSON.parse(data)+"</pre>"  );

                    $scope.filetree = JSON.parse(data).split("\n");
                    $scope.$apply();
                });



        }



        var readfile = function(filename){
            $.get(SERVER+'/readfile/'+filename, function(data){
                $('#content').val(JSON.parse(data));
            });
        }









    });
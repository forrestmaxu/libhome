$(document).ready(function(){


    //主对话框
    $(".editlawtext").click(function(){
        var dataid=$(this).attr("data-id")    
        console.log(dataid)  
        $("#editlawdialog").css("display","block");
        $(".body-content").css("background-color","rgb(131, 128, 124)")
        $("#ok").attr("data-id",dataid)
    });

    $("#ok").click(function(){
        // console.log('ok')
        var key=$(this).attr('data-id');
        var selectvalue=$("input[name='isedit']:checked").val();
        console.log(selectvalue);
        var data={"key":key,"value":selectvalue}
        $.ajax({
            url: "http://127.0.0.1:5000/upd_lawcontent_isedit",
            data:data,
            type: 'post',
            success: function (data) {
               console.log(data)
            }
        })
        // 
        $("#editlawdialog").css("display","none");
        $(".body-content").css("background-color","white")
        window.location.reload()
    });

    $("#cancel").click(function(){
        // console.log('ok')
        $("#editlawdialog").css("display","none");
        $(".body-content").css("background-color","white");
    });


    $(".editstate").click(function(){
        var dataid=$(this).attr("data-id")    
        console.log(dataid)  
        $("#statedialog").css("display","block");
        $(".body-content").css("background-color","rgb(131, 128, 124)")
        $("#ok-state").attr("data-id",dataid)
    });

    $("#ok-state").click(function(){
        // console.log('ok')
        var dataid=$("#ok-state").attr("data-id")
        console.log("")
        var selectvalue=$("input[name='state']:checked").val();
        console.log(selectvalue)
        // window.location.reload()
        data={"dataid":dataid,"value":selectvalue}
            // console.log('ok')
        $.ajax({
            url: "http://127.0.0.1:5000/upd_lawcontent_state",
            data:data,
            type: 'post',
            success: function (data) {
                console.log(data)
            }
        })
        $("#statedialog").css("display","none");
        $(".body-content").css("background-color","white");
      
    });

    $("#cancel-state").click(function(){
        // console.log('ok')
        $("#statedialog").css("display","none");
        $(".body-content").css("background-color","white");
    });


    $(".editflag").click(function(){
        var dataid=$(this).attr("data-id")    
        console.log(dataid)  
        $("#flagdialog").css("display","block")
        $(".body-content").css("background-color","rgb(131, 128, 124)")
        $("#ok-flag").attr("data-id",dataid)
        $("#flag-body").html('')
        $.ajax({
            url: "http://127.0.0.1:5000/listflag-data",
            type: 'get',
            success: function (data) {
               var flags=JSON.parse(data)
            //    console.log()
               for(var i=0;i<flags.length;i++){
                   console.log(flags[i]['flagname'])
                   $("#flag-body").append("<label><input name=\"flag\" type=\"checkbox\" value="+flags[i]['flagname']+" />"+flags[i]['flagname'] +"</label>" )
               }
               
            }
        })
    });

    $("#ok-flag").click(function(){
        // console.log('ok')
        // var selectvalue=$("input[name='flag']:checked").val();
        var contentid=$(this).attr("data-id")  
        var obj=$("input[name='flag']")
        var flags=[]
        console.log(obj.length)
        for(var i=0;i<obj.length;i++){
            if(obj[i].checked) {
                flags+=(obj[i].value+"|")
            }
        }
        if(flags.length==0){
            alert("输入复选框值")
        }
        data={"flags":flags,"contentid":contentid}
        $.ajax({
            url: "http://127.0.0.1:5000/addcontentflag",
            type: 'post',
            data: data,
            success: function (data) {
            //    var flags=JSON.parse(data)
               console.log(data)
            }

        })
        $("#flagdialog").css("display","none");
        $(".body-content").css("background-color","white");
      
    });

    $("#cancel-flag").click(function(){
        // console.log('ok')
        $("#flagdialog").css("display","none");
        $(".body-content").css("background-color","white");
    });


    $(".editrel").click(function(){
        var destlid=$(this).attr("data-id")    
        // console.log(dataid)  
        $("#rellawdialog").css("display","block");
        $(".body-content").css("background-color","rgb(131, 128, 124)")
        $("#ok-rel").attr("data-id",destlid)
    });

    $("#search-title").click(function(){
        $("#search-result").css("display","block")
        $("#search-footer").css("display","block")
        
        var titlekey=$("input[name='titlekey']").val()
        var textid=$("input[name='textid']").val()
        
        var textchild_no=$("input[name='textchild_no']").val()
        var lawtype=$("input[name='lawtype']:checked").val();
        var data={"titlekey":titlekey,"textid":textid,"textchild_no":textchild_no,"lawtype":lawtype}
        var tbody=$("#serach_content").html('')
        $.ajax({
            url: "http://127.0.0.1:5000/listcntByKey",
            type: 'post',
            data: data,
            success: function (data) {
            //    var flags=JSON.parse(data)
            //    console.log(data)
               var searchres=JSON.parse(data)
               console.log(searchres)
               
                for(var i=0;i<searchres.length;i++){
                    
                    tbody.append("<tr> <td>"+i+"</td><td>"+searchres[i]["title"] +"</td><td>"+
                    searchres[i]["content"]+"</td><td><input name=\"rel_sel_id\" data-id="+searchres[i]['lawid']
                 +"+"+ searchres[i]['id'] +"  type=\"radio\"/> </td></tr>" )
                }
            }

        })
    })

    $("#ok-rel").click(function(){
        // console.log('ok')
        var remoteid=$("input[name='rel_sel_id']:checked").attr('data-id');
        var localid=$(this).attr('data-id')
        console.log(remoteid)
        console.log(localid)
        data={"remoteid":remoteid,"localid":localid}
        $.ajax({
            url: "http://127.0.0.1:5000/addrel",
            type: 'post',
            data: data,
            success: function (data) {
            //    var flags=JSON.parse(data)
            //    console.log(data)
          
               console.log(data)
                
            }

        })
        // window.location.reload()
   
            // console.log('ok')
        // var sourceid=$("")
        $("#rellawdialog").css("display","none");
        $(".body-content").css("background-color","white");
      
    });

    $("#cancel-rel").click(function(){
        // console.log('ok')
        $("#rellawdialog").css("display","none");
        $(".body-content").css("background-color","white");
    });


});

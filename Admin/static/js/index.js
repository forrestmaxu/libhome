$(document).ready(function(){
    $("#lawadmin").click(function(){
        
    })

    $(".lawedit").click(function(){
        // console.log('hh')
        var lawid=$(this).attr("data-lawid")
        $("#ok-lawstate").attr("data-id",lawid)
        $("#laweditdialog").css("display","block")
        $(".body-content").css("background-color","rgb(131, 128, 124)")
    })

    $("#ok-lawstate").click(function(){
        // console.log('ok')
        var lawid=$(this).attr('data-id');
        var selectvalue=$("input[name='lawstate']:checked").val();
        console.log(selectvalue);
        console.log("lawid"+lawid);
        var lawtype=$("#lawtype option:selected").val()
        console.log(lawtype)
        var data={"lawid":lawid,"value":selectvalue,"lawtype":lawtype}
        $.ajax({
            url: "http://127.0.0.1:5000/upd_subject_state",
            data:data,
            type: 'post',
            success: function (data) {
               console.log(data)
            }
        })
        // 
        $("#laweditdialog").css("display","none");
        $(".body-content").css("background-color","white")
        // window.location.reload()
        // parent.location.reload()
    });

    $(".viewfulltext").click(function(){
        var lawid=$(this).attr('id')
        window.location.href = "/listlawcontent/"+lawid;
    })

    $("#cancel-lawstate").click(function(){
        // console.log('ok')
        $("#laweditdialog").css("display","none");
        $(".body-content").css("background-color","white");
    });

})
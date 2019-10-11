 $(function() {
            $('#getdata').click(function () {
                
                $.ajax({
                    url: "http://127.0.0.1:5000/listsubject",
                    type: 'post',
                    success: function (data) {
                        $('#sub_content').html(data)
                    }
                })                
                // window.location.href="listsubject";
            })

            $('#search').click(function () {
                var searchkey=$("#searchkey").val()
                console.log('111')
                data={"searchkey":searchkey}
                console.log(searchkey)
                $.ajax({
                    url: "http://127.0.0.1:5000/listsubBykey",
                    type: 'post',
                    data:data,
                    success: function (data) {
                        $('#sub_content').html(data)
                    }
                })                
                // window.location.href="listsubject";
            })
           
        });
$("#abc").on("click",function () {
    console.log($(this))
    var div = $("#delallpartdialog");
    console.log(div)
    div.css("display", "block");
    div.css("left", 400);

});
$(".dialog").on("click",".btnnoOk", function () {
alert("not ok");
$(this).parents(".dialog").css("display", "none");
});

$("#delallpartdialog").on("click",".btnok", function () {
alert("ok!");
$(this).parents(".dialog").css("display", "none");
});


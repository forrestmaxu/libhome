$(function(){
            	 
    
          
    function myfun(){ 　　 
        alert("this window.onload"); 　
        } 　　/*用window.onload调用myfun()*/　　
    window.onload = myfun;//不要括号
        
});
$(document).ready(function(){
    $(".article-thumb").click(function(){
        window.location=$(this).find("a").attr("href"); 
        return false;
   });   
});

/**
 * Created by leonard on 2015/12/31.
 */
 $(function(){
     $("#likes").one("click",function(){
         var url = "/like_category";
         var cat_id = $(this).attr("data-catid");
         var args = {"cat_id":cat_id};
         $.getJSON(url,args,function(data){
            $("#like_count").html(data);
            $('#likes').text("Liked");
         })
     })
 })
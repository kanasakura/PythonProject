//$(function(){
//    // お気に入りのクリック処理（style追加・削除）
//   $('#js-add-style').click(function(){
////    $(this).children('i').addClass('fas click-favorite-i');
////    $(this).children('i').removeClass('fa favorite-i');
//        likePost(this);
//   });
//
//   function likePost(thumb){
//   {% if user.is_authenticated %}
//    $(thumb).toggleClass('fas click-favorite-i');
//   }
//
//});

$(function(){

    $('#like-btn').on('click', function(){
      likePost(this);
    });

    function likePost(thumb){

        // Visual like button highlighting
        $(thumb).toggleClass('fas click-favorite-i')

        // route: /like/(id)
        // Take the index of the current like-button and add
        // 1 to it (so it starts at 1) to match the primary-key
        // of the database

        $.ajax({
          success: function(){
          }
        })
    }
});
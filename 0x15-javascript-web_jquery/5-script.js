$(function () {
  $("DIV#add_item").click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });
});

//OR
//document.querySelector('div#add_item').click(function () {
//    $('ul.my_list').first().append('<li>Item</li>');
//});

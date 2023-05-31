window.onload = function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
};

//OR
//$(function () {
//  const apiUrl = "https://stefanbohacek.com/hellosalut/?lang=fr";
//  $.get(apiUrl, function (data) {
//    $("DIV#hello").text(data.hello);
//  });
//});

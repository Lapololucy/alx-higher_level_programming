$(function () {
  const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  $.get(apiUrl, function (data, status) {
    $("DIV#character").text(data.name);
  });
});

//OR
//$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
//    $('div#character').html(data);
//});

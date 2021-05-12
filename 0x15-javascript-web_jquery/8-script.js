$(function()
{
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data, textStatus)
  {
    for (let i of data.results) {
    $('UL#list_movies').append("<li>" + i.title + "</li>");}
  });
});

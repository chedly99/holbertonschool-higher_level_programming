const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(this).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.getJSON(url + $('INPUT#language_code').val(), function (greeting) {
      $('DIV#hello').text(greeting.hello);
    });
  });
});

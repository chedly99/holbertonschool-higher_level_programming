const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(this).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.getJSON(url + $('INPUT#language_code').val(), function (greeting) {
      $('DIV#hello').text(greeting.hello);
    });
  });
  $('INPUT#language_code').keyup(function (k) {
    if (k.keyCode === 13) {
      $.getJSON(url + $(this).val(), function (greeting) {
        $('DIV#hello').text(greeting.hello);
      });
    }
  });
});

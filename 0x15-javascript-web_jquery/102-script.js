window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};

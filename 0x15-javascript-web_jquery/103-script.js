window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.Keycode === 13) {
      translate();
    }
  )};
};

function translate () {
  const language = $('INPUT#language_code').val();
  $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function (data) {
    $('DIV#hello').text(data.hello);
  });
}

const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
// Fetches the translation of “Hello” from this URL:
// https://fourtonfish.com/hellosalut/?lang=fr
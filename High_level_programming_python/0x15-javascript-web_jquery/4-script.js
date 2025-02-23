const $ = window.$;
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
  else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
}
);  // When the user clicks on DIV#toggle_header, the class of header must be toggled between red and green
const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
}
);  // When the user clicks on DIV#add_item, 
// a LI element must be added to UL.my_list   
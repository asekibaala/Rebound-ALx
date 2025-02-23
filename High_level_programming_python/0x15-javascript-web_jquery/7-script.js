const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, textStatus) {
  $('DIV#character').text(data.name);
}
);  // Fetches the character name from this URL: 
// https://swapi-api.hbtn.io/api/people/5/?format=json
// and displays it in the HTML’s tag DIV#character
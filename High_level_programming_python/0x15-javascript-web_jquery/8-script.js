const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
    if (data && data.results) {
        data.results.forEach(function (film) {
            if (film.title) {
                $('UL#list_movies').append('<li>' + film.title + '</li>');
            }
        });
    } else {
        console.error('No film data found');
    }
});  // Fetches and lists the titles for all movies from this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
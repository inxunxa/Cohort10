
function fetchData() {
    /**
     * create an ajax get to /api/movies
     * travel the response array
     * display each movie on the HTML
     */

     $.ajax({
        type: 'GET',
        url: '/api/movies',
        success: function(res) {
            console.log(res.objects);
            for(let i =0; i< res.objects.length; i++) {
                displayMovie(res.objects[i]);
            }
        },
        error: function(details) {
            console.log("Error", details);
        }
     });
}

function displayMovie(movie) {
    let syntax = 
    `
    <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="${movie.image_url}" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">${movie.title}</h5>
            <a href="/details/${movie.id}" class="btn btn-primary">View details</a>
        </div>
    </div>
    `;

    let container = $(".catalog-container");
    container.append(syntax);
}


function init() {
    console.log("catalog CSR page");

    fetchData();
}


window.onload = init;





function example_CreateGenre() {
    let newGe = {
        name:"created using JS"
    };

    $.ajax({
        type: "POST",
        url: '/api/genres/',
        contentType: 'application/json',
        data: JSON.stringify(newGe),
        success: function(res) {
          console.log( 'Yeii obj created')
        },
        error: function(details){
            console.log("Error", details);
        }
    });
}



function example_CreateMovie() {
    let movie = {
        title: 'created using JS',
        director : 'something',
        release_year : 2020,
        price : 123.23,
        image_url : 'something',
        description : 'A super expensive movie',
        genre :  "/api/genres/5/" // the id of the genre
    }

    $.ajax({
        type: "POST",
        url: '/api/movies/',
        contentType: 'application/json',
        data: JSON.stringify(movie),
        success: function(res) {
          console.log( 'Yeii obj created')
        },
        error: function(details){
            console.log("Error", details);
        }
    });
}
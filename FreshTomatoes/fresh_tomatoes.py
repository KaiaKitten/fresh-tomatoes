import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.5/superhero/bootstrap.min.css">
    
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        /* Start Edit */
        .center-y{
            display: table-cell;
            vertical-align: middle;
        }
        .button{
            font-size: 5em;
            width: 260px;
            height: 381px;
            line-height: 200px;
        }
        .navbar-inverse{
            background-color:#252525
        } 
        .panel-primary>.panel-heading{
            background-color:#252525
        }
        .panel-primary{
            width:260px;
            margin: auto;
            padding: 20px 20px 20px 20px;
        }
        .panel-body{
            padding: 0px;
        }
        body {
            padding-top: 80px;
            background-color:#454545
        }
        #add-form .modal-dialog{
            margin-top: 100px;
        }
        /* End Edit */
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var rating = $(this).attr('data-rating')
            var producer = $(this).attr('data-producer')
            var description = $(this).attr('data-description')
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            // Add rating,producer, and description to modal 
            $("#movie-info").empty().append("<div><ul class='list-group'><li class='list-group-item'><b>Rating</b>: " + rating + "</li><li class='list-group-item'><b>Producer</b>:" + producer + "</li><li class='list-group-item'><b>Description</b>: " + description + "</li></ul></div>");     
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').parent().hide().first().show("fast", function showNext() { //added .parent() as .movie-title was moved to be nested in div
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Add Movie Form Modal -->
    <div class="modal" id="add-form">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
              <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
          <div class="modal-header">
            <h4 class="modal-title">Add New Movie</h4>
          </div>  
          <div class="modal-body">
            <form class="form-horizontal" method="post" action="/cgi-bin/index.cgi">
              <fieldset>
                 <div class="form-group">
                   <label for="title" class="col-lg-2 control-label">Title</label>
                    <div class="col-lg-10">
                      <input class="form-control" name="title" id="Title" placeholder="Title" type="text">
                    </div>
                 </div>
                  <div class="form-group">
                   <label for="description" class="col-lg-2 control-label">Description</label>
                    <div class="col-lg-10">
                     <textarea class="form-control" name="description" rows="3" id="description"></textarea>
                    </div>
                 </div>
                 <div class="form-group">
                  <label for="select" class="col-lg-2 control-label">Rating</label>
                    <div class="col-lg-10">
                      <select class="form-control" name="rating" id="select">
                        <option>G</option>
                        <option>PG</option>
                        <option>PG-13</option>
                        <option>R</option>
                        <option>NR</option>
                      </select>
                    </div>
                 </div>
                 <div class="form-group">
                   <label for="producer" class="col-lg-2 control-label">Producer</label>
                    <div class="col-lg-10">
                      <input class="form-control" name="producer" id="Producer" placeholder="Title" type="text">
                    </div>
                 </div>
                 <div class="form-group">
                   <label for="trailer" class="col-lg-2 control-label">Youtube Trailer URL</label>
                    <div class="col-lg-10">
                     <input class="form-control" name="trailer" id="youtube-trailer" placeholder="Youtube Trailer URL" type="text">
                    </div>
                 </div>
                 <div class="form-group">
                   <label for="poster" class="col-lg-2 control-label">Poster URLr</label>
                    <div class="col-lg-10">
                     <input class="form-control" name="poster" id="Poster" placeholder="Poster URL" type="text">
                    </div>
                 </div>
                 <input type="submit" value="Submit">
              </fieldset>
            </form>
          </div>  
        </div>
      </div>
    </div>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container"></div>
          <div id="movie-info"></div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    <!-- Start Edit -->
    <div class="col-md-6 col-lg-4">
        <div class="panel panel-primary movie-tile" data-toggle="modal" data-target="#add-form">
          <center>
            <div class="center-y button btn btn-default">
              <span class="fa fa-plus fa-2x"></span>
            </div>
          </center>
        </div>
    </div>
    <!-- End Edit -->
    </div>
  </body>
</html>
'''

# A single movie entry html template, rewriten to fit theme and additional data
movie_tile_content = '''
<div class="col-md-6 col-lg-4 text-center">
  <div class="panel panel-primary movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-rating="{movie_rating}" data-description="{movie_description}" data-producer="{movie_producer}" data-toggle="modal" data-target="#trailer">
    <div class="panel-heading">
      <h3 class="panel-title">{movie_title}</h3>
    </div>
    <div class="panel-body">
      <img src="{poster_image_url}" width="220" height="342">
    </div>
  </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_rating=movie.rating,
            movie_producer=movie.producer,
            movie_description=movie.storyline
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()
  
  #Open in browser removed, handled in index.cgi and launch.py

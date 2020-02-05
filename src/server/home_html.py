home_page_html = """
<!DOCTYPE html>
    <head>
        <meta charset="utf-8"/>
        <title>
          Homepage
        </title>
        <script>
            function requestShortUrl() {
                var longUrl = document.getElementById('txtJob').value;
                console.log(longUrl)
                var xmlHttp = new XMLHttpRequest();
                xmlHttp.open( "POST", "http://localhost:8080/new", false ); // false for synchronous request
                xmlHttp.send( longUrl );
                document.getElementById("response").innerHTML =  "Short URL is: <u> http://localhost:8080/" + xmlHttp.responseText + "</u>";
            }
        </script>
        <style>
          #submit {
              background-color: lightblue;
              text-align: center;
              color: black;
              width: 10%;
              height: 50px;
              font-size: 20px;
              margin: 8px 8px;
              border: 3px solid black;
          }
          #submit:hover {
              background-color: lightgreen;
	      font-size: 20px;
          }
          #submit:active {
                  background-color: green;
              font-size: 15px;
              }
          #response {
              color: black;
              width: 100%;
              height: 50px;
              font-size: 20px;
              margin: 8px 8px;
              border-radius: 4px;
          }
          #txtJob {
              width: 80%;
              height: 50px;
              padding: 12px 20px;
              margin: 8px 8px;
              display: inline-block;
              border: 3px solid black;
              box-sizing: border-box;
              font-size: 90%;
          }
          #prompt {
              margin: 8px 8px;
              color: black;
          }
        </style>
        </head>

        <body>
            <h1 id="prompt"><u>Please enter big url:</u> </h1>
            <br>
            <input type="text" name="txtJob" id="txtJob" size="50">
            <button id="submit" onclick="requestShortUrl()">Submit</button>
            <br>
            <p id="response"></p>
        </body>
</html>
"""

short_url_redirect_html = """
<!DOCTYPE html>
  <head>
    <meta http-equiv = "refresh" content = "0; url = {{url}}" />
  </head>
  <body>
    Redirecting to website< ...
  </body>
</html>
"""

not_found_html = """
<html>
  <head>
    <title>
      URL not found.
    </title>
  </head>
  <body bgcolor="lightblue">
    <h1 style="text-align:center;font-size:200px;">404</h>
    <h1 style="text-align:center;">The URL you requested is not in our database.</h>
  </body>
</html>
"""
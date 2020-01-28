home_page_html = """
<html>
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
                document.getElementById("response").innerHTML =  "Short URL is: http://localhost:8080/" + xmlHttp.responseText;;
            }
        </script>
    </head>

    <body background="gray">
        <p1 id="prompt">
            Please enter big url: 
            <input type="text" name="txtJob" id="txtJob" size="50">
            <button id="submit" onclick="requestShortUrl()">Submit</button>
        </p1>
        <br>
        <p1 id="response"></p1>
        <div>

        </div>
    </body>
</html>
"""

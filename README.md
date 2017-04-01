# the-comics
HTML page that lists the characters from a Marvel-story


`docker build --no-cache -t the-comics:latest .`

`run -d -e MARVEL_PUBLIC_KEY=$MARVEL_PUBLIC_KEY -e MARVEL_PRIVATE_KEY=$MARVEL_PRIVATE_KEY -p 5000:5000 the-comics`

http://127.0.0.1:5000
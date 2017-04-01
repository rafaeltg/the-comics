# The Comics Test

Your task is to generate an HTML page that lists the characters from a
Marvel-story.

Using the Marvel API [http://developer.marvel.com/docs], pick a random story
featuring your favourite character (perhaps The Hulk?). Generate an HTML page
with the following characteristics:

* The story's description
* A list of names and pictures of the characters that features in the story
* The Marvel attribution text

We are not too fuzzy about the layout or design of the generated HTML
page, but the HTML itself should be well-formatted.


## Installing and running the server

Before running the server you need to get Marvel's API Public and Private keys. Once you get them, 
please set `MARVEL_PUBLIC_KEY` and `MARVEL_PRIVATE_KEY` environment variables:

```bash
export MARVEL_PUBLIC_KEY=<YOUR_MARVEL_PUBLIC_KEY>
export MARVEL_PRIVATE_KEY=<YOUR_MARVEL_PRIVATE_KEY>
```

### Running using Docker:
* Requirements
    * Docker

* Run the following commands on the project root folder:

    1) Build the Docker image: `docker build --no-cache -t the-comics:latest .`

    2) Run the Docker container: `docker run -d -e MARVEL_PUBLIC_KEY=$MARVEL_PUBLIC_KEY -e MARVEL_PRIVATE_KEY=$MARVEL_PRIVATE_KEY -p 5000:5000 the-comics`


### Running without Docker:
* Requirements:
    * Python (developed and tested with version 2.7)

* Run the following commands on the project root folder:

    1) Install the required packages: `pip install -r requirements.txt`

    2) Run the server: `./run.py`


## Let's have fun
1) Go to your browser and open the url `http://127.0.0.1:5000` (by default it will display some random Deadpool's comic)

2) You can query a random comic from any Marvel's character. For example, to open a random Hulk's comic, use the url: 
`http://127.0.0.1:5000/Hulk`
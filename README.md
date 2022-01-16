<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">URL-Shortener</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## URL-Shortener
URL shorteners take a long, awkward link and turn it into a shorter, easier to share one. 
For example, you can take something like: https://www.google.com/search?q=url+shortener&rlz=1C1CHBF_enIN979IN979&oq=url+shortener&aqs=chrome..69i57j35i39j0i512l4j69i60l2.2995j0j7&sourceid=chrome&ie=UTF-8 and turn it into https://rb.gy/wzkhor.

In this way, you can include a memorable, typable link on a business card, print ad, podcast interview, or any other occasion where someone cannot click a hyperlink.


### Built With
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started
To use URL-Shortner run either commands
  ```sh
  python app.py
  ```
  OR
  ```sh
  flask run
  ```

### Prerequisites
To install python packages use below command:
  ```sh
  pip install flask 
  ```

### Run as docker image
* To run as docker image:
  ```sh
  docker run --name test-flask -p 5001:5001 priyankakhairnar/local_python_1:url-shortener
  ```

* To test APP visit below URL:
  ```sh
  http://127.0.0.1:5001/shortener
  ```
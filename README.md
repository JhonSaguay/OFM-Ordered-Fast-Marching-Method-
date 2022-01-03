
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Ordered Fast Marching Method (OFM)</h3>

  <p align="center">
    Modification of Fast Marching Method, OFM is a new varian of FMM that use an proposed sort method for ordering the narrow band.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About OFM</a>
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

There are many variants of FMM that try to optimize the computational time, applying differents changes on the FMM algorithm. However, these variants are not efficient in all scenarios.

Here's why:
* OFM is a new proposed variant of FMM. Unlike other variants of FMM, OFM does not replace the narrow band with stacks. Furthermore, OFM uses a new ordering method that we call SEF to order the narrow band in each iteration.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section contains the libraries and python version used to build this project.

* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
### Ubuntu
* python 3.6
  ```sh
  sudo apt install python3.6
  ```
* pip
    ```sh
  sudo apt-get -y install python3-pip
  ```
* numpy
    ```sh
  pip3 install numpy
  ```
  ```sh
  pip install numpy
  ```
* matplotlib
    ```sh
  pip install matplotlib
  ```
  ```sh
  pip3 install matplotlib
  ```
* opencv
    ```sh
  pip3 install opencv-contrib-python
  ```


### Windows 
* Download and install python 3.6 from oficial page.
  ```sh
  https://www.python.org/downloads/release/python-368/
  ```
* numpy
    ```sh
  pip3 install numpy
  ```
  ```sh
  pip install numpy
  ```
* matplotlib
    ```sh
  pip install matplotlib
  ```
  ```sh
  pip3 install matplotlib
  ```
* opencv
    ```sh
  pip install opencv-contrib-python
  ```
    ```sh
  pip3 install matplotlib
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
For running this project you need extract all files on a folder, and running the next code line.

* FMM
    ```sh
  python3 fastmarchingserachminimal.py
  ```
* FMM using fibonnaci heap
```sh
  python3 fastmarchingfibonnaciheap.py
  ```
* FMM using binary heap
```sh
  python3 fastmarchingbinaryheap.py
  ```
* OFM
```sh
  python3 OFM.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Examples and results -->
## Results
Example using a maze image.

![alt text](https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-/blob/main/laberinto3.jpg?raw=true)

![alt text](https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-/blob/main/route6_laberinto2.png?raw=true)


Example using a real map of San Diego city.

![alt text](https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-/blob/main/mapasandiego.jpg?raw=true)

![alt text](https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-/blob/main/maparoute.png?raw=true)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jhonatan Saguay - Personal email - jhonsaguay@gmail.com

Jhonatan Saguay - University email - jhonatan.saguay@yachaytech.edu.ec

Project Link: [https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-](https://github.com/JhonSaguay/OFM-Ordered-Fast-Marching-Method-)

<p align="right">(<a href="#top">back to top</a>)</p>



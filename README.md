# Ex.05 Design a Website for Server Side Processing
## Date:16/12/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
{% load static %}
<html>
<head>
    <title>math</title>
    <style>
h1{
    border:2px solid cornflowerblue;
    padding:20px;
    margin:10px;
    border-radius: 10px;
    position: fixed;
    top: 200px;
    right:835px;
    font-size:x-large;
    font-weight: bolder;
    font-variant:small-caps;
    background-color:burlywood;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color:brown;
}
form{
     border:3px slategrey;
     background-color:aqua;
     padding:30px;
     margin:10px;
     border-radius: 10px;
     width:400px;
     position:fixed;
     top:300px;
     left:750px;
 }
        </style>
</head>
 <body>
    <h1 align="center">POWER OF A LAMP FILAMENT</h1>
    <form align="center" method="POST">
     {%csrf_token%}
            <div class="power">
                <label><b>INTENSITY:</b></label>
                <input type="text" name="intensity" value="{{i}}">
                </div>
                <div class="power"></div>
                <label><b>RESISTANCE:</b></label>
                <input type="text" name="resistance" value="{{r}}">
            </div>
            <br>
            <input type="submit" value="COMPUTE">
            <div class="power">
                <label><b>POWER:</b></label>
                   <input type="text" name="POWER" value="{{power}}">
            </div>
</form>
</body>
</html>
```


## SERVER SIDE PROCESSING:

![alt text](<Screenshot (9).png>)
## HOMEPAGE:
![alt text](<Screenshot (8).png>)

## RESULT:
The program for performing server side processing is completed successfully.

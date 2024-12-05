# Ex.05 Design a Website for Server Side Processing
## Date:05.12.2024

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
math.html

<!DOCTYPE html>
 <html>
 <head>
 <meta charset='utf-8'>
 <meta http-equiv='X-UA-Compatible' content='IE=edge'>
 <title>Power of a lamp filament</title>
 <meta name='viewport' content='width=device-width, initial-scale=1'>
 <style type="text/css">
 body {
    background-color: rgb(164, 238, 204);
 }
 .edge {
    width: 100%;
    padding-top: 250px;
    text-align: center;
 }
 .box {
    display: inline-block;
    border: thick dashed rgb(0, 0, 0);
    width: 500px;
    min-height: 300px;
    font-size: 20px;
    background-color: rgb(246, 175, 221);
 }
 .formelt {
    color: black;
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
 }
 h1 {
    color: black;
    padding-top: 20px;
 }
 </style>
 </head>
 <body>
 <div class="edge">
    <div class="box">
        <h1>Surfacearea of Right Cylinder</h1>
        <h3>Janani S</h3>
        <form method="POST">
            <div class="formelt">
                Intensity: <input type="text" name="Intensity" value="{{r}}">m<br/
            </div>
            <div class="formelt">
                Resistance: <input type="text" name="Resistance" value="{{h}}">m<br/
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate"><br/>
            </div>
            <div class="formelt">
                power: <input type="text" name="Power" value="{{area}}">m<sup
            </div>
        </form>
    </div>
 </div>
 </body>
 </html

views.py

from django.shortcuts import render
def power(request):
    context = {}
    context['power'] = "0"
    context['i'] = "0"
    context['r'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)
        i = request.POST.get('intensity', '0') 
        r = request.POST.get('resistance', '0') 
        print('intensity =', i)
        print('resistance =', r)
        power =  int(i) * int(i) * int(r)
        context['power'] = power
        context['i'] = i
        context['r'] = r
        print('Power =', power)
    
    return render(request, 'mathapp/math.html',context)


urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('power/',views.power,name="power"),
    path('',views.power,name="power")
]
```

## SERVER SIDE PROCESSING:
![image](https://github.com/user-attachments/assets/c50ac808-e281-410f-9383-a8af10ede909)


## HOMEPAGE:
![Screenshot 2024-12-05 161815](https://github.com/user-attachments/assets/fc244e14-ffdd-4249-b3cb-3691998fc4e9)

## RESULT:
The program for performing server side processing is completed successfully.

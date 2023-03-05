# AfricaHackon MasterClass 2023
## Sonic Go Brrr (CyberTalents!)
### @Author : M3tr1c_r00t
![image](https://user-images.githubusercontent.com/99975622/222982585-bb1bec1f-823c-4d7b-acd9-0359c49c213a.png)
### Challenge Description...
![image](https://user-images.githubusercontent.com/99975622/222986489-8b6d3321-9b9c-491c-8068-baf5ee334190.png)

### Enumeration...
#### Gobusterscan...
```
/.hta                [33m (Status: 403)[0m [Size: 330]
/.git/HEAD           [32m (Status: 200)[0m [Size: 23]
/.htaccess           [33m (Status: 403)[0m [Size: 330]
/.htpasswd           [33m (Status: 403)[0m [Size: 330]
/index.php           [32m (Status: 200)[0m [Size: 812]
/index.html          [32m (Status: 200)[0m [Size: 10701]
/robots.txt          [32m (Status: 200)[0m [Size: 41]
/server-status       [33m (Status: 403)[0m [Size: 330]
```
After doing the gobusterscan, we can visit the robots.txt file.
![Screenshot_2023-03-04_13_07_10](https://user-images.githubusercontent.com/99975622/222985063-6a84ee23-7442-4f13-b0b8-94f8095daf2a.png)
We get a clue to take a look at the .git repo.

So, I install git-dumper and we can take a look at the logs.
![Screenshot_2023-03-04_12_55_48](https://user-images.githubusercontent.com/99975622/222985161-64329c13-c700-48bf-b987-11d2d2bf2013.png)
If we check the logs, we find  2 present. 

![Screenshot_2023-03-04_12_59_43](https://user-images.githubusercontent.com/99975622/222985220-070c7952-f190-448c-bfee-22cb95b7576d.png)
The first being the default startup one and the second containing the source code of the index.php file.
![Screenshot_2023-03-04_13_00_14](https://user-images.githubusercontent.com/99975622/222985292-728736e1-193e-4b66-9372-d296253f11f3.png)
```
+<!DOCTYPE html>
+<html lang="en" >
+<head>
+  <meta charset="UTF-8">
+  <title>CodePen - CSS+SVG Motion Blur Text Effect</title>
+  <link rel="stylesheet" href="./style.css">
+
+</head>
+<body>
+<!-- partial:index.partial.html -->
+<svg xmlns="http://www.w3.org/2000/svg">
+
+  <!-- filterUnits is required to prevent clipping the blur outside the viewBox -->
+
+    <filter id="motion-blur-filter" filterUnits="userSpaceOnUse">
+
+      <!-- We only want horizontal blurring. x: 100, y: 0 -->
+
+        <feGaussianBlur stdDeviation="100 0"></feGaussianBlur>
+    </filter>
+</svg>
+
+
+<?php
+Session_start();
+
+
+
+
+function mstime(){
+
+  return round(microtime(true) * 1000);
+}
+
+function generateRandomString($length = 10) {
+    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
+    $charactersLength = strlen($characters);
+    $randomString = '';
+    for ($i = 0; $i < $length; $i++) {
+        $randomString .= $characters[rand(0, $charactersLength - 1)];
+    }
+    return $randomString;
+}
+
+
+
+if(!isset($_SESSION['flooog']) and !isset($_COOKIE['secret'])) {
+    $flog=generateRandomString();
+    $_SESSION['flooog'] = $flog;
+    $_SESSION['counter'] = mstime();
+    setcookie("secret",base64_encode($flog));
+
+
+
+}
+
+
+
+
+
+if (isset($_POST['Q'])) {
+  if ($_POST['Q']== $_SESSION['flooog']) {
+
+    if (  (mstime() - $_SESSION['counter']) < 2999  ){
+
+    echo '<span filter-content="S">You won against sonic!!! GJ Here is a flag for you: flag{f4k3_fl4g}</span>';
+
+    }else{
+
+ echo '<span filter-content="S">cmon.. do you call this speed?</span>';
+
+    }
+
+  }else{
+
+ echo '<span filter-content="S">The encoded secret you provided is wrong :( Sonic is not impressed</span>';
+
+    echo "\n";
+  }
+
+
+
+}else{
+
+ echo "\n";
+ echo '<span filter-content="S">Q parameter is not set!</span>';
+  echo '<span filter-content="S">Challenge suspended</span>';
+
+
+}
+?>
+
+
+
+<!-- partial -->
+  <script src='https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.12/vue.min.js'></script>
+</body>
+</html>
diff --git a/robots.txt b/robots.txt
new file mode 100644
index 0000000..68edb70
--- /dev/null
+++ b/robots.txt
@@ -0,0 +1 @@
+hint: git gud to solve this challenge ;)
diff --git a/style.css b/style.css
new file mode 100644
index 0000000..79e3f7e
--- /dev/null
+++ b/style.css
@@ -0,0 +1,37 @@
+@charset "UTF-8";
+/* We’ll set some colors and center everything. */
+body {
+  background: #4c268f;
+  color: #99eeb4;
+  height: 100vh;
+  text-align: center;
+  display: flex;
+  justify-content: center;
+  align-items: center;
+}
+
+/* We set the position to relative so that we can stack a blurred pseudo element on top of the original text */
+span {
+  position: relative;
+  font-family: "Avenir Next", sans-serif;
+  font-weight: 900;
+  font-size: 64px;
+  text-transform: uppercase;
+  font-style: italic;
+  letter-spacing: 0.05em;
+  display: inline-block;
+}
+
+/* We create a pseudo element and blur it using the SVG filter. We’ll grab the content from the custom HTML attribute. */
+span:before {
+  position: absolute;
+  left: 0;
+  top: 0;
+  content: attr(filter-content);
+  filter: url(#motion-blur-filter);
+}
+
+/* We hide the SVG filter element from the DOM as it would take up some space */
+svg {
+  display: none;
+}
```
### Explanation on what the code is doing...
The PHP code uses the Session_start() function to start a session.

There are two functions defined: mstime() and generateRandomString().

The code checks whether a session variable called 'flooog' and a cookie called 'secret' have been set. If not, it generates a random string, sets the session variable, sets a session counter, and sets the 'secret' cookie with the base64 encoded value of the random string.

If the 'Q' parameter is set in a POST request, the code checks whether it matches the 'flooog' session variable. If it does, it checks if the time elapsed since the session counter was set is less than 2999 milliseconds. If it is, it displays a message with a flag. Otherwise, it displays a message saying the speed was too slow.

If the 'Q' parameter is not set, the code displays a message saying the challenge is suspended.

So in short, the challenge is to grub the encoded key and send it off as a different parameter.

Note that we are going to need to send it off in less that three seconds. That's why the challenge is called sonic*

So, to fix this, i wrote a python script to do this for us.
![Screenshot_2023-03-04_14_03_42](https://user-images.githubusercontent.com/99975622/222985972-bf873f95-e3f7-4686-a43a-dae6fa81f7b3.png)

The Python Script...
```
#!/usr/bin/env python3
#Author : M3tr1c_r00t

import base64
import requests
from urllib.parse import unquote

url = "http://wcamxwl32pue3e6m5l3n94wbq36o4nzy8kr5snzk-web.cybertalentslabs.com/index.php"
s = requests.Session()

get = s.get(url)

cookies = unquote(get.cookies['secret'])

decoded_cookie = base64.b64decode(cookies).decode()

post =  s.post(url,data={'Q': decoded_cookie})

#respost = requests.post(url,data = data)
print(post.text)


```

With that, we get the flag.
![Screenshot_2023-03-04_14_54_05](https://user-images.githubusercontent.com/99975622/222986046-2738bad5-8607-4f1f-83ea-5c33cf060d42.png)
And Done!

## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/

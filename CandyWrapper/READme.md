# AfricaHackon MasterClass 2023
## Candy Wraper(CTFRoom!)
### @Author : M3tr1c_r00t
![image](https://user-images.githubusercontent.com/99975622/222982585-bb1bec1f-823c-4d7b-acd9-0359c49c213a.png)
### Enumeration...
#### Gobusterscan...
```
/.gitignore          [33m (Status: 200)[0m [Size: 277]
/.hta                [33m (Status: 403)[0m [Size: 277]
/.htaccess           [33m (Status: 403)[0m [Size: 277]
/.htpasswd           [33m (Status: 403)[0m [Size: 277]
/index.php           [32m (Status: 200)[0m [Size: 0]
```
![Screenshot_2023-03-04_11_02_31](https://user-images.githubusercontent.com/99975622/222982766-b2a1f048-2c0f-4a87-8002-245e2f099f28.png)
After looking at the about page, its being loaded by php. I tried a bunch of filters but it didnt work.
Since there was a .gitignore file, we can take a look at it.
![Screenshot_2023-03-04_11_27_46](https://user-images.githubusercontent.com/99975622/222982947-2c81f378-7bd6-421d-940a-e58604877b6c.png)
There's one directory and we can do some fuzzing.
We can also try visiting the creds file.
Since it's php, we can't see its contents. I then tried the php filters on this file and got one that worked. The base64 filter.
![Screenshot_2023-03-04_11_56_12](https://user-images.githubusercontent.com/99975622/222983265-2ef772d2-5710-4e4a-94a0-feba0c817678.png)
And we've found some credentials.
![Screenshot_2023-03-04_11_56_47](https://user-images.githubusercontent.com/99975622/222983305-8c53eb8c-1fa0-4b4a-884c-2a87b01aa464.png)

After doing the fuzzing, I found a login page ```admin_area.php```
I entered the creds and got the first flag.
![Screenshot_2023-03-04_12_42_22](https://user-images.githubusercontent.com/99975622/222983401-84665a98-664c-42cd-867a-66b8f8ae653c.png)

### Flag 2
If we check the cookies in the web-server, we find 2.

One for session handling and a ```superadmin``` cookie.
![Screenshot_2023-03-04_12_42_46](https://user-images.githubusercontent.com/99975622/222983570-42ff52ad-967d-48dc-9f07-7c20c4b2c355.png)
The cookie seemed to be base64 so after decoding it, it was set to ```false```

![Screenshot_2023-03-04_12_44_15](https://user-images.githubusercontent.com/99975622/222983620-54ac37e4-235c-4897-b704-770810bfa872.png)

Encoding to ```true``` base64
![Screenshot_2023-03-04_12_45_08](https://user-images.githubusercontent.com/99975622/222983686-c911ee64-e877-4fa0-b132-4e2eb8c28c0b.png)

with that, I set it to true and we get a command execute panel.
![Screenshot_2023-03-04_12_45_37](https://user-images.githubusercontent.com/99975622/222983726-8be890c8-62cc-4d98-a3bf-350a0c1f5231.png)
It seems that we can execute commands in a system so we can read the files on the server internally.
![Screenshot_2023-03-04_12_46_31](https://user-images.githubusercontent.com/99975622/222983798-61dd4982-6a77-4748-9dcf-5d7ea9df431e.png)
Seeing that there is a neymar user and that the web-server is running as him, we can try and check his home files and there we get a flag.
![Screenshot_2023-03-04_12_48_24](https://user-images.githubusercontent.com/99975622/222983842-1f9a8eb0-898e-4ab2-bb8d-8dd6187f348f.png)
We finally get the flag.
![Screenshot_2023-03-04_12_48_45](https://user-images.githubusercontent.com/99975622/222983888-63ae3d11-6a56-4d63-8dc0-8d5c174c2999.png)
And Done!
## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
 

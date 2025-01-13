![Logo](./images/Title_2-removebg-short.svg)
#
_Writeup of challenges solved by me during WannaHack2025 , a annual Capture the Flag competition hosted by IIT(BHU)CyberSec and the COPS Infosec vertical._
### 1. i love chess
**Submission Time** @ Jan 10th 11:40:50 PM  
**Value** : 421 , **Tag** : Forensics , **Note** : First Blood  
  
  ***Solution***  
- The link provided in challenge takes us to the Game analysis between 2 players (Most probably BOTS) . After looking at computer analysis of game I immediatly remembered about [a youtube video](https://www.youtube.com/watch?v=TUtafoC4-7k) which I watched in last September. The above mentioned video explains idea of storing data in form of PGN (Notation used in chess to record a chess match).
- After some google serches i found **[a website](https://incoherency.co.uk/chess-steg/)** which helped to decode data from PGN.
- Flag : WannaHack{ch3ss_1s_4dd1ct1v3}  

### 2. The Turings Challenge
**Submission Time** @ Jan 11th 12:44:13 AM  
**Value** : 50 , **Tag** : Crypto

 ***Solution***  
 - Upon searching some keywords form challenge descriptions together i.e _encryption, machine, rotor and ring position_ some webpages regarding **Enigma Cipher Machine**  are suggested.
- I found this [Cryptii Enigma Machine decoder](https://cryptii.com/pipes/enigma-machine) online , by usings hints in paragraph we can counclude that:
  - Model : Enigma M3 (German army and navy)
  - Reflector : UKW C
  - Rotor : 6 , 2 ,3
  - Position :  5(E) , 1(A) , 8(H)
  - Ring : 2(B) , 1(A) , 4(D)
- After clearing the letters in plugboard and including foreign characters we can decode the given flag. Make sure capitalize letters which are in capital form in orignal string.
- Flag : WannaHack{EniGMa_maCHiNe_sAys_heIL_HItLeR}

### 3. Kimi No Sekai: Part 1
**Submission Time** @ Jan 11th 1:14:41 AM  
**Value** : 50 , **Tag** : OSINT

 ***Solution***  
 - A simple Google Lens search will tell that the landmark in above mentioned challenge is of **Suga Shrine** in Shinjuku , Japan.
 - Using Google Lens Street View we can exactly pin point location of above image.
 - Flag : WannaHack{35.685285_139.72247}

### 4. Kimi No Sekai: Part 3
**Submission Time** @ Jan 11th 1:24:39 AM  
**Value** : 50 , **Tag** : OSINT

 ***Solution***  
 - A simple Google Lens search will tell that the landmark in above mentioned challenge is near **Docomo Tower** in Tokyo , Japan.
 - Using Google Lens Street View we can exactly pin point location of above image.
 - Flag : WannaHack{35.684670_139.704079}

### 5. Kimi No Sekai: Part 2
**Submission Time** @ Jan 11th 1:29:56 AM  
**Value** : 50 , **Tag** : OSINT

 ***Solution***  
 - A simple Google Lens search will tell that the landmark in above mentioned challenge is near **The National Art Center** in Tokyo , Japan.
 - Using Google Lens Street View we can exactly pin point location of above image.
 - Flag : WannaHack{35.664484_139.726985}

### 6. Secret Chat  
**Sunmission Time** @ Jan 11th 2:26:32 PM  
**Value** : 50 , **Tag** : Forensics 

 ***Solution***
 - The file with challenge ends with extention .pcap . These files contain packet data of a network and are used to analyze the network characteristics.
 - To open and analyze such file a packet analyzer like **WireShark** is used.
 - After opening the file in **WireShrak** and looking for various things in the application I found out that after searching word ***DATA*** in search box there were **9 packets** which had data hidden in them.
 - After carefully examining them we get a **BASE 64** encoded string.
 - Note : **7w** isn't part of string as when you hover your mouse over the string **WireShark** doesn't highlight it.
 - Decoding the **Base 64** string an online decoder gives us our desired flag.
 - Flag : WannaHack{TCP_ENC0DED_CH4T}

### 7. RickRoll Resonance  
**Submission Time** @ Jan 11th 3:17:06 PM  
**Value** : 50 , **Tag** : Forensics  

***Solution***  
- The challenge provides a audio file which was unlike any other previous audio based CTF's I solved.
- Googling about various methods to hid secret message in audio led me to search more about **Audio Steganography**.
- I downloaded **Sonic Visualiser** to analysis the audio.
- After watching some tutorial about using Sonic Visualiser in audio steganography, I found out about **Add Spectrogram** under **Layers** tab.
- Now the flag was visible on screen but a bit blur , so by changing some properties of spectrogram by trial and error we can clearly see the flag.
- Flag : WannaHack{y34H_17_w45_345y_1G}

### 8. Know your Crows Vultures & Eagles 1  
**Submission Time** @ Jan 11th 3:26:58 PM  
**Value** : 50 , **Tag** : OSINT  

***Solution***  
- I used ChatGPT AI to know about vulnerability in Apache Tomcat's CGI Servlet and got to know that option is enableCmdLineArguments and OS is Windows
- Flag : WannaHack{enableCmdLineArguments-Windows}

### 9. Know Your Malware  
**Submission Time** @ Jan 11th 3:28:11 PM  
**Value** : 50 , **Tag** : OSNIT  

***Solution***  
- This one is preety stright forward and require no thinking , even if you don't know A-B-C you can ofcourse Google it.
- A is a Torjan , B is a Virus and C is Ransomware.
- Flag : WannaHack{Trojan-Virus-Ransomware}

### 10. Knowyour Crows Vultures & Eagles 2  
***Submission Time*** @ Jan 11th 3:33:54 PM  
**Value** : 50 , **Tag** : OSNIT  

***Solution***  
-  One takeaway from this problem for me was : Don't trust ChatGPT blindly (It responed with a wrong version) :disappointed:
-  Searching about Apache HTTP Server mod_auth_digest Control Bypass Vulnerability led me to [this website.](https://pentest-tools.com/vulnerabilities-exploits/apache-http-server-2439-mod-auth-digest-access-control-bypass-vulnerability-windows_4483)
-  The version in which above mentioned issue was fixed is 2.4.39
-  Flag : WannaHack{2.4.39}

### 11. Least Significant Clue  
**Submission Time** @ Jan 11th 4:00:30 PM  
**Value** : 50 , **Tag** : Forensics  

***Solution***  
-  As the title of challenge is **Least Significant Clue** and we can see word **LSB** in image, it was crystal clear this challenge had somthing to do with word least significant.
-   After some Google Searches I found that B stands for **Bit** , also I read a [cft101 article](https://ctf101.org/forensics/what-is-stegonagraphy/) which helped me understand LSB Steganography.
-   Then I watched a [Youtube Tutorial](https://www.youtube.com/watch?v=OPRGfJJ8bmU) on solving LSB CTF's
- Running these Command in Linux/WSL/Ubantu will give flag :
  ```
  $ gem install zsteg
  $ zsteg -a chall.png
  ```
- Flag : WannaHack{l3457_significant_3u7_1mp0r74n7}

  ### 12. Rules
  **Submission Time** @ Jan 11th 7:54:58 PM
  **Value** : 50 , **Tag** : Web

  ***Solution***
  - The most obvious thing to do was submit flag as WannaHack{flag_string} as solution but this is just a red herring.
  - Upon opening **Inspect Tab** under **Elements** menu we can see the **HTML** used for website.
  - The flag is part of **comment** inside the pages HTML content.
  - Flag : WannaHack{4lw4ys_r34d_7h3_ru135}

  ### 13. Sanity 2
  **Submission Time** @ Jan 11th 11:00:13 PM
  **Value** : 136 , **Tag** : Misc

  ***Solution***
  - I stumbled upon solution of **Sanity 2** accidently while looking at Discord for solution  of **Sanity**.
  - After looking at evey channel and chat in hopes of finding solution of **Sanity** , in despartely I just searched word **WannaHack** on search bar.
  - This obviously showed me all chats with word **Wanna Hack** in it but also showed me meme of rickroll sent by **[kn1gh7](https://tenor.com/view/rick-roll-gif-25917805)**.
  - I didn't understood then how was that flag hidden in the image but now after learning to write in **markdown** , I understand it now.
  - Flag : WannaHack{d15c0rd_15_4_5c4ry_b3457_6969}

  ### 14. Sanity
  **Submission Time** @ Jan 11th 11:21:07 PM
  **Value** : 50 , **Tag** : Misc

  ***Solution***
  - The Sanity Txt file was a massive red herring for this challenge and quite waste of time for me too.
  - I was bit biased towards thought that flag must be hidden in chat or in admin profile ( Like CicadaIITBHU) that I just didn't noticed sub-heading of **#rules** for quite a lot of time.
  - Flag : WannaHack{y0u_4r3_54n3_6969}

  ### 15. Easy Cat
  **Submission Time** @ Jan 12th 1:13:56 AM
  **Value** : 50 , **Tag** : PWN

  ***Solution***
  - This one is also preaty stright forward
  - Just click on Initiate Suffering and put the given commmand in WSL/Linux/Ubantu Command prompt.
  -  Flag : WannaHack{345y_netcat_fVcHlP9D}

  ### 16. Cheap Amazon
  **Submisiion Time** @ Jan 12th 1:32:53 AM
  **Value** : 50 , **Tag** : PWN

  ***Solution***
  - Challenge 

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
**Submission Time** @Jan 11th 3:26:58 PM  
**Value** : 50 , **Tag** : OSINT  

***Solution***  
- I used ChatGPT AI to know about vulnerability in Apache Tomcat's CGI Servlet and got to know that option is enableCmdLineArguments and OS is Windows
- Flag : WannaHack{enableCmdLineArguments-Windows}

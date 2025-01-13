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
- I was bit biased towards thought that flag must be hidden in chat or in admin profile (Like CicadaIITBHU) that I just didn't noticed sub-heading of **#rules** for quite a lot of time.
- Flag : WannaHack{y0u_4r3_54n3_6969}

### 15. Easy Cat
**Submission Time** @ Jan 12th 1:13:56 AM
**Value** : 50 , **Tag** : PWN

***Solution***
- This one is also preaty stright forward
- Just click on Initiate Suffering and put the given commmand in WSL/Linux/Ubantu terminal.
-  Flag : WannaHack{345y_netcat_fVcHlP9D}

### 16. Cheap Amazon
**Submisiion Time** @ Jan 12th 1:32:53 AM
**Value** : 50 , **Tag** : PWN

***Solution***
- Challenge had a C file and a NetCat link in it. Upon running nc command in terminal I realised that the provided chall.c file is code used in NetCat link.
- Our goal is to find vulnerability in C code to make our balance enough to buy flag.
- We can exploit it with integer underflow.
- Following is one exmple of inputs to cause underflow and buy flag :
  ```
    Option : 1
    Enter amount of money to withdraw : -20000000000
    Option : 2
    Enter amount of money to withdraw : -20000000000
    Option: 3
  ```
- Flag : WannaHack{w3lc0m3_70_pwn1ng_VGtoEJct}

### 17. Cheap Amazon Revange
**Submission Time** @ Jan 12th 1:44:59 AM
**Value** : 50 , **Tag** : PWN

***Solution***
- The key idea of this question is same as **Cheap Amazon**
- This time though we cant input < 0 but other key vulnerability added in program is from the line :
  ```
  input = input * 100
  ```
- As this time we can input a large number which will not overflow to negetive number but after cheaking input < 0 condition it will execute input = input * 100 causing it to overflow after cheak.
- If we deposited a negetive sum money it will increase our money instead of decreasing.
  ```
  Option :  2
  Enter number of Rs.100 gift cards to deposit: 2000000000
  Option : 3
  ```
- Flag : WannaHack{1n73g3r_0v3rfl0w_CSO101_agFc5Mf1}

### 18. Basics
**Submission Time** @ Jan 12th 3:21::18 AM  
**Value** : 379 , **Tag** : PPC  

***Solution***  
- The challenge desription talks about pwntools , as some one who didn't used pwn ever I spent quite sometime learning about PWN through Youtube and Google and read some solutions about PWN CTF's to understand its implemention in CTF.
- As I already know decent about Python , Coding wasn't a huge issue.
- Basiclly we open connection with wannahack.iitbhucybersec on a port and then recive and send data using Python Code.
  ```
  from pwn import *
  import requests

  io = remote('wannahack.iitbhucybersec.in', 28632)
  io.recvuntil('I GIVE:')
  for _ in range(250):
    line = io.recvline().decode().strip()
    if 'I GIVE:' in line:
        i = int(line.strip('I GIVE:').strip())
        io.sendline(str(i**2))
    elif 'You Give:' not in line:
        print(line)
  ```
- Flag : WannaHack{pwntools_m4g1c_duBuTWnd}

### 19. impossible  
**Submission Time** @ Jan 12th 4:43:05 AM  
**Value** : 120 , **Tag** : Misc  

***Solution***  
- We have to enter string whoes length is less than 20 but still after using upper method on string then length needs to be 25 , sounds impossible right?
- Well NO, There are special unicode character that expand in length when transformed by .upper(). For example The German Eszett (ß) becomes SS when converted to
uppercase.
- Hence a string like ßßßßßßßßßßßßS would satify all the conditions.
- Flag : WannaHack{m0r3_l1k3_1_4m_p0551bl3_0aHYUg10}

### 20. Guess  
**Submission Time** : Jan 12th 10:35:23 AM  
**Value** : 405 , **Tag** : PPC  

***Solution**  
- Challenge ask us to guess a random number between 1 to 100000000 with in 30 attempts and gives us hint *Higher* or *Lower* after every attempt.
- **Binary Search** is our only way to Guess the number within 30 attempts.
- I wrote the following Binary Search Code to get the right guess.
  ```
  from pwn import *
  io = remote('wannahack.iitbhucybersec.in', 35867)
  io.recvuntil('[1] YOUR GUESS: ')

  low = 0
  high = 100000000
  for _ in range(100):
      mid = (low + high) // 2
      io.sendline(str(mid))
      res = io.recvline().decode().strip()
      if 'HIGHER' in res:
          low = mid
      elif 'LOWER' in res:
          high = mid
      else:
          print(res)
  ```
- Flag : WannaHack{m3n_gu335_suks_5tjZX6A8}  

### 21. Easy Sudoko  
**Submission Time** @ Jan 12th 12:08:37 PM  
**Value** : 405 , **Tag** : PPC  

***Solution***  
- Just like previours problem this one too don't require exctrating a data from file or find hidden information , All we have to do is program to solve sudoku and recive and send requests via PWN tools.
- I used a sudoko solver program from GreekForGreeks and modified it so that it not just solve sudoku from input list but also fetch input data from *nc wannahack.iitbhucybersec.in*.
- Here is my code :
  ```
  from pwn import *
  io = remote('wannahack.iitbhucybersec.in', 63817)

  def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1
  def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

  def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        grid[i][j] = 0
        return False
  for _ in range(10):
        grid=[]
        io.recvuntil('>>')
        line = io.recvline().strip()
        for i in range(9):
            line =io.recvline().strip().decode()
            line = line.replace('_', '0')
            numbers = list(map(int, line.split()))
            grid.append(numbers)
        a = solveSudoku(grid)
        io.recvuntil('>>')
        for i in range(9):
            io.sendline(' '.join(map(str, grid[i])))
        if _ == 9:
                for i in range(9):
                        print(io.recvline().decode())
  ```
- Flag : WannaHack{Very_3Ay_sud0KU_indE3D_wZ4EYay4}

### 22. The Social Network 
**Submisssion Time** @ Jan 12th 7:21:39 PM  
**Value** : 405 , **Tag** : Web  

***Solution***  
- This problem was stright forward but a lot of time consuming and harder code compared to previous one.
- The problem required to gather data from 5 Hostel from a website and present it in a JSON file.
- Due to complex nature of code of problem I am attaching [link to the code](https://github.com/RudranilJadhav/WannaHack-CTFWriteup/tree/main/The%20Social%20Network) instead of writing it here.
- I must admit that I heavly used ChatGTP's in solving this challenge as I was clueless against InfiniteScroll and had no prior exprenience in creating an automated chrome Bot to scroll to infinty and beyond.😉
- Note : You need to constantly click on 'Prolong Suffering' as this will avoid TimeOut and make sure get all hostel data on similar Port number as names are randomly genrated with each diffrent port.
- Flag : WannaHack{}

### 23. Safest Bank In The World  
**Submission Time** @ Jan 12th 7:36:42 PM  
**Value** : 405 , **Tag** : Web  

***Solution***  
- Since I couldn't find any thing vulnerable in login and signup source pages in Inspect menu , I decided to create a account and sign up for the bank .
- After sign up and login , first thing you see is **New Transfer** , by sending some money to either of 2 accounts mentioned in challenge. We get to a transaction details window.
- The bank gives this transaction as id = 13 , this means there were 12 transactions before this.
- By cheaking for each transaction id we can find our desired transaction at id = 12
- The note contains flag.
- Flag : WannaHack{1n53cur3_d1r3ct_0bj3ct_r3f3r3nc3_Bgy8k0oO}

### 24. Text First Search  
**Submission** @ Jan 12th 10:28:57 PM  
**Value** : 280 , **Tag** : OSNIT  

***Solution***  
- By using the exiftool it becomes clear that the file provided in challenge is a txt file.
- Google searching first few sub-string of the txt file i.e */9j/4AAQSkZJRgABAQAAAQABAAD* I got to know that this text file is JPEG file converted in BASE 64 .
- By online tool such as [Base64 Guru](https://base64.guru/converter/decode/image/jpg) we can decode the text to jpeg.
- Just a normal Google Lens search showed me same wall that which was present in image but nothing usefull to solve problem.
- Searching Image with IIT(BHU) tag led me to linkedin profile of person in image **Naman Tandel**. By using information on his linkedin page I got to know he is my senior of batch 2023.
- By usingg the list of Hostel allotment of freshers of 2023, I found out his roll number.
- Flag :  WannaHack{231022097}

### The End

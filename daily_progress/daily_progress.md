
# This is a personal progress metric.

### Day 0:
- Checked out **Nmap**. Some of the commands. Started with black hat python book.

### Day 1:
- Started playing around with **vim**. Been using atom but vim seems like a better choice for scripting on servers etc. There is a learning curve. New things I found out and liked:
  - /\c{word} _for case sensitive search_
  - :w | !pyton file.py _to save file and run it without closing it_
  - dd _to delete lines_
  - _v_ to select a word and then _shift_ _v_ _Makes word upper case_
  - open multiple files and then moving around with :prev, :n
  - _<_ to indent blocks
  - Copying lines and pasting
  - Using vim is forcing me to spend more time on terminal, making me more comfortable with common terminal commands

-  [Networks - python tcp,udp,server script](https://github.com/Bazarovay/cybersecurity-warplan/black_hat_python/network_basic)


### Day 2:
- Tower of Hanoi and other recursion problems

### Day 3: _12/10/17_
- Cryptography _Add more detail, and move outside Daily Plan_
   - Basic principles,One Time Pad, Double Transposition etc
   - Symmetric Key Algorithm
      - Block Ciphers
         - [DES](https://www.youtube.com/watch?v=G_guTnTcoqg)
         - [AES](https://www.youtube.com/watch?v=ZhILF5Dhx74)
      - Stream Ciphers
         - [A5/1](https://www.youtube.com/watch?v=1GoP_HfF_v4)
         - [RC4](https://www.youtube.com/watch?v=riIp6EQOJOg)
- Resources:
   [Mark Stamp information security principles and Practice chapter 3](https://www.amazon.com/Information-Security-Principles-Mark-Stamp/dp/0470626399)

### Day 4: _13/10/17_
- Linux User Accounts
- less /etc/passwd
first name, encrypted passwrd, id (-999 for sys, 1000+ for user),
group id (/etc/group), comment field info abt user, user home directory (default in home
  In etc/default/useradd. useradd -D, default login shell)

- cat /etc/shells
- sudo less /etc/shadow
- file only root can read
- 9 cols

- Set up CentOS https://geekflare.com/no-internet-connection-from-vmware-with-centos-7/
- Created users


### Day 5: _17/10/17_
- Between Day4 and Day5: Covered RSA, Asymmetric Crypto, Onion Routing, ARP & Routing
Today I plan on looking into:
- Virtual Labs tutorials
- Data structures, O(n) etc from jwasham's repo
- Metasploitable-2 Walkthru
- Go over VLAN and Trunking

- Virtual Lab
- [x] Eli The Computer Guy
 - NAT, Bridge, Internal
 - Keep dynamic size
 - Host to guest option
 - clone OS if experimenting so dont have to install again if messed up
 - boot from ISO (like CD) if need to do registry level stuff etc
 - Different networks card, can use open source routers like pfsense
 - Guest read from host, host shouldnt read from guest, guest cant write to host

- [x] (Building A Pentesting Lab - David Boyd)[https://www.youtube.com/watch?v=b8_sOoQtALs]
- Very Helpful
 Pen Testing Platforms:
 - Kali Linux
 - Pentoo
 - Backbox
 - Samurai WTF(Web App Testing)
 - Samurai STFU(Utility Hacking)
 - Deft Linux(Forensics)
 - People build their own distros as well

 Vulnerable VMs:
 Metasploitable-2
 Morning Catch (Phishing)
 OWASP BrokenWebApplications
 WebGoat (Web Applications)
 vulnhub.com
 Kioptrix (for beginners)
 PwnOS

 Guides:
 Metaspolaitable 2 Exploitability Guide
 Introducing Morning Catch
 Sans Mutilliadae Whitepaper

 Vulnerable VMs
 - Windows XP, Windows Server, Microsoft Exchange, Windows 7

 Tools:
 Nmap/Masscan
 Nessus (Vulnerability Scanning)
 Cain (ARP poisoning)
 Responder (MiTM)
John The Ripper (Hash Cashing)
Metasploit (Exploits)
SET/GoPhish/SPF
Discover Scripts (OSINT)
PowerShellEmpire (Powershell scripts)
CrackMapExec (PostExploitation)

Build A Domain,
Add Users With Various Privileges
Hacker Playbook: http://thehackerplaybook.com/Windows_Domain.htm

For additional training:
- (Metasploit Unleashed)[https://www.offensive-security.com/metasploit-unleashed/]
- www.hackthissite.com
- DerbyCon, DefCon, BSides, ISSA
- Sans Cyber Aces, Infosec Institute, Cybrary


Recommended Reading:
- The Hacker Playbook 1 & 2
- Penetration Testing
- Metasploit
- Hacking The Art of Exploitation
- Professional Penetration Testing
- The Art Of Intrusion
- The Art of Deception
- Ghost in the Wires
- Black Hat Python

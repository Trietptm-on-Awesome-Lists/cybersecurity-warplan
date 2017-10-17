
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

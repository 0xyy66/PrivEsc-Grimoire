# PrivEsc Grimoire

<img src="https://user-images.githubusercontent.com/72035730/193342866-c4c43c70-5b7b-4aa4-836d-dfb29e91f8fd.png" alt="drawing" width="500"/>

### Privilege Escalation Grimoire

A bit of contest: 

I'm always too lazy to open the browser to find ways to take advantage of a sudo or suid misconfiguration when I get shells on systems during CTFs.
I prefer to stick to my black console.

That's why I created a command line tool to search for binaries privesc exploits.

The script reads from a json file created with [gtfobin-scrape] and lists the possible ways to escalate privileges with a binary.

Special thanks to [GTFOBins](https://github.com/GTFOBins).

![privescg-console]
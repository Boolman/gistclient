# Install:
```
pip install git+http://github.com/boolman/gistclient
```

# Usage:

## List gists of specified user
```bash
$ python gists.py ListGists --user boolman
https://api.github.com/gists/8f54862da4d40c5206c168108b6c073b
```

## List files/view content of files in specified Gist
```bash
$ python gists.py ViewGist --url https://api.github.com/gists/8f54862da4d40c5206c168108b6c073b                        
bash-script: {"content": "#!/bin/bash\n\n\necho ${foo}\n", "raw_url": "https://gist.githubusercontent.com/Boolman/8f54862da4d40c5206c168108b6c073b/raw/3eba204f9269ebf907add96f951ce82f907d7a9e/bash-script", "type": "text/plain", "size": 26, "language": "Shell", "filename": "bash-script", "truncated": false}
```

```bash
$ python gists.py ViewGist --url https://api.github.com/gists/8f54862da4d40c5206c168108b6c073b bash-script content
#!/bin/bash


echo ${foo}
```

## Add Gist
```bash
$ python gists.py AddGist --filepath foobar.sh --user boolman
```


## Delete Gist
```bash
$ python gists.py AddGist --filepath foobar.sh --user boolman
```

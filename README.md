<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_en.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_de.md">Deutsch</a> | <b>English</b> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_ru.md">Russian</a></p>

---

Library for adding and removing subdomains in CloudFlare.


### Hot to install

```sh
pip3 install cloudflare_api==0.0.3
```
                    

### How to use

```python
from cloudflare_api import CLOUDFLARE_API

email = '****@****'
token = '****'
domain = 'estate.im'

#add subdomain
add = CLOUDFLARE_API(domain=domain, email=email, token=token).addSubdomain(subdomain='new')
print(add)

#delete subdomain
delete = CLOUDFLARE_API(domain=domain, email=email, token=token).deleteSubdomain(subdomain='new')
print(delete)
		
```


<hr />

Version = 0.0.3 <br />
Library name = cloudflare_api <br />
Title = CloudFlare API <br />
Keywords = cloudflare api domain subdomains <br />


    

---

<p align="center"><b>🛠️ This repository was created using the <a href="https://gitupload.com">GitUpload</a>.</b></p>
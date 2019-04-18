<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_de.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><b>Deutsch</b> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_ru.md">Russian</a></p>

---

Bibliothek zum Hinzufügen und Entfernen von Unterdomänen in CloudFlare.


### Heiß zu installieren

```sh
pip3 install cloudflare_api==0.0.3
```


### Wie benutzt man

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
Bibliotheksname = cloudflare_api <br />
Titel = CloudFlare API <br />
Schlüsselwörter = cloudflare api domain subdomains <br />



---

<p align="center"><b>🛠️ Dieses Repository wurde mit <a href="https://gitupload.com">GitUpload</a> erstellt.</b></p>
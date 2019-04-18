<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_it.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_fr.md">French</a> | <b>Italian</b> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_ru.md">Russian</a></p>

---

Libreria per aggiungere e rimuovere sottodomini in CloudFlare.


### Caldo da installare

```sh
pip3 install cloudflare_api==0.0.3
```


### Come usare

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

Versione = 0.0.3 <br />
Nome libreria = cloudflare_api <br />
Title = CloudFlare API <br />
Parole chiave = cloudflare api domain subdomains <br />



---

<p align="center"><b>🛠️ Questo repository è stato creato usando <a href="https://gitupload.com">GitUpload</a>.</b></p>
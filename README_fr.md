<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_fr.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_es.md">Spanish</a> | <b>French</b> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_ru.md">Russian</a></p>

---

Bibliothèque pour ajouter et supprimer des sous-domaines dans CloudFlare.


### Chaud à installer

```sh
pip3 install cloudflare_api==0.0.3
```


### Comment utiliser

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
Nom de la bibliothèque = cloudflare_api <br />
Titre = CloudFlare API <br />
Mots-clés = cloudflare api domain subdomains <br />



---

<p align="center"><b>🛠️ Ce référentiel a été créé en utilisant le <a href="https://gitupload.com">GitUpload</a>.</b></p>
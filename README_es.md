<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_es.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README.md">English</a> | <b>Spanish</b> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_it.md">Italian</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_ru.md">Russian</a></p>

---

Biblioteca para agregar y eliminar subdominios en CloudFlare.


### Caliente para instalar

```sh
pip3 install cloudflare_api==0.0.1
```


### Cómo utilizar

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

Versión = 0.0.1 <br />
Nombre de la biblioteca = cloudflare_api <br />
Título = CloudFlare API <br />
Palabras clave = cloudflare api domain subdomains <br />



---

<p align="center"><b>🛠️ Este repositorio fue creado usando el <a href="https://gitupload.com">GitUpload</a>.</b></p>
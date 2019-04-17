<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>
<p align="center"><a href="https://gitupload.com"><img src="https://github.com/markolofsen/cloudflare_api//blob/master/.banners/banner_ru.jpg?raw=1" /></a></p>
<p align="center"><b>Languages:</b><br /><a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_de.md">Deutsch</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README.md">English</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_es.md">Spanish</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_fr.md">French</a> | <a href="https://github.com/markolofsen/cloudflare_api/blob/master/README_it.md">Italian</a> | <b>Russian</b></p>

---

Библиотека для добавления и удаления поддоменов в CloudFlare.


### Горячая установка

```sh
pip3 install cloudflare_api==0.0.2
```


### Как пользоваться

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

Версия = 0.0.2 <br />
Название библиотеки = cloudflare_api <br />
Название = CloudFlare API <br />
Ключевые слова = cloudflare api domain subdomains <br />



---

<p align="center"><b>🛠️ Этот репозиторий был создан с использованием <a href="https://gitupload.com">GitUpload</a>.</b></p>